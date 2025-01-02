import os
import django
import sys
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from django.utils import timezone
from contacts.models import ContactMessage
from catalog.models import Order

ITEMS_PER_PAGE = 5  # Количество элементов на странице

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    await update.message.reply_text(
        "Привет! Я бот Afiyat Energy. Я помогу вам отслеживать новые заказы и сообщения.\n\n"
        "Доступные команды:\n"
        "/orders - Просмотр новых заказов\n"
        "/messages - Просмотр новых сообщений"
    )

def get_orders_keyboard(page: int, total_pages: int, orders):
    """Создает клавиатуру навигации для заказов"""
    keyboard = []
    
    # Кнопки для отметки заказов как прочитанных
    for order in orders:
        keyboard.append([
            InlineKeyboardButton(
                f"✅ Отметить заказ #{order.id} как обработанный",
                callback_data=f"mark_order_{order.id}"
            )
        ])
    
    # Кнопки навигации
    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton("⬅️ Назад", callback_data=f"orders_{page-1}"))
    if page < total_pages - 1:
        nav_buttons.append(InlineKeyboardButton("Вперед ➡️", callback_data=f"orders_{page+1}"))
    if nav_buttons:
        keyboard.append(nav_buttons)
    
    # Информация о странице
    keyboard.append([InlineKeyboardButton(
        f"Страница {page + 1} из {total_pages}",
        callback_data="page_info"
    )])
    
    return InlineKeyboardMarkup(keyboard)

def get_messages_keyboard(page: int, total_pages: int, messages):
    """Создает клавиатуру навигации для сообщений"""
    keyboard = []
    
    # Кнопки для отметки сообщений как обработанных
    for message in messages:
        keyboard.append([
            InlineKeyboardButton(
                f"✅ Отметить сообщение #{message.id} как обработанное",
                callback_data=f"mark_message_{message.id}"
            )
        ])
    
    # Кнопки навигации
    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton("⬅️ Назад", callback_data=f"messages_{page-1}"))
    if page < total_pages - 1:
        nav_buttons.append(InlineKeyboardButton("Вперед ➡️", callback_data=f"messages_{page+1}"))
    if nav_buttons:
        keyboard.append(nav_buttons)
    
    # Информация о странице
    keyboard.append([InlineKeyboardButton(
        f"Страница {page + 1} из {total_pages}",
        callback_data="page_info"
    )])
    
    return InlineKeyboardMarkup(keyboard)

def format_order(order: Order) -> str:
    """Форматирует заказ для отображения"""
    return (
        f"🛍 Заказ #{order.id}\n"
        f"👤 {order.first_name} {order.last_name}\n"
        f"📱 {order.phone}\n"
        f"📧 {order.email}\n"
        f"📍 {order.address}\n"
        f"💰 Сумма: {order.total_price} UZS\n"
        f"📝 Комментарий: {order.comment if order.comment else '-'}\n"
        f"🕒 Создан: {order.created_at.strftime('%d.%m.%Y %H:%M')}"
    )

def format_message(message: ContactMessage) -> str:
    """Форматирует сообщение для отображения"""
    return (
        f"✉️ Сообщение #{message.id}\n"
        f"👤 {message.name}\n"
        f"📱 {message.phone if message.phone else '-'}\n"
        f"📧 {message.email}\n"
        f"📝 Тема: {message.subject}\n"
        f"💬 Сообщение: {message.message}\n"
        f"🕒 Создано: {message.created_at.strftime('%d.%m.%Y %H:%M')}"
    )

