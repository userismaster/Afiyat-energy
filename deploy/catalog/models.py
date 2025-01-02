from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
import os
from django.conf import settings

class ProductCategory(models.Model):
    name = models.CharField(_('Название'), max_length=200)
    name_en = models.CharField(_('Название (EN)'), max_length=200, blank=True)
    name_uz = models.CharField(_('Название (UZ)'), max_length=200, blank=True)
    
    slug = models.SlugField(_('URL'), max_length=200, unique=True)
    
    description = models.TextField(_('Описание'), blank=True)
    description_en = models.TextField(_('Описание (EN)'), blank=True)
    description_uz = models.TextField(_('Описание (UZ)'), blank=True)
    
    image = models.ImageField(_('Изображение'), upload_to='categories/', blank=True)
    icon_class = models.CharField(_('Класс иконки'), max_length=50, blank=True,
                                help_text=_('Например: fas fa-bolt'))
    parent = models.ForeignKey('self', verbose_name=_('Родительская категория'),
                             on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='children')
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_name(self, language='ru'):
        if language == 'en':
            return self.name_en or self.name
        elif language == 'uz':
            return self.name_uz or self.name
        return self.name

    def get_description(self, language='ru'):
        if language == 'en':
            return self.description_en or self.description
        elif language == 'uz':
            return self.description_uz or self.description
        return self.description

    def get_products(self):
        """Получить все товары категории, включая подкатегории"""
        products = self.products.all()
        for child in self.children.all():
            products = products | child.get_products()
        return products.distinct()

    @property
    def product_count(self):
        """Получить количество товаров в категории и подкатегориях"""
        count = self.products.count()
        for child in self.children.all():
            count += child.product_count
        return count

class Product(models.Model):
    category = models.ForeignKey('ProductCategory', verbose_name=_('Категория'),
                               related_name='products', on_delete=models.CASCADE)
    name = models.CharField(_('Название'), max_length=200)
    name_en = models.CharField(_('Название (EN)'), max_length=200, blank=True)
    name_uz = models.CharField(_('Название (UZ)'), max_length=200, blank=True)
    
    description = RichTextUploadingField(_('Описание'))
    description_en = RichTextUploadingField(_('Описание (EN)'), blank=True)
    description_uz = RichTextUploadingField(_('Описание (UZ)'), blank=True)
    
    specifications = RichTextUploadingField(_('Характеристики'), blank=True, null=True)
    specifications_en = RichTextUploadingField(_('Характеристики (EN)'), blank=True, null=True)
    specifications_uz = RichTextUploadingField(_('Характеристики (UZ)'), blank=True, null=True)
    
    slug = models.SlugField(_('URL'), max_length=200, unique=True)
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(_('На складе'), default=0)
    available = models.BooleanField(_('Доступен'), default=True)
    is_popular = models.BooleanField(_('Популярный товар'), default=False)
    image = models.ImageField(_('Изображение'), upload_to='products/images/', blank=True, null=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_name(self, language='ru'):
        """Получить название товара на указанном языке"""
        if language == 'en' and self.name_en:
            return self.name_en
        elif language == 'uz' and self.name_uz:
            return self.name_uz
        return self.name

    def get_description(self, language='ru'):
        """Получить описание товара на указанном языке"""
        if language == 'en' and self.description_en:
            return self.description_en
        elif language == 'uz' and self.description_uz:
            return self.description_uz
        return self.description

    def get_specifications(self, language='ru'):
        """Получить характеристики товара на указанном языке"""
        if language == 'en' and self.specifications_en:
            return self.specifications_en
        elif language == 'uz' and self.specifications_uz:
            return self.specifications_uz
        return self.specifications

    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[self.slug])

    def get_image_path(self):
        if self.image:
            return os.path.join(settings.MEDIA_ROOT, str(self.image))
        return None

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class ProductSpecification(models.Model):
    product = models.ForeignKey('Product', related_name='spec_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Название')
    value = models.CharField(max_length=255, verbose_name='Значение')

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товара'

    def __str__(self):
        return f"{self.name}: {self.value}"

