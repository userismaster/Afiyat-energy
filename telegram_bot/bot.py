import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.utils import timezone
from django.db.models import Q, OuterRef, Exists
from asgiref.sync import sync_to_async
from .models import TelegramSettings, TelegramNotification
from catalog.models import Order
from contacts.models import ContactMessage
from telegram.error import BadRequest

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Константы для callback данных
ORDERS_PAGE = 'orders_page'
MESSAGES_PAGE = 'messages_page'
MARK_READ_ORDER = 'mark_read_order'
MARK_READ_MESSAGE = 'mark_read_message'
ITEMS_PER_PAGE = 5

@sync_to_async
def get_active_settings():
    return TelegramSettings.objects.filter(is_active=True).first()

@sync_to_async
def get_orders(page=0):
    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    return list(Order.objects.all().order_by('-created_at')[start:end])

@sync_to_async
def get_orders_count():
    return Order.objects.count()

@sync_to_async
def get_messages(page=0):
    try:
        start = page * ITEMS_PER_PAGE
        end = start + ITEMS_PER_PAGE
        messages = list(ContactMessage.objects.all().order_by('-created_at')[start:end])
        logger.info(f"Found {len(messages)} messages, page {page}, start {start}, end {end}")
        return messages
    except Exception as e:
        logger.error(f"Error getting messages: {e}")
        return []

@sync_to_async
def get_messages_count():
    try:
        count = ContactMessage.objects.count()
        logger.info(f"Total messages count: {count}")
        return count
    except Exception as e:
        logger.error(f"Error getting messages count: {e}")
        return 0

@sync_to_async
def get_notification(type_, object_id):
    return TelegramNotification.objects.filter(
        type=type_,
        object_id=object_id
    ).first()

@sync_to_async
def mark_notification_as_read(type_, object_id):
    notification = TelegramNotification.objects.filter(
        type=type_,
        object_id=object_id
    ).first()
    if notification:
        notification.mark_as_read()
        return True
    return False

@sync_to_async
def get_unread_notifications():
    return list(TelegramNotification.objects.filter(is_read=False).order_by('-sent_at'))

@sync_to_async
def get_unread_orders():
    """Получить непрочитанные заказы"""
    from django.db.models import Q, OuterRef, Exists
    
    # Подзапрос для проверки наличия прочитанного уведомления
    read_notification = TelegramNotification.objects.filter(
        type='order',
        object_id=OuterRef('id'),
        is_read=True
    )
    
    # Получаем заказы, у которых нет прочитанного уведомления
    return list(Order.objects.annotate(
        has_read_notification=Exists(read_notification)
    ).filter(
        has_read_notification=False
    ).order_by('-created_at'))

@sync_to_async
def get_unread_messages():
    """Получить непрочитанные сообщения"""
    from django.db.models import Q, OuterRef, Exists
    
    # Подзапрос для проверки наличия прочитанного уведомления
    read_notification = TelegramNotification.objects.filter(
        type='message',
        object_id=OuterRef('id'),
        is_read=True
    )
    
    # Получаем сообщения, у которых нет прочитанного уведомления
    return list(ContactMessage.objects.annotate(
        has_read_notification=Exists(read_notification)
    ).filter(
        has_read_notification=False
    ).order_by('-created_at'))

@sync_to_async
def mark_order_as_read(order_id):
    """Отметить заказ как прочитанный"""
    try:
        # Получаем или создаем уведомление
        notification, created = TelegramNotification.objects.get_or_create(
            type='order',
            object_id=order_id,
            defaults={'is_read': True}
        )
        if not notification.is_read:
            notification.is_read = True
            notification.save(update_fields=['is_read'])
        return True
    except Exception as e:
        logger.error(f"Error marking order as read: {e}")
        return False

@sync_to_async
def mark_message_as_read(message_id):
    """Отметить сообщение как прочитанное"""
    try:
        message = ContactMessage.objects.get(id=message_id)
        # Отмечаем сообщение как прочитанное
        if not message.is_read:
            message.is_read = True
            message.read_at = timezone.now()
            message.save(update_fields=['is_read', 'read_at'])
        
        # Получаем или создаем уведомление
        notification, created = TelegramNotification.objects.get_or_create(
            type='message',
            object_id=message_id,
            defaults={'is_read': True}
        )
        if not notification.is_read:
            notification.is_read = True
            notification.save(update_fields=['is_read'])
        return True
    except Exception as e:
        logger.error(f"Error marking message as read: {e}")
        return False

@sync_to_async
def get_order_total_price(order):
    """Получить общую сумму заказа"""
    return order.total_price