async def show_orders(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 0):
    """Показывает список новых заказов"""
    # Получаем заказы за последние 24 часа
    yesterday = datetime.now() - timedelta(days=1)
    orders = Order.objects.filter(
        created_at__gte=yesterday,
        status='new'
    ).order_by('-created_at')
    
    total_orders = orders.count()
    if total_orders == 0:
        await update.effective_message.reply_text("Новых заказов нет.")
        return
    
    # Вычисляем общее количество страниц
    total_pages = (total_orders + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
    
    # Получаем заказы для текущей страницы
    start_idx = page * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE
    page_orders = orders[start_idx:end_idx]
    
    # Формируем сообщение
    message = f"📦 Новые заказы (всего: {total_orders}):\n\n"
    message += "\n\n".join(format_order(order) for order in page_orders)
    
    # Отправляем сообщение с клавиатурой навигации
    if update.callback_query:
        await update.callback_query.edit_message_text(
            text=message,
            reply_markup=get_orders_keyboard(page, total_pages, page_orders)
        )
    else:
        await update.message.reply_text(
            text=message,
            reply_markup=get_orders_keyboard(page, total_pages, page_orders)
        )

async def show_messages(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 0):
    """Показывает список новых сообщений"""
    # Получаем сообщения за последние 24 часа
    yesterday = timezone.now() - timedelta(days=1)
    messages = ContactMessage.objects.filter(
        created_at__gte=yesterday,
        is_processed=False
    ).order_by('-created_at')
    
    total_messages = messages.count()
    if total_messages == 0:
        await update.effective_message.reply_text("Новых сообщений нет.")
        return
    
    # Вычисляем общее количество страниц
    total_pages = (total_messages + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
    
    # Получаем сообщения для текущей страницы
    start_idx = page * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE
    page_messages = messages[start_idx:end_idx]
    
    # Формируем сообщение
    message = f"📨 Новые сообщения (всего: {total_messages}):\n\n"
    message += "\n\n".join(format_message(msg) for msg in page_messages)
    
    # Отправляем сообщение с клавиатурой навигации
    if update.callback_query:
        await update.callback_query.edit_message_text(
            text=message,
            reply_markup=get_messages_keyboard(page, total_pages, page_messages)
        )
    else:
        await update.message.reply_text(
            text=message,
            reply_markup=get_messages_keyboard(page, total_pages, page_messages)
        )

async def mark_order_as_processed(update: Update, context: ContextTypes.DEFAULT_TYPE, order_id: int):
    """Отмечает заказ как обработанный"""
    try:
        order = Order.objects.get(id=order_id)
        order.status = 'processing'  # или другой подходящий статус
        order.save()
        
        # Отправляем уведомление
        await update.callback_query.answer(f"Заказ #{order_id} отмечен как обработанный")
        
        # Обновляем список заказов
        # Получаем текущую страницу из callback_data предыдущего сообщения
        current_page = 0
        for row in update.callback_query.message.reply_markup.inline_keyboard:
            for button in row:
                if button.callback_data.startswith("orders_"):
                    current_page = int(button.callback_data.split("_")[1])
                    break
        
        await show_orders(update, context, current_page)
        
    except Order.DoesNotExist:
        await update.callback_query.answer("Ошибка: заказ не найден")
    except Exception as e:
        await update.callback_query.answer("Произошла ошибка при обработке заказа")
        print(f"Error marking order as processed: {e}")

async def mark_message_as_processed(update: Update, context: ContextTypes.DEFAULT_TYPE, message_id: int):
    """Отмечает сообщение как обработанное"""
    try:
        message = ContactMessage.objects.get(id=message_id)
        message.mark_as_processed()
        
        # Отправляем уведомление
        await update.callback_query.answer(f"Сообщение #{message_id} отмечено как обработанное")
        
        # Обновляем список сообщений
        # Получаем текущую страницу из callback_data предыдущего сообщения
        current_page = 0
        for row in update.callback_query.message.reply_markup.inline_keyboard:
            for button in row:
                if button.callback_data.startswith("messages_"):
                    current_page = int(button.callback_data.split("_")[1])
                    break
        
        await show_messages(update, context, current_page)
        
    except ContactMessage.DoesNotExist:
        await update.callback_query.answer("Ошибка: сообщение не найдено")
    except Exception as e:
        await update.callback_query.answer("Произошла ошибка при обработке сообщения")
        print(f"Error marking message as processed: {e}")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    
    if query.data == "page_info":
        # Игнорируем нажатие на информацию о странице
        await query.answer()
        return
    
    # Разбираем данные колбэка
    action = query.data.split('_')[0]
    
    if action == "mark":
        # Определяем тип и ID объекта для обработки
        obj_type = query.data.split('_')[1]
        obj_id = int(query.data.split('_')[2])
        
        if obj_type == "order":
            await mark_order_as_processed(update, context, obj_id)
        elif obj_type == "message":
            await mark_message_as_processed(update, context, obj_id)
    else:
        # Обработка навигации по страницам
        action, page = query.data.split('_')
        page = int(page)
        
        if action == "orders":
            await show_orders(update, context, page)
        elif action == "messages":
            await show_messages(update, context, page)
    
    await query.answer()

def main():
    """Запуск бота"""
    # Получаем токен из переменной окружения
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        print("Ошибка: не задан токен бота (TELEGRAM_BOT_TOKEN)")
        return
    
    # Создаем приложение
    application = Application.builder().token(token).build()
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("orders", show_orders))
    application.add_handler(CommandHandler("messages", show_messages))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Запускаем бота
    print("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    # Настройка Django
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()
    
    main()
