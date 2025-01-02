from django.shortcuts import redirect, render
from catalog.models import Product, ProductCategory
from django.conf import settings
from django.db.models import Count, Q

def change_language(request):
    language = request.GET.get('lang', 'ru')
    if language in ['ru', 'en', 'uz']:
        request.session['language'] = language
    return redirect(request.META.get('HTTP_REFERER', '/'))

def home(request):
    # Получаем текущий язык из сессии или используем русский по умолчанию
    current_language = request.session.get('language', settings.LANGUAGE_CODE)
    
    # Получаем популярные товары
    popular_products = Product.objects.filter(is_popular=True, available=True)[:8]
    
    # Получаем популярные категории (с подсчетом количества товаров)
    popular_categories = ProductCategory.objects.annotate(
        total_products=Count('products', filter=Q(products__available=True))
    ).filter(parent__isnull=True)[:6]  # Только родительские категории
    
    # Подготавливаем данные с учетом языка
    products_data = []
    for product in popular_products:
        product_data = {
            'id': product.id,
            'slug': product.slug,
            'name': product.get_name(current_language),
            'description': product.get_description(current_language),
            'price': product.price,
            'image': product.image,
            'get_absolute_url': product.get_absolute_url(),
            'category': product.category,
            'stock': product.stock,
        }
        products_data.append(product_data)
    
    context = {
        'popular_products': products_data,
        'popular_categories': popular_categories,
        'current_language': current_language,
    }
    
    return render(request, 'pages/home.html', context)