def create_pagination_keyboard(current_page, total_items, callback_prefix):
    keyboard = []
    total_pages = (total_items + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
    
    row = []
    if current_page > 0:
        row.append(InlineKeyboardButton("◀️ Назад", callback_data=f"{callback_prefix}_{current_page-1}"))
    if current_page < total_pages - 1:
        row.append(InlineKeyboardButton("Вперед ▶️", callback_data=f"{callback_prefix}_{current_page+1}"))
    if row:
        keyboard.append(row)
    
    keyboard.append([InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")])
    return InlineKeyboardMarkup(keyboard)

def create_main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("📦 Заказы", callback_data=f"{ORDERS_PAGE}_0")],
        [InlineKeyboardButton("✉️ Сообщения", callback_data=f"{MESSAGES_PAGE}_0")],
        [InlineKeyboardButton("🔔 Непрочитанные", callback_data="unread")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    settings = await get_active_settings()
    if not settings or str(update.effective_chat.id) != settings.admin_chat_id:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Извините, у вас нет доступа к этому боту."
        )
        return

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            "👋 Добро пожаловать в панель администратора Afiyat Energy!\n\n"
            "Выберите раздел для просмотра:"
        ),
        reply_markup=create_main_menu_keyboard()
    )

async def view_orders(update: Update, context: ContextTypes.DEFAULT_TYPE, page=0):
    """Показать список заказов"""
    settings = await get_active_settings()
    if not settings or str(update.effective_chat.id) != settings.admin_chat_id:
        return

    orders = await get_orders(page)
    total_orders = await get_orders_count()

    if not orders:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="📦 Нет доступных заказов.",
            reply_markup=create_main_menu_keyboard()
        )
        return

    message = "📦 *Список заказов:*\n\n"
    
    for order in orders:
        notification = await get_notification('order', order.id)
        total = await get_order_total_price(order)
        
        status = "✅" if notification and notification.is_read else "🆕"
        status_display = order.get_status_display()
        
        order_text = (
            f"{status} *Заказ #{order.id}*\n"
            f"📅 Дата: `{order.created_at.strftime('%d.%m.%Y %H:%M')}`\n"
            f"👤 Клиент: _{order.first_name} {order.last_name}_\n"
            f"📱 Телефон: `{order.phone}`\n"
            f"📧 Email: `{order.email}`\n"
            f"💰 Сумма: `{total:,.0f} UZS`\n"
            f"📊 Статус: _{status_display}_\n"
        )
        if not notification or not notification.is_read:
            order_text += "└ [Отметить как прочитанное](callback:/mark_read_order_{order.id})\n"
        message += f"{order_text}\n"

    keyboard = create_pagination_keyboard(page, total_orders, ORDERS_PAGE)
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
        reply_markup=keyboard,
        parse_mode='Markdown'
    )

