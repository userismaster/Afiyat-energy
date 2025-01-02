from django.core.management.base import BaseCommand
from telegram_bot.models import TelegramSettings
from telegram_bot.bot import setup_bot

class Command(BaseCommand):
    help = 'Runs the Telegram bot'

    def handle(self, *args, **options):
        settings = TelegramSettings.objects.filter(is_active=True).first()
        if not settings:
            self.stdout.write(self.style.ERROR('No active Telegram bot settings found'))
            return

        self.stdout.write(self.style.SUCCESS('Starting Telegram bot...'))
        application = setup_bot(settings.bot_token)
        application.run_polling()
