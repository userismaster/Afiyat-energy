from django.db import models
from django.conf import settings

# Create your models here.

class TelegramSettings(models.Model):
    bot_token = models.CharField(max_length=255, help_text="Токен Telegram бота")
    chat_id = models.CharField(max_length=255, help_text="ID чата или канала для уведомлений")
    enabled = models.BooleanField(default=True, help_text="Включить/выключить уведомления")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Настройки Telegram"
        verbose_name_plural = "Настройки Telegram"

    def __str__(self):
        return f"Telegram Bot Settings (Active: {self.enabled})"

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('order', 'Новый заказ'),
        ('message', 'Новое сообщение'),
    )

    type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=255)
    message = models.TextField()
    sent = models.BooleanField(default=False)
    error = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"

    def __str__(self):
        return f"{self.get_type_display()} - {self.title}"
