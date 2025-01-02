from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Min, Max, Count
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Product, ProductCategory, Article, ArticleCategory,
    Cart, CartItem, Order, OrderItem
)
from .cart import get_or_create_cart 
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import OrderForm
from decimal import Decimal
import json

def home(request):
    current_language = request.session.get('language', 'ru')
    
    # Получаем только корневые категории (без родителей)
    popular_categories = ProductCategory.objects.filter(parent=None).annotate(
        total_products=Count('products')
    ).order_by('-total_products')[:6]

    # Получаем популярные товары
    popular_products = Product.objects.filter(
        available=True, is_popular=True
    ).select_related('category').order_by('-created_at')[:8]

    context = {
        'popular_categories': popular_categories,
        'popular_products': popular_products,
        'current_language': current_language,
        'cart': get_or_create_cart(request),
    }
    return render(request, 'pages/home.html', context)

def about(request):
    current_language = request.session.get('language', 'ru')
    context = {
        'cart': get_or_create_cart(request),
    }
    return render(request, 'pages/about.html', context)

def blog(request):
    current_language = request.session.get('language', 'ru')
    
    # Получаем все опубликованные статьи, отсортированные по дате создания
    articles = Article.objects.filter(
        published=True
    ).select_related(
        'category', 'author'
    ).order_by('-created_at')

    # Пагинация
    paginator = Paginator(articles, 6)  # 6 статей на страницу
    page = request.GET.get('page')
    
    try:
        articles_page = paginator.page(page)
    except PageNotAnInteger:
        articles_page = paginator.page(1)
    except EmptyPage:
        articles_page = paginator.page(paginator.num_pages)

    # Применяем переводы к названиям статей и категорий
    for article in articles_page:
        article.title = article.get_title(current_language)
        article.content = article.get_content(current_language)
        if article.category:
            article.category.name = article.category.get_name(current_language)

    categories = ArticleCategory.objects.all()
    for category in categories:
        category.name = category.get_name(current_language)

    context = {
        'articles': articles_page,
        'categories': categories,
        'cart': get_or_create_cart(request),
    }
    return render(request, 'pages/blog.html', context)

