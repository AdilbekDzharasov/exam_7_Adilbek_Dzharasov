from django.db import models
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    ACTIVE = 'ACTIVE', 'Активно'
    BLOCKED = 'BLOCKED', 'Заблакировано'


class Entry(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False, verbose_name='Имя')
    email = models.EmailField(max_length=300, null=False, blank=False, verbose_name='Почта')
    text_entry = models.TextField(max_length=4000, null=False, blank=False, verbose_name='Текст записи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=50, null=False, blank=False, choices=StatusChoices.choices, default=StatusChoices.ACTIVE, verbose_name='Статус')

    def __str__(self):
        return f"{self.name} - {self.text_entry} - {self.status}"

