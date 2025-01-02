import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from telegram_bot.models import TelegramSettings

def setup_bot_settings():
    # Деактивируем все существующие настройки
    TelegramSettings.objects.all().update(is_active=False)
    
    # Создаем новые настройки
    TelegramSettings.objects.create(
        bot_token='7698230012:AAGudGNHAwyxeGhIRbLewF-zPf36DqowFJ0',
        admin_chat_id='1516663193',
        is_active=True
    )
    print('Telegram bot settings have been updated successfully!')

if __name__ == '__main__':
    setup_bot_settings()
