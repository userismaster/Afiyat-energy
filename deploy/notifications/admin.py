from django.contrib import admin
from .models import TelegramSettings, Notification

# Register your models here.

@admin.register(TelegramSettings)
class TelegramSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'enabled', 'created_at', 'updated_at')
    list_filter = ('enabled',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'sent', 'created_at', 'sent_at')
    list_filter = ('type', 'sent')
    search_fields = ('title', 'message')
    readonly_fields = ('created_at', 'sent_at')
    ordering = ('-created_at',)