class ProductDocument(models.Model):
    product = models.ForeignKey('Product', related_name='documents', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Название')
    file = models.FileField(upload_to='products/documents/', verbose_name='Файл')

    class Meta:
        verbose_name = 'Документ товара'
        verbose_name_plural = 'Документы товара'

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'

class ArticleCategory(models.Model):
    name = models.CharField(_('Название'), max_length=200)
    name_en = models.CharField(_('Название (EN)'), max_length=200, blank=True)
    name_uz = models.CharField(_('Название (UZ)'), max_length=200, blank=True)
    
    slug = models.SlugField(_('URL'), max_length=200, unique=True)
    
    description = models.TextField(_('Описание'), blank=True)
    description_en = models.TextField(_('Описание (EN)'), blank=True)
    description_uz = models.TextField(_('Описание (UZ)'), blank=True)
    
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)

    class Meta:
        verbose_name = _('Категория статей')
        verbose_name_plural = _('Категории статей')
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_name(self, language='ru'):
        if language == 'en':
            return self.name_en or self.name
        elif language == 'uz':
            return self.name_uz or self.name
        return self.name

    def get_description(self, language='ru'):
        if language == 'en':
            return self.description_en or self.description
        elif language == 'uz':
            return self.description_uz or self.description
        return self.description

class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, verbose_name=_('Категория'),
                               related_name='articles', on_delete=models.CASCADE)
    
    title = models.CharField(_('Заголовок'), max_length=200)
    title_en = models.CharField(_('Заголовок (EN)'), max_length=200, blank=True)
    title_uz = models.CharField(_('Заголовок (UZ)'), max_length=200, blank=True)
    
    slug = models.SlugField(_('URL'), max_length=200, unique=True)
    
    content = RichTextUploadingField(_('Содержание'))
    content_en = RichTextUploadingField(_('Содержание (EN)'), blank=True)
    content_uz = RichTextUploadingField(_('Содержание (UZ)'), blank=True)
    
    image = models.ImageField(_('Изображение'), upload_to='articles/')
    author = models.ForeignKey(User, verbose_name=_('Автор'), 
                             on_delete=models.CASCADE, 
                             related_name='articles')
    published = models.BooleanField(_('Опубликовано'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)

    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('catalog:article_detail', args=[self.slug])

    def get_title(self, language='ru'):
        if language == 'en':
            return self.title_en or self.title
        elif language == 'uz':
            return self.title_uz or self.title
        return self.title

    def get_content(self, language='ru'):
        if language == 'en':
            return self.content_en or self.content
        elif language == 'uz':
            return self.content_uz or self.content
        return self.content

class Cart(models.Model):
    session_key = models.CharField(max_length=255, unique=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.session_key}"

    def get_total_price(self):
        """Получить общую стоимость корзины"""
        return sum(item.get_total_price() for item in self.items.all())

    def get_total_quantity(self):
        """Получить общее количество товаров в корзине"""
        return sum(item.quantity for item in self.items.all())

    def add(self, product, quantity=1, override_quantity=False):
        """Добавить товар в корзину или обновить его количество"""
        try:
            cart_item = self.items.get(product=product)
            if override_quantity:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity
            cart_item.save()
        except CartItem.DoesNotExist:
            self.items.create(product=product, quantity=quantity)

    def remove(self, product):
        """Удалить товар из корзины"""
        try:
            cart_item = self.items.get(product=product)
            cart_item.delete()
        except CartItem.DoesNotExist:
            pass

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_cost(self):
        return self.quantity * self.product.price

    def get_total_price(self):
        """Получить общую стоимость позиции"""
        return self.quantity * self.product.price

class Order(models.Model):
    STATUS_CHOICES = (
        ('new', _('Новый')),
        ('processing', _('В обработке')),
        ('shipped', _('Отправлен')),
        ('delivered', _('Доставлен')),
        ('cancelled', _('Отменен')),
    )

    user = models.ForeignKey(User, verbose_name=_('Пользователь'),
                           on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(_('Имя'), max_length=50)
    last_name = models.CharField(_('Фамилия'), max_length=50)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Телефон'), max_length=20)
    address = models.TextField(_('Адрес доставки'))
    status = models.CharField(_('Статус'), max_length=20,
                           choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)
    comment = models.TextField(_('Комментарий к заказу'), blank=True)

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')
        ordering = ['-created_at']

    def __str__(self):
        return f'Заказ {self.id} от {self.first_name} {self.last_name}'

    @property
    def total_price(self):
        """Получить общую стоимость заказа"""
        return sum(item.total_price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_('Заказ'),
                           related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('Товар'),
                             on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(_('Количество'), default=1)

    class Meta:
        verbose_name = _('Товар в заказе')
        verbose_name_plural = _('Товары в заказе')

    def __str__(self):
        product_name = self.product.name if self.product else 'Удаленный товар'
        return f'{product_name} x {self.quantity}'

    @property
    def total_price(self):
        """Получить общую стоимость позиции"""
        return self.price * self.quantity