def contacts(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # Создаем новое сообщение
            # ContactMessage.objects.create(
            #     name=name,
            #     email=email,
            #     phone=phone,
            #     subject=subject,
            #     message=message
            # )

            # Отправляем уведомление администратору
            send_mail(
                subject=f'Новое сообщение от {name}',
                message=f'От: {name}\nEmail: {email}\nТелефон: {phone}\n\n{message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )

            return JsonResponse({
                'status': 'success',
                'message': 'Сообщение успешно отправлено'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    context = {
        'cart': get_or_create_cart(request),
    }
    return render(request, 'pages/contacts.html', context)

def product_list(request, category_slug=None):
    # Получаем текущий язык из сессии
    current_language = request.session.get('language', 'ru')
    
    products = Product.objects.filter(available=True)
    categories = ProductCategory.objects.filter(parent=None)  # Получаем только корневые категории

    # Фильтрация по slug категории
    category = None
    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        products = products.filter(category=category)

    # Фильтрация по категориям из GET параметров
    selected_categories = request.GET.getlist('category')
    if selected_categories:
        products = products.filter(category_id__in=selected_categories)

    # Фильтрация по цене
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Фильтр по наличию
    in_stock = request.GET.get('in_stock')
    if in_stock:
        products = products.filter(stock__gt=0)

    # Сортировка
    sort = request.GET.get('sort', 'popular')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'new':
        products = products.order_by('-created_at')
    else:  # popular
        products = products.order_by('-id')

    # Пагинация
    paginator = Paginator(products, 12)  # 12 товаров на странице
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # Формируем строку параметров для пагинации
    query_params = ''
    for key, value in request.GET.items():
        if key != 'page':
            query_params += f'&{key}={value}'

    # Получаем диапазон цен для фильтра
    price_range = Product.objects.filter(available=True).aggregate(
        min_price=Min('price'),
        max_price=Max('price')
    )

    # Применяем переводы к названиям
    for product in products:
        product.name = product.get_name(current_language)
    
    for category in categories:
        category.name = category.get_name(current_language)

    context = {
        'products': products,
        'categories': categories,
        'category': category,
        'selected_categories': selected_categories,
        'sort': sort,
        'query_params': query_params,
        'price_range': price_range,
        'selected_min_price': min_price,
        'selected_max_price': max_price,
        'in_stock': in_stock == 'true',
        'cart': get_or_create_cart(request),
    }
    
    return render(request, 'pages/catalog.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    current_language = request.session.get('language', 'ru')
    
    # Получаем похожие товары из той же категории
    similar_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]
    
    # Получаем характеристики товара
    specifications = product.spec_items.all()
    
    # Получаем документы товара
    documents = product.documents.all()
    
    # Получаем дополнительные изображения товара
    product_images = product.images.all()
    
    # Получаем переведенный контент
    product_data = {
        'id': product.id,
        'name': product.get_name(current_language),
        'description': product.get_description(current_language),
        'specifications': product.get_specifications(current_language),
        'price': str(product.price).replace(',', '.'),  # Заменяем запятую на точку
        'stock': product.stock,
        'image': product.image,
        'category': product.category.get_name(current_language),
    }
    
    context = {
        'product': product,
        'product_data': product_data,
        'similar_products': similar_products,
        'specifications': specifications,
        'documents': documents,
        'product_images': product_images,
        'cart': get_or_create_cart(request),
    }
    return render(request, 'pages/product_detail.html', context)

def cart_view(request):
    """Отображение страницы корзины"""
    cart = get_or_create_cart(request)
    current_language = request.session.get('language', 'ru')
    
    # Загружаем переводы
    try:
        with open(f'translations/{current_language}.json', 'r', encoding='utf-8') as f:
            translations = json.load(f)
    except Exception as e:
        print(f"Error loading translations: {e}")
        translations = {
            'cart': {
                'empty': {
                    'title': 'Ваша корзина пуста',
                    'message': 'Добавьте товары в корзину, чтобы оформить заказ',
                    'button': 'Перейти в каталог'
                }
            }
        }
    
    # Вычисляем общую стоимость
    cart_total = sum(item.get_total_price() for item in cart.items.all())
    cart_items = cart.items.select_related('product').all()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'translations': translations,
        'current_language': current_language,
        'cart_total': cart_total
    }
    
    return render(request, 'pages/cart.html', context)

def get_or_create_cart(request):
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def add_to_cart(request, product_id, quantity):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    if not product.available or product.stock <= 0:
        return {
            'success': False,
            'error': 'Товар недоступен или отсутствует в наличии'
        }
    
    if quantity > product.stock:
        return {
            'success': False,
            'error': f'Доступно только {product.stock} единиц товара'
        }
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 0}
    )
    
    # Если товар уже есть в корзине, увеличиваем количество
    if not created:
        new_quantity = cart_item.quantity + quantity
        if new_quantity > product.stock:
            return {
                'success': False,
                'error': f'В корзине уже есть {cart_item.quantity} единиц товара. Доступно для добавления: {product.stock - cart_item.quantity}'
            }
        cart_item.quantity = new_quantity
    else:
        cart_item.quantity = quantity
    
    cart_item.save()
    
    return {
        'success': True,
        'cart_count': cart.get_total_quantity(),
        'message': 'Товар успешно добавлен в корзину'
    }

@require_POST
def cart_add(request):
    """Добавление товара в корзину через AJAX"""
    try:
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = int(data.get('quantity', 1))
        
        if not product_id:
            return JsonResponse({
                'success': False,
                'error': 'Не указан ID товара'
            })
        
        result = add_to_cart(request, product_id, quantity)
        return JsonResponse(result)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Неверный формат данных'
        })
    except ValueError:
        return JsonResponse({
            'success': False,
            'error': 'Неверное количество товара'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

@require_POST
def cart_remove(request):
    """Удаление товара из корзины"""
    try:
        data = json.loads(request.body)
        product_id = data.get('product_id')
        
        if not product_id:
            return JsonResponse({
                'success': False,
                'error': 'Не указан ID товара'
            })
        
        result = remove_from_cart(request, product_id)
        return JsonResponse(result)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Неверный формат данных'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

@require_POST
def cart_update(request):
    """Обновление количества товара в корзине"""
    try:
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = int(data.get('quantity', 1))
        
        if not product_id:
            return JsonResponse({
                'success': False,
                'error': 'Не указан ID товара'
            })
        
        result = update_cart_quantity(request, product_id, quantity)
        return JsonResponse(result)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Неверный формат данных'
        })
    except ValueError:
        return JsonResponse({
            'success': False,
            'error': 'Неверное количество товара'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

def article_detail(request, slug):
    current_language = request.session.get('language', 'ru')
    article = get_object_or_404(Article.objects.select_related('category', 'author'), slug=slug, published=True)
    
    # Применяем переводы
    article.title = article.get_title(current_language)
    article.content = article.get_content(current_language)
    if article.category:
        article.category.name = article.category.get_name(current_language)
    
    context = {
        'article': article,
        'cart': get_or_create_cart(request),
    }
    return render(request, 'pages/article_detail.html', context)

def checkout(request):
    """Оформление заказа"""
    cart = get_or_create_cart(request)
    current_language = request.session.get('language', settings.LANGUAGE_CODE)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                order = form.save(commit=False)
                if request.user.is_authenticated:
                    order.user = request.user
                order.save()
                
                # Сохраняем товары из корзины в заказ
                cart_items = cart.items.all()
                for item in cart_items:
                    OrderItem.objects.create(
                        order=order,
                        product=item.product,
                        price=item.product.price,
                        quantity=item.quantity
                    )
                
                # Очищаем корзину
                cart.items.all().delete()
                
                # Создаем уведомление о новом заказе
                from notifications.services import create_order_notification
                create_order_notification(order)
                
                # Перенаправляем на страницу успешного оформления
                return redirect('catalog:order_success', order_id=order.id)
                
            except Exception as e:
                messages.error(request, str(e))
    else:
        # Создаем форму с переведенными placeholder'ами
        form = OrderForm()
        for field in form.fields.values():
            field.widget.attrs['placeholder'] = ''  # Очищаем стандартные placeholder'ы
    
    cart_items = []
    cart_total = 0
    
    # Получаем все товары из корзины с оптимизацией запросов
    cart_items_queryset = cart.items.select_related('product').all()
    
    for item in cart_items_queryset:
        total_price = item.get_total_price()
        cart_items.append({
            'product': {
                'id': item.product.id,
                'name': item.product.get_name(current_language),
                'price': item.product.price,
                'image': item.product.image,
                'get_absolute_url': item.product.get_absolute_url()
            },
            'quantity': item.quantity,
            'total_price': total_price
        })
        cart_total += total_price
    
    return render(request, 'pages/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'cart_total': cart_total,
        'cart': cart,
    })

def order_success(request, order_id):
    """Успешное оформление заказа"""
    order = get_object_or_404(Order, id=order_id)
    cart = get_or_create_cart(request)
    return render(request, 'pages/order_success.html', {
        'order': order,
        'cart': cart
    })

def remove_from_cart(request, product_id):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return {
        'success': True,
        'cart_count': cart.get_total_quantity(),
        'cart_total': cart.get_total_price(),
        'message': 'Товар удален из корзины'
    }

def update_cart_quantity(request, product_id, quantity):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    if quantity > product.stock:
        return {
            'success': False,
            'error': f'Доступно только {product.stock} единиц товара'
        }
    
    cart.add(product, quantity, override_quantity=True)
    return {
        'success': True,
        'cart_count': cart.get_total_quantity(),
        'cart_total': cart.get_total_price(),
        'message': 'Корзина обновлена'
    }
