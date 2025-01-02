from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.utils.html import format_html
from .models import ProductCategory, Product, Order, OrderItem, ArticleCategory, Article, ProductImage, ProductDocument, ProductSpecification

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'created_at', 'updated_at']
    list_filter = ['parent', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Основная информация', {
            'fields': ('parent', 'image', 'icon_class')
        }),
        ('Русский язык', {
            'fields': ('name', 'description')
        }),
        ('English', {
            'fields': ('name_en', 'description_en'),
            'classes': ('collapse',)
        }),
        ('O\'zbek tili', {
            'fields': ('name_uz', 'description_uz'),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': ('slug',),
            'classes': ('collapse',)
        })
    )

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductDocumentInline(admin.TabularInline):
    model = ProductDocument
    extra = 1

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'available', 'is_popular', 'image_preview', 'created_at', 'translate_button']
    list_filter = ['available', 'is_popular', 'created_at', 'updated_at', 'category']
    list_editable = ['price', 'stock', 'available', 'is_popular']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductDocumentInline, ProductSpecificationInline]
    search_fields = ['name', 'name_en', 'name_uz', 'description']
    readonly_fields = ['image_preview']
    fieldsets = (
        ('Основная информация', {
            'fields': ('category', 'image', 'price', 'stock', 'available', 'is_popular')
        }),
        ('Русский язык', {
            'fields': ('name', 'description', 'specifications')
        }),
        ('English', {
            'fields': ('name_en', 'description_en', 'specifications_en'),
            'classes': ('collapse',)
        }),
        ('O\'zbek tili', {
            'fields': ('name_uz', 'description_uz', 'specifications_uz'),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': ('slug',),
            'classes': ('collapse',)
        })
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return ''
    image_preview.short_description = 'Превью'

    def translate_button(self, obj):
        if not obj.name_en or not obj.name_uz or not obj.description_en or not obj.description_uz:
            return format_html(
                '<a class="button" href="{}">Перевести</a>',
                f'/admin/catalog/product/{obj.id}/translate/'
            )
        return "Переведено"
    translate_button.short_description = 'Перевод'

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Русский язык', {
            'fields': ('name', 'description')
        }),
        ('English', {
            'fields': ('name_en', 'description_en'),
            'classes': ('collapse',)
        }),
        ('O\'zbek tili', {
            'fields': ('name_uz', 'description_uz'),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': ('slug',),
            'classes': ('collapse',)
        })
    )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'published', 'image_preview', 'created_at']
    list_filter = ['published', 'category', 'author', 'created_at']
    list_editable = ['published']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['image_preview', 'created_at', 'updated_at']
    fieldsets = (
        ('Основная информация', {
            'fields': ('category', 'author', 'image', 'published')
        }),
        ('Русский язык', {
            'fields': ('title', 'content')
        }),
        ('English', {
            'fields': ('title_en', 'content_en'),
            'classes': ('collapse',)
        }),
        ('O\'zbek tili', {
            'fields': ('title_uz', 'content_uz'),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': ('slug',),
            'classes': ('collapse',)
        }),
        ('Системная информация', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50"/>', obj.image.url)
        return ''
    image_preview.short_description = 'Предпросмотр'

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'price', 'quantity', 'get_total_price']
    can_delete = False

    def get_total_price(self, obj):
        return obj.total_price
    get_total_price.short_description = 'Сумма'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'email', 'created_at', 'get_total_price', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    readonly_fields = ['created_at']
    inlines = [OrderItemInline]
    fieldsets = (
        ('Информация о заказе', {
            'fields': (
                'status', 'created_at'
            )
        }),
        ('Информация о покупателе', {
            'fields': (
                ('first_name', 'last_name'),
                ('email', 'phone'),
                'address',
                'comment'
            )
        }),
    )

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'ФИО'

    def get_total_price(self, obj):
        return obj.total_price
    get_total_price.short_description = 'Сумма заказа'

class AfiyatAdminSite(admin.AdminSite):
    site_header = 'Afiyat Energy - Панель управления'
    site_title = 'Afiyat Energy'
    index_title = 'Управление сайтом'

    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Создаем кастомное меню
        custom_app_list = [
            {
                'name': 'Каталог',
                'app_label': 'catalog',
                'models': [
                    {
                        'name': 'Категории товаров',
                        'object_name': 'ProductCategory',
                        'admin_url': '/admin/catalog/productcategory/',
                        'add_url': '/admin/catalog/productcategory/add/',
                    },
                    {
                        'name': 'Товары',
                        'object_name': 'Product',
                        'admin_url': '/admin/catalog/product/',
                        'add_url': '/admin/catalog/product/add/',
                    },
                ],
            },
            {
                'name': 'Статьи',
                'app_label': 'articles',
                'models': [
                    {
                        'name': 'Категории статей',
                        'object_name': 'ArticleCategory',
                        'admin_url': '/admin/catalog/articlecategory/',
                        'add_url': '/admin/catalog/articlecategory/add/',
                    },
                    {
                        'name': 'Статьи',
                        'object_name': 'Article',
                        'admin_url': '/admin/catalog/article/',
                        'add_url': '/admin/catalog/article/add/',
                    },
                ],
            },
            {
                'name': 'Заказы',
                'app_label': 'orders',
                'models': [
                    {
                        'name': 'Заказы',
                        'object_name': 'Order',
                        'admin_url': '/admin/catalog/order/',
                        'add_url': '/admin/catalog/order/add/',
                    },
                ],
            },
            {
                'name': 'Обратная связь',
                'app_label': 'contacts',
                'models': [
                    {
                        'name': 'Сообщения',
                        'object_name': 'ContactMessage',
                        'admin_url': '/admin/contacts/contactmessage/',
                        'add_url': '/admin/contacts/contactmessage/add/',
                    },
                ],
            },
            {
                'name': 'Пользователи',
                'app_label': 'auth',
                'models': [
                    {
                        'name': 'Пользователи',
                        'object_name': 'User',
                        'admin_url': '/admin/auth/user/',
                        'add_url': '/admin/auth/user/add/',
                    },
                    {
                        'name': 'Группы',
                        'object_name': 'Group',
                        'admin_url': '/admin/auth/group/',
                        'add_url': '/admin/auth/group/add/',
                    },
                ],
            },
        ]

        return custom_app_list

admin_site = AfiyatAdminSite(name='admin')

# Регистрируем модели в нашем кастомном админ-сайте
admin_site.register(ProductCategory, ProductCategoryAdmin)
admin_site.register(Product, ProductAdmin)
admin_site.register(ArticleCategory, ArticleCategoryAdmin)
admin_site.register(Article, ArticleAdmin)
admin_site.register(Order, OrderAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
