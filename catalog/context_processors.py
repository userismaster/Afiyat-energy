from .models import Cart

def cart(request):
    """
    Добавляет объект корзины и количество товаров в контекст всех шаблонов
    """
    cart = Cart.objects.filter(session_key=request.session.session_key).first()
    cart_count = cart.get_total_quantity() if cart else 0
    return {
        'cart': cart,
        'cart_count': cart_count
    }
