from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(_('Имя'), max_length=100)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Телефон'), max_length=20, blank=True)
    subject = models.CharField(_('Тема'), max_length=200)
    message = models.TextField(_('Сообщение'))
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    is_read = models.BooleanField(_('Прочитано'), default=False)
    read_at = models.DateTimeField(_('Дата прочтения'), null=True, blank=True)
    is_processed = models.BooleanField(_('Обработано'), default=False)

    class Meta:
        verbose_name = _('Сообщение')
        verbose_name_plural = _('Сообщения')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

    def mark_as_read(self):
        """Отметить сообщение как прочитанное"""
        self.is_read = True
        self.read_at = timezone.now()
        self.save()

    def mark_as_processed(self):
        """Отметить сообщение как обработанное"""
        self.is_processed = True
        self.save()
