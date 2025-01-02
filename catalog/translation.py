from modeltranslation.translator import register, TranslationOptions
from .models import ProductCategory, Product

@register(ProductCategory)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'specifications')