async def view_messages(update: Update, context: ContextTypes.DEFAULT_TYPE, page=0):
    """Показать список сообщений"""
    settings = await get_active_settings()
    if not settings or str(update.effective_chat.id) != settings.admin_chat_id:
        return

    messages = await get_messages(page)
    total_messages = await get_messages_count()

    if not messages:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="✉️ Нет доступных сообщений.",
            reply_markup=create_main_menu_keyboard()
        )
        return

    message_text = "✉️ *Список сообщений:*\n\n"
    keyboard = []

    for msg in messages:
        # Добавляем статус сообщения (прочитано/не прочитано)
        status = "✅" if msg.is_read else "🆕"
        message_text += (
            f"{status} *Сообщение #{msg.id}*\n"
            f"👤 От: {msg.name}\n"
            f"📧 Email: {msg.email}\n"
            f"📝 Тема: {msg.subject}\n"
            f"💬 Сообщение:\n{msg.message[:200]}{'...' if len(msg.message) > 200 else ''}\n"
            f"📅 Дата: {msg.created_at.strftime('%d.%m.%Y %H:%M')}\n\n"
        )
        
        # Добавляем кнопку для каждого сообщения
        button_text = "✅ Отметить как прочитанное" if not msg.is_read else "📝 Уже прочитано"
        keyboard.append([InlineKeyboardButton(
            f"{button_text} #{msg.id}",
            callback_data=f"mark_read_message_{msg.id}"
        )])

    # Добавляем кнопки пагинации
    pagination_buttons = []
    if page > 0:
        pagination_buttons.append(InlineKeyboardButton("⬅️ Назад", callback_data=f"{MESSAGES_PAGE}_{page-1}"))
    if (page + 1) * ITEMS_PER_PAGE < total_messages:
        pagination_buttons.append(InlineKeyboardButton("➡️ Вперед", callback_data=f"{MESSAGES_PAGE}_{page+1}"))
    
    if pagination_buttons:
        keyboard.append(pagination_buttons)
    
    # Добавляем кнопку возврата в главное меню
    keyboard.append([InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")])

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

async def view_unread(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать непрочитанные уведомления"""
    settings = await get_active_settings()
    if not settings or str(update.effective_chat.id) != settings.admin_chat_id:
        return

    unread_orders = await get_unread_orders()
    unread_messages = await get_unread_messages()

    if not unread_orders and not unread_messages:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="🔔 Нет непрочитанных уведомлений.",
            reply_markup=create_main_menu_keyboard()
        )
        return

    message_text = "🔔 *Непрочитанные уведомления:*\n\n"
    keyboard = []

    # Добавляем непрочитанные заказы
    if unread_orders:
        message_text += "*📦 Заказы:*\n\n"
        for order in unread_orders:
            total_price = await get_order_total_price(order)
            message_text += (
                f"🆕 *Заказ #{order.id}*\n"
                f"👤 От: {order.first_name} {order.last_name}\n"
                f"📱 Телефон: {order.phone}\n"
                f"💰 Сумма: {total_price:,.0f} UZS\n"
                f"📅 Дата: {order.created_at.strftime('%d.%m.%Y %H:%M')}\n\n"
            )
            keyboard.append([InlineKeyboardButton(
                f"✅ Отметить заказ #{order.id} как прочитанный",
                callback_data=f"mark_read_order_{order.id}"
            )])

    # Добавляем непрочитанные сообщения
    if unread_messages:
        if unread_orders:  # Добавляем разделитель, если есть и заказы, и сообщения
            message_text += "\n"
        message_text += "*✉️ Сообщения:*\n\n"
        for msg in unread_messages:
            message_text += (
                f"🆕 *Сообщение #{msg.id}*\n"
                f"👤 От: {msg.name}\n"
                f"📧 Email: {msg.email}\n"
                f"📝 Тема: {msg.subject}\n"
                f"💬 Сообщение:\n{msg.message[:200]}{'...' if len(msg.message) > 200 else ''}\n"
                f"📅 Дата: {msg.created_at.strftime('%d.%m.%Y %H:%M')}\n\n"
            )
            keyboard.append([InlineKeyboardButton(
                f"✅ Отметить сообщение #{msg.id} как прочитанное",
                callback_data=f"mark_read_message_{msg.id}"
            )])

    # Добавляем кнопку возврата в главное меню
    keyboard.append([InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")])

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    
    try:
        # Пытаемся ответить на callback query
        await query.answer()
        
        # Получаем данные из callback_data
        data = query.data
        
        if data == "main_menu":
            await start(update, context)
            return
        elif data == "unread":
            await view_unread(update, context)
            return
        elif data.startswith(ORDERS_PAGE):
            try:
                page = int(data.split('_')[-1])
                await view_orders(update, context, page)
            except (ValueError, IndexError):
                await view_orders(update, context, 0)
            return
        elif data.startswith(MESSAGES_PAGE):
            try:
                page = int(data.split('_')[-1])
                await view_messages(update, context, page)
            except (ValueError, IndexError):
                await view_messages(update, context, 0)
            return
        elif data.startswith('mark_read_order_'):
            order_id = int(data.split('_')[-1])
            success = await mark_order_as_read(order_id)
            
            if success:
                # Показываем обновленный список
                if update.callback_query.message.text.startswith('🔔'):
                    await view_unread(update, context)
                else:
                    await view_orders(update, context)
                await query.answer("✅ Заказ отмечен как прочитанный")
            else:
                await query.answer("❌ Ошибка: заказ не найден")
            return
        elif data.startswith('mark_read_message_'):
            message_id = int(data.split('_')[-1])
            success = await mark_message_as_read(message_id)
            
            if success:
                # Показываем обновленный список
                if update.callback_query.message.text.startswith('🔔'):
                    await view_unread(update, context)
                else:
                    await view_messages(update, context)
                await query.answer("✅ Сообщение отмечено как прочитанное")
            else:
                await query.answer("❌ Ошибка: сообщение не найдено")
    except BadRequest as e:
        if "Query is too old" in str(e):
            # Если callback устарел, отправляем новое сообщение
            await update.effective_message.reply_text(
                "Это меню устарело. Пожалуйста, используйте актуальное меню или начните сначала с помощью /start"
            )
        else:
            # Для других ошибок BadRequest
            await update.effective_message.reply_text(
                "Произошла ошибка. Пожалуйста, попробуйте снова или используйте /start"
            )
    except Exception as e:
        # Для всех остальных ошибок
        logger.error(f"Error in button_callback: {str(e)}")
        await update.effective_message.reply_text(
            "Произошла непредвиденная ошибка. Пожалуйста, попробуйте позже или используйте /start"
        )

def setup_bot(token: str):
    """Настройка и запуск бота"""
    application = ApplicationBuilder().token(token).build()
    
    # Регистрация обработчиков команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    return application
