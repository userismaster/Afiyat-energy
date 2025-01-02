import json
import os
from django.conf import settings

def load_translations(language):
    file_path = os.path.join(settings.BASE_DIR, 'translations', f'{language}.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return {}

def translations(request):
    language = request.session.get('language', 'ru')
    return {
        'translations': load_translations(language),
        'current_language': language
    }

def cart(request):
    cart = request.session.get('cart', {})
    total_quantity = sum(item.get('quantity', 0) for item in cart.values())
    return {
        'cart': {
            'items': cart,
            'total_quantity': total_quantity
        }
    }
