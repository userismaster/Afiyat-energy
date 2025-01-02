from django.conf import settings
from .models import Cart, CartItem, Product

def get_or_create_cart(request):
    """Получить или создать корзину для текущей сессии"""
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def add_to_cart(request, product_id, quantity=1):
    """Добавить товар в корзину"""
    try:
        product = Product.objects.get(id=product_id, available=True)
        cart = get_or_create_cart(request)
        
        # Проверяем наличие товара
        if product.stock < quantity:
            return {
                'success': False,
                'error': f'Доступно только {product.stock} единиц товара'
            }
        
        # Добавляем или обновляем товар в корзине
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        return {
            'success': True,
            'cart_count': cart.get_total_quantity(),
            'cart_total': cart.get_total_price()
        }
        
    except Product.DoesNotExist:
        return {
            'success': False,
            'error': 'Товар не найден'
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def remove_from_cart(request, product_id):
    """Удалить товар из корзины"""
    try:
        cart = get_or_create_cart(request)
        CartItem.objects.filter(cart=cart, product_id=product_id).delete()
        
        return {
            'success': True,
            'cart_count': cart.get_total_quantity(),
            'cart_total': cart.get_total_price()
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def update_cart_quantity(request, product_id, quantity):
    """Обновить количество товара в корзине"""
    try:
        if quantity <= 0:
            return remove_from_cart(request, product_id)
            
        product = Product.objects.get(id=product_id, available=True)
        cart = get_or_create_cart(request)
        
        # Проверяем наличие товара
        if product.stock < quantity:
            return {
                'success': False,
                'error': f'Доступно только {product.stock} единиц товара'
            }
        
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity = quantity
        cart_item.save()
        
        return {
            'success': True,
            'cart_count': cart.get_total_quantity(),
            'cart_total': cart.get_total_price()
        }
        
    except CartItem.DoesNotExist:
        return {
            'success': False,
            'error': 'Товар не найден в корзине'
        }
    except Product.DoesNotExist:
        return {
            'success': False,
            'error': 'Товар не найден'
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def clear_cart(request):
    """Очистить корзину"""
    try:
        cart = get_or_create_cart(request)
        cart.items.all().delete()
        return {'success': True}
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }
