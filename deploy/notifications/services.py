import requests
from django.utils import timezone
from .models import TelegramSettings, Notification

def send_telegram_message(message):
    """
    Отправляет сообщение через Telegram бота
    """
    try:
        settings = TelegramSettings.objects.filter(enabled=True).first()
        if not settings:
            return False, "Telegram notifications are disabled or not configured"

        url = f"https://api.telegram.org/bot{settings.bot_token}/sendMessage"
        data = {
            "chat_id": settings.chat_id,
            "text": message,
            "parse_mode": "HTML"
        }

        response = requests.post(url, data=data)
        response.raise_for_status()
        return True, None

    except Exception as e:
        return False, str(e)

def create_order_notification(order):
    """
    Создает уведомление о новом заказе
    """
    # Формируем сообщение о заказе
    message = f"""
🛍️ <b>Новый заказ #{order.id}</b>

👤 <b>Клиент:</b>
Имя: {order.first_name} {order.last_name}
Телефон: {order.phone}
Email: {order.email}

📦 <b>Товары:</b>
"""
    total = 0
    for item in order.items.all():
        product = item.product
        subtotal = item.quantity * item.price
        total += subtotal
        message += f"- {product.get_name('ru')} x {item.quantity} = {subtotal:,.2f} UZS\n"

    message += f"\n💰 <b>Итого:</b> {total:,.2f} UZS"

    if order.comment:
        message += f"\n\n💬 <b>Комментарий:</b>\n{order.comment}"

    # Создаем уведомление
    notification = Notification.objects.create(
        type='order',
        title=f'Новый заказ #{order.id}',
        message=message
    )

    # Отправляем уведомление
    success, error = send_telegram_message(message)
    
    if success:
        notification.sent = True
        notification.sent_at = timezone.now()
    else:
        notification.error = error
    
    notification.save()
    return success, error

def create_message_notification(contact_message):
    """
    Создает уведомление о новом сообщении
    """
    message = f"""
📨 <b>Новое сообщение</b>

👤 <b>От:</b>
Имя: {contact_message.name}
Email: {contact_message.email}
Телефон: {contact_message.phone}

📝 <b>Тема:</b> {contact_message.subject}

💬 <b>Сообщение:</b>
{contact_message.message}
"""

    # Создаем уведомление
    notification = Notification.objects.create(
        type='message',
        title=f'Новое сообщение от {contact_message.name}',
        message=message
    )

    # Отправляем уведомление
    success, error = send_telegram_message(message)
    
    if success:
        notification.sent = True
        notification.sent_at = timezone.now()
    else:
        notification.error = error
    
    notification.save()
    return success, error
