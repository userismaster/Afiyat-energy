from django.core.management.base import BaseCommand
from catalog.models import ArticleCategory, Article
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate blog with test categories and articles'

    def handle(self, *args, **kwargs):
        # Очищаем существующие данные
        ArticleCategory.objects.all().delete()
        Article.objects.all().delete()

        # Создаем автора
        author, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            author.set_password('admin')
            author.save()

        # Создаем категории блога
        news = ArticleCategory.objects.create(
            name='Новости компании',
            name_en='Company News',
            name_uz='Kompaniya yangiliklari',
            slug='news'
        )

        articles = ArticleCategory.objects.create(
            name='Статьи',
            name_en='Articles',
            name_uz='Maqolalar',
            slug='articles'
        )

        tips = ArticleCategory.objects.create(
            name='Советы по применению',
            name_en='Usage Tips',
            name_uz='Foydalanish bo\'yicha maslahatlar',
            slug='tips'
        )

        # Создаем статьи
        Article.objects.create(
            title='Открытие нового склада в Ташкенте',
            title_en='New Warehouse Opening in Tashkent',
            title_uz='Toshkentda yangi ombor ochilishi',
            slug='new-warehouse-opening',
            content='''
            Мы рады сообщить об открытии нового современного склада в Ташкенте!
            
            Новый склад оснащен:
            - Современным погрузочно-разгрузочным оборудованием
            - Системой климат-контроля
            - Автоматизированной системой учета
            
            Это позволит нам:
            1. Увеличить скорость обработки заказов
            2. Обеспечить оптимальные условия хранения удобрений
            3. Улучшить логистику в Ташкентской области
            ''',
            content_en='''
            We are excited to announce the opening of our new modern warehouse in Tashkent!
            
            The new warehouse is equipped with:
            - Modern loading and unloading equipment
            - Climate control system
            - Automated inventory management system
            
            This will allow us to:
            1. Increase order processing speed
            2. Ensure optimal storage conditions for fertilizers
            3. Improve logistics in the Tashkent region
            ''',
            content_uz='''
            Toshkentda yangi zamonaviy omborimiz ochilganini mamnuniyat bilan ma'lum qilamiz!
            
            Yangi ombor jihozlangan:
            - Zamonaviy yuklash va tushirish uskunalari
            - Iqlim nazorati tizimi
            - Avtomatlashtirilgan hisobga olish tizimi
            
            Bu bizga imkon beradi:
            1. Buyurtmalarni qayta ishlash tezligini oshirish
            2. O'g'itlarni saqlash uchun optimal sharoitlarni ta'minlash
            3. Toshkent viloyatida logistikani yaxshilash
            ''',
            category=news,
            author=author,
            published=True,
            created_at=timezone.now()
        )

        Article.objects.create(
            title='Правильное применение азотных удобрений',
            title_en='Proper Application of Nitrogen Fertilizers',
            title_uz='Azotli o\'g\'itlardan to\'g\'ri foydalanish',
            slug='proper-nitrogen-fertilizers',
            content='''
            Азотные удобрения являются важнейшим элементом питания растений.
            
            Основные правила применения:
            1. Вносите удобрения в правильные сроки
            2. Соблюдайте рекомендованные дозировки
            3. Учитывайте тип почвы и культуры
            
            Преимущества правильного применения:
            - Повышение урожайности
            - Улучшение качества продукции
            - Экономия средств
            ''',
            content_en='''
            Nitrogen fertilizers are an essential plant nutrient.
            
            Basic application rules:
            1. Apply fertilizers at the right time
            2. Follow recommended dosages
            3. Consider soil type and crops
            
            Benefits of proper application:
            - Increased yield
            - Improved product quality
            - Cost savings
            ''',
            content_uz='''
            Azotli o'g'itlar o'simliklarning eng muhim ozuqa elementi hisoblanadi.
            
            Asosiy qo'llash qoidalari:
            1. O'g'itlarni to'g'ri vaqtda qo'llang
            2. Tavsiya etilgan dozalarga rioya qiling
            3. Tuproq va ekin turini hisobga oling
            
            To'g'ri qo'llashning afzalliklari:
            - Hosildorlikni oshirish
            - Mahsulot sifatini yaxshilash
            - Mablag'larni tejash
            ''',
            category=tips,
            author=author,
            published=True,
            created_at=timezone.now()
        )

        Article.objects.create(
            title='Тренды в производстве удобрений 2024',
            title_en='Fertilizer Production Trends 2024',
            title_uz='O\'g\'it ishlab chiqarish tendentsiyalari 2024',
            slug='fertilizer-trends-2024',
            content='''
            Обзор основных трендов в производстве удобрений в 2024 году.
            
            Ключевые тенденции:
            1. Экологичное производство
            2. Умные удобрения
            3. Биостимуляторы
            
            Перспективы развития:
            - Внедрение новых технологий
            - Расширение ассортимента
            - Повышение эффективности
            ''',
            content_en='''
            Overview of main trends in fertilizer production in 2024.
            
            Key trends:
            1. Eco-friendly production
            2. Smart fertilizers
            3. Biostimulants
            
            Development prospects:
            - Implementation of new technologies
            - Product range expansion
            - Efficiency improvement
            ''',
            content_uz='''
            2024 yilda o'g'it ishlab chiqarishdagi asosiy tendentsiyalar sharhi.
            
            Asosiy tendentsiyalar:
            1. Ekologik ishlab chiqarish
            2. Aqlli o'g'itlar
            3. Biostimulyatorlar
            
            Rivojlanish istiqbollari:
            - Yangi texnologiyalarni joriy etish
            - Mahsulot turlarini kengaytirish
            - Samaradorlikni oshirish
            ''',
            category=articles,
            author=author,
            published=True,
            created_at=timezone.now()
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated blog'))
