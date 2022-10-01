# Generated by Django 4.1.1 on 2022-10-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Имя')),
                ('email', models.EmailField(max_length=300, verbose_name='Почта')),
                ('text_entry', models.TextField(max_length=4000, verbose_name='Текст записи')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('ACTIVE', 'Активно'), ('BLOCKED', 'Заблакировано')], default='ACTIVE', max_length=50, verbose_name='Статус')),
            ],
        ),
    ]
