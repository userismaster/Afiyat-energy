from django.contrib import admin
from .models import TelegramSettings, TelegramNotification

# Register your models here.

@admin.register(TelegramSettings)
class TelegramSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

    def has_add_permission(self, request):
        # Разрешаем создать только одну запись настроек
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(TelegramNotification)
class TelegramNotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'object_id', 'is_read', 'sent_at', 'read_at')
    list_filter = ('type', 'is_read')
    readonly_fields = ('sent_at', 'read_at')
    search_fields = ('object_id',)
    ordering = ('-sent_at',)
