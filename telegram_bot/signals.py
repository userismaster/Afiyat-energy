from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone
from catalog.models import Order, ContactMessage
from .models import TelegramSettings, TelegramNotification
import telegram
import asyncio

async def send_telegram_message(chat_id: str, message: str, reply_markup=None):
    """Отправка сообщения в Telegram"""
    bot_settings = TelegramSettings.objects.filter(is_active=True).first()
    if not bot_settings:
        return
    
    bot = telegram.Bot(token=bot_settings.bot_token)
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=message,
            parse_mode='HTML',
            reply_markup=reply_markup
        )
    except Exception as e:
        print(f"Error sending Telegram message: {e}")

@receiver(post_save, sender=Order)
def order_notification(sender, instance, created, **kwargs):
    """Отправка уведомления о новом заказе"""
    if not created:
        return

    bot_settings = TelegramSettings.objects.filter(is_active=True).first()
    if not bot_settings:
        return

    # Создаем запись об уведомлении
    notification = TelegramNotification.objects.create(
        type='order',
        object_id=instance.id
    )

    message = (
        f"🆕 <b>Новый заказ #{instance.id}</b>\n\n"
        f"<b>Клиент:</b> {instance.first_name} {instance.last_name}\n"
        f"<b>Телефон:</b> {instance.phone}\n"
        f"<b>Email:</b> {instance.email}\n"
        f"<b>Сумма:</b> {instance.total_price} UZS\n\n"
        f"Нажмите кнопку «📦 Заказы» в меню для просмотра деталей"
    )

    # Отправляем сообщение асинхронно
    asyncio.create_task(send_telegram_message(bot_settings.admin_chat_id, message))

@receiver(post_save, sender=ContactMessage)
def message_notification(sender, instance, created, **kwargs):
    """Отправка уведомления о новом сообщении"""
    if not created:
        return

    bot_settings = TelegramSettings.objects.filter(is_active=True).first()
    if not bot_settings:
        return

    # Создаем запись об уведомлении
    notification = TelegramNotification.objects.create(
        type='message',
        object_id=instance.id
    )

    message = (
        f"🆕 <b>Новое сообщение #{instance.id}</b>\n\n"
        f"<b>От:</b> {instance.name}\n"
        f"<b>Email:</b> {instance.email}\n"
        f"<b>Тема:</b> {instance.subject}\n"
        f"<b>Сообщение:</b>\n{instance.message[:200]}{'...' if len(instance.message) > 200 else ''}\n\n"
        f"Нажмите кнопку «✉️ Сообщения» в меню для просмотра деталей"
    )

    # Отправляем сообщение асинхронно
    asyncio.create_task(send_telegram_message(bot_settings.admin_chat_id, message))

@receiver(post_save, sender=TelegramNotification)
def sync_notification_status(sender, instance, **kwargs):
    """Синхронизация статуса прочтения между TelegramNotification и моделями"""
    if instance.is_read:
        if instance.type == 'message':
            try:
                message = ContactMessage.objects.get(id=instance.object_id)
                if not message.is_read:
                    message.is_read = True
                    message.read_at = timezone.now()
                    message.save(update_fields=['is_read', 'read_at'])
            except ContactMessage.DoesNotExist:
                pass
