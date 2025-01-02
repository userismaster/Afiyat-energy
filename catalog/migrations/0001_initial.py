# Generated by Django 4.2.7 on 2024-12-28 12:09

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('name_en', models.CharField(blank=True, max_length=200, verbose_name='Название (EN)')),
                ('name_uz', models.CharField(blank=True, max_length=200, verbose_name='Название (UZ)')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, verbose_name='Описание (EN)')),
                ('description_uz', models.TextField(blank=True, verbose_name='Описание (UZ)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Категория статей',
                'verbose_name_plural': 'Категории статей',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(default='', max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.TextField(verbose_name='Адрес доставки')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('processing', 'В обработке'), ('shipped', 'Отправлен'), ('delivered', 'Доставлен'), ('cancelled', 'Отменен')], default='new', max_length=20, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий к заказу')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('name_en', models.CharField(blank=True, max_length=200, verbose_name='Название (EN)')),
                ('name_uz', models.CharField(blank=True, max_length=200, verbose_name='Название (UZ)')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание (EN)')),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание (UZ)')),
                ('specifications', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Характеристики')),
                ('specifications_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Характеристики (EN)')),
                ('specifications_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Характеристики (UZ)')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='На складе')),
                ('available', models.BooleanField(default=True, verbose_name='Доступен')),
                ('is_popular', models.BooleanField(default=False, verbose_name='Популярный товар')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/images/', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('value', models.CharField(max_length=255, verbose_name='Значение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec_items', to='catalog.product')),
            ],
            options={
                'verbose_name': 'Характеристика товара',
                'verbose_name_plural': 'Характеристики товара',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images/', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.product')),
            ],
            options={
                'verbose_name': 'Изображение товара',
                'verbose_name_plural': 'Изображения товара',
            },
        ),
        migrations.CreateModel(
            name='ProductDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('file', models.FileField(upload_to='products/documents/', verbose_name='Файл')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='catalog.product')),
            ],
            options={
                'verbose_name': 'Документ товара',
                'verbose_name_plural': 'Документы товара',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('name_en', models.CharField(blank=True, max_length=200, verbose_name='Название (EN)')),
                ('name_uz', models.CharField(blank=True, max_length=200, verbose_name='Название (UZ)')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, verbose_name='Описание (EN)')),
                ('description_uz', models.TextField(blank=True, verbose_name='Описание (UZ)')),
                ('image', models.ImageField(blank=True, upload_to='categories/', verbose_name='Изображение')),
                ('icon_class', models.CharField(blank=True, help_text='Например: fas fa-bolt', max_length=50, verbose_name='Класс иконки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='catalog.productcategory', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.productcategory', verbose_name='Категория'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'ordering': ['-added_at'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('title_en', models.CharField(blank=True, max_length=200, verbose_name='Заголовок (EN)')),
                ('title_uz', models.CharField(blank=True, max_length=200, verbose_name='Заголовок (UZ)')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Содержание')),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Содержание (EN)')),
                ('content_uz', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Содержание (UZ)')),
                ('image', models.ImageField(upload_to='articles/', verbose_name='Изображение')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='catalog.articlecategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-created_at'],
            },
        ),
    ]
