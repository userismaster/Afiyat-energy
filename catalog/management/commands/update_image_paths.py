from django.core.management.base import BaseCommand
from catalog.models import Product
import os
from django.conf import settings
import shutil

class Command(BaseCommand):
    help = 'Updates product image paths to use the correct directory structure'

    def handle(self, *args, **options):
        # Создаем директорию если её нет
        images_dir = os.path.join(settings.MEDIA_ROOT, 'products', 'images')
        os.makedirs(images_dir, exist_ok=True)

        products = Product.objects.all()
        moved_count = 0
        error_count = 0

        for product in products:
            if product.image:
                # Получаем текущий путь к файлу
                current_path = os.path.join(settings.MEDIA_ROOT, str(product.image))
                
                # Если файл находится в корневой папке products
                if os.path.exists(current_path) and 'products/images' not in str(product.image):
                    try:
                        # Формируем новый путь
                        filename = os.path.basename(current_path)
                        new_path = os.path.join(images_dir, filename)
                        
                        # Перемещаем файл
                        shutil.move(current_path, new_path)
                        
                        # Обновляем путь в базе данных
                        product.image = f'products/images/{filename}'
                        product.save()
                        
                        moved_count += 1
                        self.stdout.write(self.style.SUCCESS(
                            f'Successfully moved image for product {product.name}'
                        ))
                    except Exception as e:
                        error_count += 1
                        self.stdout.write(self.style.ERROR(
                            f'Error moving image for product {product.name}: {str(e)}'
                        ))

        self.stdout.write(self.style.SUCCESS(
            f'Finished! Moved {moved_count} images, encountered {error_count} errors'
        ))
