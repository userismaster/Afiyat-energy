from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class TelegramSettings(models.Model):
    bot_token = models.CharField(max_length=255, verbose_name="Bot Token")
    admin_chat_id = models.CharField(max_length=255, verbose_name="Admin Chat ID")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Telegram Settings"
        verbose_name_plural = "Telegram Settings"

    def __str__(self):
        return f"Telegram Bot Settings (Active: {self.is_active})"

class TelegramNotification(models.Model):
    NOTIFICATION_TYPES = (
        ('order', 'Order'),
        ('message', 'Message'),
    )

    type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    object_id = models.IntegerField()  # ID заказа или сообщения
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-sent_at']
        verbose_name = "Telegram Notification"
        verbose_name_plural = "Telegram Notifications"

    def mark_as_read(self):
        if not self.is_read:
            self.is_read = True
            self.read_at = timezone.now()
            self.save()

    def __str__(self):
        return f"{self.get_type_display()} Notification ({self.sent_at})"
