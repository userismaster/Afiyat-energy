# Generated by Django 4.2.7 on 2024-12-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('order', 'Order'), ('message', 'Message')], max_length=20)),
                ('object_id', models.IntegerField()),
                ('is_read', models.BooleanField(default=False)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('read_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Telegram Notification',
                'verbose_name_plural': 'Telegram Notifications',
                'ordering': ['-sent_at'],
            },
        ),
        migrations.CreateModel(
            name='TelegramSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_token', models.CharField(max_length=255, verbose_name='Bot Token')),
                ('admin_chat_id', models.CharField(max_length=255, verbose_name='Admin Chat ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Telegram Settings',
                'verbose_name_plural': 'Telegram Settings',
            },
        ),
    ]
