from .models import Product
from modeltranslation.translator import register, TranslationOptions

# регистрируем наши модели для перевода

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)  # указываем, какие именно поля надо переводить в виде кортежа
