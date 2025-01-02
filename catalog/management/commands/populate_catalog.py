from django.core.management.base import BaseCommand
from catalog.models import ProductCategory, Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate catalog with test categories and products'

    def handle(self, *args, **kwargs):
        # Очищаем существующие данные
        ProductCategory.objects.all().delete()
        Product.objects.all().delete()

        # Создаем основную категорию "Удобрения"
        fertilizers = ProductCategory.objects.create(
            name='Удобрения',
            name_en='Fertilizers',
            name_uz='O\'g\'itlar',
            description='Широкий ассортимент высококачественных удобрений для различных культур',
            description_en='Wide range of high-quality fertilizers for various crops',
            description_uz='Turli ekinlar uchun yuqori sifatli o\'g\'itlarning keng assortimenti',
            slug='fertilizers'
        )

        # Создаем подкатегории
        macro = ProductCategory.objects.create(
            name='Удобрения с макроэлементами (NPK и S)',
            name_en='Macronutrient Fertilizers (NPK and S)',
            name_uz='Makroelementli o\'g\'itlar (NPK va S)',
            description='Удобрения, содержащие основные питательные элементы: азот, фосфор, калий и серу',
            description_en='Fertilizers containing essential nutrients: nitrogen, phosphorus, potassium, and sulfur',
            description_uz='Asosiy ozuqa elementlarini o\'z ichiga olgan o\'g\'itlar: azot, fosfor, kaliy va oltingugurt',
            slug='macro',
            parent=fertilizers
        )

        complex_fert = ProductCategory.objects.create(
            name='Комплексные минеральные удобрения',
            name_en='Complex Mineral Fertilizers',
            name_uz='Kompleks mineral o\'g\'itlar',
            description='Сбалансированные комплексные удобрения для различных типов почв и культур',
            description_en='Balanced complex fertilizers for various soil types and crops',
            description_uz='Turli tuproq va ekinlar uchun muvozanatlashtirilgan kompleks o\'g\'itlar',
            slug='complex',
            parent=fertilizers
        )

        water = ProductCategory.objects.create(
            name='Водорастворимые удобрения',
            name_en='Water-Soluble Fertilizers',
            name_uz='Suvda eruvchan o\'g\'itlar',
            description='Полностью растворимые удобрения для капельного полива и листовых подкормок',
            description_en='Fully soluble fertilizers for drip irrigation and foliar feeding',
            description_uz='Tomchilab sug\'orish va bargdan oziqlantirish uchun to\'liq eruvchan o\'g\'itlar',
            slug='water',
            parent=fertilizers
        )

        special = ProductCategory.objects.create(
            name='Специальные удобрения',
            name_en='Special Fertilizers',
            name_uz='Maxsus o\'g\'itlar',
            description='Специализированные удобрения для особых потребностей растений',
            description_en='Specialized fertilizers for specific plant needs',
            description_uz='O\'simliklarning maxsus ehtiyojlari uchun ixtisoslashtirilgan o\'g\'itlar',
            slug='special',
            parent=fertilizers
        )

        # Создаем продукты для каждой категории
        products_data = [
            # Макроэлементные удобрения (NPK и S) - 9 товаров
            {
                'category': macro,
                'name': 'OLTIN NPK(S) 5:17:10(7)',
                'name_en': 'OLTIN NPK(S) 5:17:10(7)',
                'name_uz': 'OLTIN NPK(S) 5:17:10(7)',
                'description': '''Комплексное удобрение с оптимальным балансом макроэлементов.
                Состав:
                - Азот (N): 5%
                - Фосфор (P): 17%
                - Калий (K): 10%
                - Сера (S): 7%
                
                Особенности:
                - Все элементы представлены в форме, доступной для быстрого усвоения растениями
                - Высокая водорастворимость фосфора обеспечивает быстрое развитие корневой системы
                - Сбалансированное содержание калия улучшает вкус и качество продукции
                - Сера способствует синтезу аминокислот, улучшая здоровье растений
                
                Рекомендуемое использование:
                - Подходит для картофеля, лука, чеснока, кукурузы и хлопка
                - Идеально для весеннего и осеннего внесения в грунт''',
                'description_uz': '''Makroelementlarning optimal muvozanatiga ega kompleks o'g'it.
                Tarkibi:
                - Azot (N): 5%
                - Fosfor (P): 17%
                - Kaliy (K): 10%
                - Oltingugurt (S): 7%
                
                Xususiyatlari:
                - Barcha elementlar o'simliklar tomonidan tez o'zlashtirilishi mumkin bo'lgan shaklda
                - Fosforning yuqori suvda eruvchanligi ildiz tizimining tez rivojlanishini ta'minlaydi
                - Kaliyning muvozanatlashgan tarkibi mahsulot ta'mi va sifatini yaxshilaydi
                - Oltingugurt aminokislotalar sinteziga yordam beradi, o'simliklar salomatligini yaxshilaydi
                
                Tavsiya etilgan foydalanish:
                - Kartoshka, piyoz, sarimsoq, makkajo'xori va g'o'za uchun mos keladi
                - Bahorda va kuzda tuproqqa kiritish uchun ideal''',
                'description_en': '''Complex fertilizer with optimal balance of macronutrients.
                Composition:
                - Nitrogen (N): 5%
                - Phosphorus (P): 17%
                - Potassium (K): 10%
                - Sulfur (S): 7%
                
                Features:
                - All elements are in a form readily available for plant uptake
                - High water solubility of phosphorus ensures rapid root system development
                - Balanced potassium content improves taste and product quality
                - Sulfur promotes amino acid synthesis, improving plant health
                
                Recommended use:
                - Suitable for potatoes, onions, garlic, corn and cotton
                - Perfect for spring and autumn soil application''',
                'price': Decimal('100000'),
                'stock': 100,
                'available': True,
                'slug': 'oltin-npk-s-5-17-10-7'
            },
            {
                'category': macro,
                'name': 'OLTIN NPK(S) 7:22:14(5)',
                'name_en': 'OLTIN NPK(S) 7:22:14(5)',
                'name_uz': 'OLTIN NPK(S) 7:22:14(5)',
                'description': '''Комплексное удобрение для улучшения корневой системы.
                Состав:
                - Азот (N): 7%
                - Фосфор (P): 22%
                - Калий (K): 14%
                - Сера (S): 5%
                
                Особенности:
                - Низкое содержание азота помогает избежать избытка зелёной массы в ущерб плодоношению
                - Высокий уровень фосфора способствует росту корневой системы, особенно в ранних стадиях развития
                - Сбалансированное содержание серы и калия улучшает устойчивость растений к болезням
                
                Рекомендуемое использование:
                - Подходит для многолетних трав, сахарной свеклы и картофеля
                - Эффективно для осеннего внесения на корнеплоды''',
                'description_uz': '''Ildiz tizimini yaxshilash uchun kompleks o'g'it.
                Tarkibi:
                - Azot (N): 7%
                - Fosfor (P): 22%
                - Kaliy (K): 14%
                - Oltingugurt (S): 5%
                
                Xususiyatlari:
                - Azotning past miqdori meva tugishiga zarar yetkazmagan holda yashil massaning ortiqcha bo'lishini oldini oladi
                - Fosforning yuqori darajasi, ayniqsa rivojlanishning dastlabki bosqichlarida ildiz tizimining o'sishiga yordam beradi
                - Oltingugurt va kaliyning muvozanatlashgan tarkibi o'simliklarning kasalliklarga chidamliligini oshiradi
                
                Tavsiya etilgan foydalanish:
                - Ko'p yillik o'tlar, qand lavlagi va kartoshka uchun mos keladi
                - Ildizmevalilar uchun kuzgi kiritish uchun samarali''',
                'description_en': '''Complex fertilizer for root system improvement.
                Composition:
                - Nitrogen (N): 7%
                - Phosphorus (P): 22%
                - Potassium (K): 14%
                - Sulfur (S): 5%
                
                Features:
                - Low nitrogen content helps avoid excess green mass without compromising fruiting
                - High phosphorus level promotes root system growth, especially in early development stages
                - Balanced sulfur and potassium content improves plant disease resistance
                
                Recommended use:
                - Suitable for perennial grasses, sugar beets and potatoes
                - Effective for autumn application on root crops''',
                'price': Decimal('110000'),
                'stock': 150,
                'available': True,
                'slug': 'oltin-npk-s-7-22-14-5'
            },
            {
                'category': macro,
                'name': 'OLTIN NPK(S) 12:24(8)',
                'name_en': 'OLTIN NPK(S) 12:24(8)',
                'name_uz': 'OLTIN NPK(S) 12:24(8)',
                'description': '''Комплексное удобрение с высоким содержанием фосфора.
                Состав:
                - Азот (N): 12%
                - Фосфор (P): 24%
                - Сера (S): 8%
                
                Особенности:
                - Богатый источник фосфора для улучшенного роста корней и повышения урожайности
                - Высокое содержание азота способствует быстрому росту вегетативной массы
                - Сера улучшает фотосинтез и образование хлорофилла
                
                Рекомендуемое использование:
                - Для пшеницы, овощей и фруктов
                - Применяется как основное удобрение при подготовке почвы''',
                'description_uz': '''Fosfor miqdori yuqori bo'lgan kompleks o'g'it.
                Tarkibi:
                - Azot (N): 12%
                - Fosfor (P): 24%
                - Oltingugurt (S): 8%
                
                Xususiyatlari:
                - Ildizlarning yaxshilangan o'sishi va hosildorlikni oshirish uchun fosforning boy manbai
                - Azotning yuqori miqdori vegetativ massaning tez o'sishiga yordam beradi
                - Oltingugurt fotosintez va xlorofill hosil bo'lishini yaxshilaydi
                
                Tavsiya etilgan foydalanish:
                - Bug'doy, sabzavotlar va mevalar uchun
                - Tuproqni tayyorlashda asosiy o'g'it sifatida qo'llaniladi''',
                'description_en': '''Complex fertilizer with high phosphorus content.
                Composition:
                - Nitrogen (N): 12%
                - Phosphorus (P): 24%
                - Sulfur (S): 8%
                
                Features:
                - Rich source of phosphorus for improved root growth and increased yield
                - High nitrogen content promotes rapid vegetative growth
                - Sulfur improves photosynthesis and chlorophyll formation
                
                Recommended use:
                - For wheat, vegetables and fruits
                - Applied as a base fertilizer in soil preparation''',
                'price': Decimal('115000'),
                'stock': 130,
                'available': True,
                'slug': 'oltin-npk-s-12-24-8'
            },
            {
                'category': macro,
                'name': 'OLTIN NPK 8:20:30',
                'name_en': 'OLTIN NPK 8:20:30',
                'name_uz': 'OLTIN NPK 8:20:30',
                'description': '''Комплексное удобрение с повышенным содержанием калия.
                Состав:
                - Азот (N): 8%
                - Фосфор (P): 20%
                - Калий (K): 30%
                
                Особенности:
                - Высокое содержание калия улучшает устойчивость растений к засухе и болезням
                - Подходит для всех видов культур, особенно для корнеплодов и овощей
                - Эффективно поддерживает рост и развитие растений в любых климатических условиях
                
                Рекомендуемое использование:
                - Применяется перед посевом или в начале вегетации
                - Идеально для культур с высокой потребностью в калии''',
                'description_uz': '''Kaliy miqdori yuqori bo'lgan kompleks o'g'it.
                Tarkibi:
                - Azot (N): 8%
                - Fosfor (P): 20%
                - Kaliy (K): 30%
                
                Xususiyatlari:
                - Kaliyning yuqori miqdori o'simliklarning qurg'oqchilik va kasalliklarga chidamliligini oshiradi
                - Barcha turdagi ekinlar, ayniqsa ildizmevalar va sabzavotlar uchun mos keladi
                - Har qanday iqlim sharoitida o'simliklarning o'sishi va rivojlanishini samarali qo'llab-quvvatlaydi
                
                Tavsiya etilgan foydalanish:
                - Ekishdan oldin yoki vegetatsiya boshida qo'llaniladi
                - Kaliyga bo'lgan ehtiyoji yuqori bo'lgan ekinlar uchun ideal''',
                'description_en': '''Complex fertilizer with increased potassium content.
                Composition:
                - Nitrogen (N): 8%
                - Phosphorus (P): 20%
                - Potassium (K): 30%
                
                Features:
                - High potassium content improves plant resistance to drought and diseases
                - Suitable for all types of crops, especially root vegetables
                - Effectively supports plant growth and development in any climatic conditions
                
                Recommended use:
                - Applied before sowing or at the beginning of vegetation
                - Perfect for crops with high potassium demand''',
                'price': Decimal('120000'),
                'stock': 140,
                'available': True,
                'slug': 'oltin-npk-8-20-30'
            },
            {
                'category': macro,
                'name': 'OLTIN NPK 8:24:24',
                'name_en': 'OLTIN NPK 8:24:24',
                'name_uz': 'OLTIN NPK 8:24:24',
                'description': '''Комплексное удобрение с повышенным содержанием фосфора и калия.
                Состав:
                - Азот (N): 8%
                - Фосфор (P): 24%
                - Калий (K): 24%
                
                Особенности:
                - Сбалансированное содержание фосфора и калия для оптимального развития растений
                - Улучшает корневую систему и повышает устойчивость к стрессам
                - Способствует лучшему цветению и формированию плодов
                
                Рекомендуемое использование:
                - Идеально для овощных культур и фруктовых деревьев
                - Применяется в период активного роста и плодоношения''',
                'description_uz': '''Fosfor va kaliy miqdori yuqori bo'lgan kompleks o'g'it.
                Tarkibi:
                - Azot (N): 8%
                - Fosfor (P): 24%
                - Kaliy (K): 24%
                
                Xususiyatlari:
                - O'simliklarning optimal rivojlanishi uchun fosfor va kaliyning muvozanatlashgan tarkibi
                - Ildiz tizimini yaxshilaydi va stresslarga chidamlilikni oshiradi
                - Yaxshi gullash va meva shakllanishiga yordam beradi
                
                Tavsiya etilgan foydalanish:
                - Sabzavot ekinlari va mevali daraxtlar uchun ideal
                - Faol o'sish va meva tugish davrida qo'llaniladi''',
                'description_en': '''Complex fertilizer with increased phosphorus and potassium content.
                Composition:
                - Nitrogen (N): 8%
                - Phosphorus (P): 24%
                - Potassium (K): 24%
                
                Features:
                - Balanced phosphorus and potassium content for optimal plant development
                - Improves root system and increases stress resistance
                - Promotes better flowering and fruit formation
                
                Recommended use:
                - Perfect for vegetable crops and fruit trees
                - Applied during active growth and fruiting period''',
                'price': Decimal('125000'),
                'stock': 160,
                'available': True,
                'slug': 'oltin-npk-8-24-24'
            },
            {
                'category': macro,
                'name': 'OLTIN NPK(S) 10:20:20(5)',
                'name_en': 'OLTIN NPK(S) 10:20:20(5)',
                'name_uz': 'OLTIN NPK(S) 10:20:20(5)',
                'description': '''Комплексное удобрение с серой.
                Состав:
                - Азот (N): 10%
                - Фосфор (P): 20%
                - Калий (K): 20%
                - Сера (S): 5%
                
                Особенности:
                - Способствует развитию мощной корневой системы
                - Улучшает засухоустойчивость и холодостойкость растений
                - Сбалансированное содержание макроэлементов повышает урожайность
                
                Рекомендуемое использование:
                - Для всех видов культур, включая овощи, фрукты и зерновые
                - Подходит для основного внесения и подкормок''',
                'description_uz': '''Oltingugurtli kompleks o'g'it.
                Tarkibi:
                - Azot (N): 10%
                - Fosfor (P): 20%
                - Kaliy (K): 20%
                - Oltingugurt (S): 5%
                
                Xususiyatlari:
                - Kuchli ildiz tizimining rivojlanishiga yordam beradi
                - O'simliklarning qurg'oqchilik va sovuqqa chidamliligini oshiradi
                - Makroelementlarning muvozanatlashgan tarkibi hosildorlikni oshiradi
                
                Tavsiya etilgan foydalanish:
                - Sabzavotlar, mevalar va don ekinlari kabi barcha turdagi ekinlar uchun
                - Asosiy kiritish va oziqlantirish uchun mos keladi''',
                'description_en': '''Complex fertilizer with sulfur.
                Composition:
                - Nitrogen (N): 10%
                - Phosphorus (P): 20%
                - Potassium (K): 20%
                - Sulfur (S): 5%
                
                Features:
                - Promotes development of powerful root system
                - Improves drought resistance and cold tolerance of plants
                - Balanced content of macronutrients increases yield
                
                Recommended use:
                - For all types of crops, including vegetables, fruits and cereals
                - Suitable for basic application and top dressing''',
                'price': Decimal('118000'),
                'stock': 170,
                'available': True,
                'slug': 'oltin-npk-s-10-20-20-5'
            },
            {
                'category': macro,
                'name': 'OLTIN NPK 20:10:10(10)',
                'name_en': 'OLTIN NPK 20:10:10(10)',
                'name_uz': 'OLTIN NPK 20:10:10(10)',
                'description': '''Комплексное удобрение с повышенным содержанием азота.
                Состав:
                - Азот (N): 20%
                - Фосфор (P): 10%
                - Калий (K): 10%
                - Сера (S): 10%
                
                Особенности:
                - Идеальное удобрение для азотных культур
                - Помогает растениям справляться с неблагоприятными условиями
                - Увеличивает урожайность за счёт улучшенного фотосинтеза
                
                Рекомендуемое использование:
                - Рекомендуется для использования в овощеводстве и садоводстве
                - Эффективно для культур, требующих азотного питания''',
                'description_uz': '''Azot miqdori yuqori bo'lgan kompleks o'g'it.
                Tarkibi:
                - Azot (N): 20%
                - Fosfor (P): 10%
                - Kaliy (K): 10%
                - Oltingugurt (S): 10%
                
                Xususiyatlari:
                - Azotli ekinlar uchun ideal o'g'it
                - O'simliklarga noqulay sharoitlarga bardosh berishga yordam beradi
                - Yaxshilangan fotosintez hisobiga hosildorlikni oshiradi
                
                Tavsiya etilgan foydalanish:
                - Sabzavotchilik va bog'dorchilikda foydalanish uchun tavsiya etiladi
                - Azotli oziqlanishni talab qiladigan ekinlar uchun samarali''',
                'description_en': '''Complex fertilizer with increased nitrogen content.
                Composition:
                - Nitrogen (N): 20%
                - Phosphorus (P): 10%
                - Potassium (K): 10%
                - Sulfur (S): 10%
                
                Features:
                - Perfect fertilizer for nitrogen-loving crops
                - Helps plants cope with adverse conditions
                - Increases yield through improved photosynthesis
                
                Recommended use:
                - Recommended for use in vegetable growing and horticulture
                - Effective for crops requiring nitrogen nutrition''',
                'price': Decimal('122000'),
                'stock': 145,
                'available': True,
                'slug': 'oltin-npk-20-10-10-10'
            },
            {
                'category': macro,
                'name': 'OLTIN NPK(S) 15:15:15(7)',
                'name_en': 'OLTIN NPK(S) 15:15:15(7)',
                'name_uz': 'OLTIN NPK(S) 15:15:15(7)',
                'description': '''Универсальное комплексное удобрение с серой.
                Состав:
                - Азот (N): 15%
                - Фосфор (P): 15%
                - Калий (K): 15%
                - Сера (S): 7%
                
                Особенности:
                - Универсальное сбалансированное удобрение для всех культур
                - Сера способствует образованию белков и укреплению растений
                - Улучшает качество продукции и повышает урожайность
                
                Рекомендуемое использование:
                - Для улучшения структуры почвы и плодородия
                - Подходит для всех сельскохозяйственных культур''',
                'description_uz': '''Oltingugurtli universal kompleks o'g'it.
                Tarkibi:
                - Azot (N): 15%
                - Fosfor (P): 15%
                - Kaliy (K): 15%
                - Oltingugurt (S): 7%
                
                Xususiyatlari:
                - Barcha ekinlar uchun universal muvozanatlashtirilgan o'g'it
                - Oltingugurt oqsillar hosil bo'lishiga va o'simliklarni mustahkamlashga yordam beradi
                - Mahsulot sifatini yaxshilaydi va hosildorlikni oshiradi
                
                Tavsiya etilgan foydalanish:
                - Tuproq tuzilishi va unumdorligini yaxshilash uchun
                - Barcha qishloq xo'jaligi ekinlari uchun mos keladi''',
                'description_en': '''Universal complex fertilizer with sulfur.
                Composition:
                - Nitrogen (N): 15%
                - Phosphorus (P): 15%
                - Potassium (K): 15%
                - Sulfur (S): 7%
                
                Features:
                - Universal balanced fertilizer for all crops
                - Sulfur promotes protein formation and plant strengthening
                - Improves product quality and increases yield
                
                Recommended use:
                - For improving soil structure and fertility
                - Suitable for all agricultural crops''',
                'price': Decimal('116000'),
                'stock': 155,
                'available': True,
                'slug': 'oltin-npk-s-15-15-15-7'
            },
            {
                'category': macro,
                'name': 'OLTIN NPK(S) 16:16:16(7)',
                'name_en': 'OLTIN NPK(S) 16:16:16(7)',
                'name_uz': 'OLTIN NPK(S) 16:16:16(7)',
                'description': '''Универсальное комплексное удобрение с повышенным содержанием NPK.
                Состав:
                - Азот (N): 16%
                - Фосфор (P): 16%
                - Калий (K): 16%
                - Сера (S): 7%
                
                Особенности:
                - Оптимальное соотношение питательных веществ для повышения урожайности
                - Сбалансированное содержание азота, фосфора и калия улучшает общий рост растений
                - Способствует улучшению структуры почвы, её водопроницаемости и аэрации
                
                Рекомендуемое использование:
                - Подходит для овощей, зерновых, фруктов и других культур
                - Рекомендуется для применения в качестве основного или дополнительного удобрения''',
                'description_uz': '''NPK miqdori yuqori bo'lgan universal kompleks o'g'it.
                Tarkibi:
                - Azot (N): 16%
                - Fosfor (P): 16%
                - Kaliy (K): 16%
                - Oltingugurt (S): 7%
                
                Xususiyatlari:
                - Hosildorlikni oshirish uchun ozuqa moddalarining optimal nisbati
                - Azot, fosfor va kaliyning muvozanatlashgan tarkibi o'simliklarning umumiy o'sishini yaxshilaydi
                - Tuproq tuzilishi, suv o'tkazuvchanligi va aeratsiyasini yaxshilashga yordam beradi
                
                Tavsiya etilgan foydalanish:
                - Sabzavotlar, don ekinlari, mevalar va boshqa ekinlar uchun mos keladi
                - Asosiy yoki qo'shimcha o'g'it sifatida qo'llash uchun tavsiya etiladi''',
                'description_en': '''Universal complex fertilizer with increased NPK content.
                Composition:
                - Nitrogen (N): 16%
                - Phosphorus (P): 16%
                - Potassium (K): 16%
                - Sulfur (S): 7%
                
                Features:
                - Optimal nutrient ratio for increased yield
                - Balanced content of nitrogen, phosphorus and potassium improves overall plant growth
                - Helps improve soil structure, water permeability and aeration
                
                Recommended use:
                - Suitable for vegetables, cereals, fruits and other crops
                - Recommended for use as main or supplementary fertilizer''',
                'price': Decimal('117000'),
                'stock': 165,
                'available': True,
                'slug': 'oltin-npk-s-16-16-16-7'
            },
            {
                'category': complex_fert,
                'name': 'OLTIN Mini Amophos',
                'name_en': 'OLTIN Mini Amophos',
                'name_uz': 'OLTIN Mini Amofos',
                'description': '''Комплексное фосфорное удобрение с добавлением азота.
                Состав:
                - Азот (N): 5%
                - Фосфор (P): 23%
                - Сера (S): 4%
                - Кальций (Ca): 12%
                
                Особенности:
                - Способствует улучшению почвенного плодородия и усвоению питательных веществ
                - Высокая концентрация фосфора стимулирует развитие корневой системы
                - Кальций улучшает структуру почвы и pH баланс
                
                Рекомендуемое использование:
                - Идеально подходит для применения на бедных фосфором почвах
                - Эффективно для предпосевной обработки и основного внесения''',
                'description_uz': '''Azot qo'shilgan kompleks fosforli o'g'it.
                Tarkibi:
                - Azot (N): 5%
                - Fosfor (P): 23%
                - Oltingugurt (S): 4%
                - Kalsiy (Ca): 12%
                
                Xususiyatlari:
                - Tuproq unumdorligini yaxshilashga va ozuqa moddalarining o'zlashtirilishiga yordam beradi
                - Fosforning yuqori konsentratsiyasi ildiz tizimining rivojlanishini rag'batlantiradi
                - Kalsiy tuproq tuzilishini va pH balansini yaxshilaydi
                
                Tavsiya etilgan foydalanish:
                - Fosfor kam bo'lgan tuproqlarda qo'llash uchun ideal
                - Ekishdan oldingi ishlov berish va asosiy kiritish uchun samarali''',
                'description_en': '''Complex phosphorus fertilizer with added nitrogen.
                Composition:
                - Nitrogen (N): 5%
                - Phosphorus (P): 23%
                - Sulfur (S): 4%
                - Calcium (Ca): 12%
                
                Features:
                - Promotes improvement of soil fertility and nutrient absorption
                - High phosphorus concentration stimulates root system development
                - Calcium improves soil structure and pH balance
                
                Recommended use:
                - Ideal for use on phosphorus-poor soils
                - Effective for pre-sowing treatment and basic application''',
                'price': Decimal('135000'),
                'stock': 120,
                'available': True,
                'slug': 'oltin-mini-amophos'
            },
            {
                'category': complex_fert,
                'name': 'OLTIN CarboPhos Tez 42:5',
                'name_en': 'OLTIN CarboPhos Tez 42:5',
                'name_uz': 'OLTIN CarboPhos Tez 42:5',
                'description': '''Быстродействующее азотно-фосфорное удобрение.
                Состав:
                - Азот (N): 42%
                - Фосфор (P): 5%
                
                Особенности:
                - Быстро восполняет дефицит азота в почве
                - Идеально подходит для устранения азотного голодания у растений
                - Эффективно работает на всех типах почв
                
                Рекомендуемое использование:
                - Используется в виде основного удобрения или подкормки
                - Применяется на стадии активного роста растений''',
                'description_uz': '''Tez ta'sir qiluvchi azot-fosforli o'g'it.
                Tarkibi:
                - Azot (N): 42%
                - Fosfor (P): 5%
                
                Xususiyatlari:
                - Tuproqdagi azot tanqisligini tezda to'ldiradi
                - O'simliklardagi azot tanqisligini bartaraf etish uchun ideal
                - Barcha tuproq turlarida samarali ishlaydi
                
                Tavsiya etilgan foydalanish:
                - Asosiy o'g'it yoki oziqlantirish sifatida ishlatiladi
                - O'simliklarning faol o'sish bosqichida qo'llaniladi''',
                'description_en': '''Fast-acting nitrogen-phosphorus fertilizer.
                Composition:
                - Nitrogen (N): 42%
                - Phosphorus (P): 5%
                
                Features:
                - Quickly replenishes nitrogen deficiency in soil
                - Perfect for eliminating nitrogen starvation in plants
                - Works effectively on all soil types
                
                Recommended use:
                - Used as basic fertilizer or top dressing
                - Applied during active plant growth stage''',
                'price': Decimal('140000'),
                'stock': 110,
                'available': True,
                'slug': 'oltin-carbophos-tez-42-5'
            },
            {
                'category': complex_fert,
                'name': 'Ammoniated Single Superphosphate (ASSP)',
                'name_en': 'Ammoniated Single Superphosphate (ASSP)',
                'name_uz': 'Ammoniylashtirilgan oddiy superfosfat (ASSP)',
                'description': '''Комплексное фосфорное удобрение с азотом и серой.
                Состав:
                - Азот (N): 4%
                - Фосфор (P): 20%
                - Сера (S): 12%
                
                Особенности:
                - Обеспечивает длительное фосфорное питание
                - Содержит серу в доступной для растений форме
                - Улучшает качество продукции
                
                Рекомендуемое использование:
                - Подходит для всех типов почв
                - Особенно эффективно для масличных культур''',
                'description_uz': '''Azot va oltingugurt qo'shilgan kompleks fosforli o'g'it.
                Tarkibi:
                - Azot (N): 4%
                - Fosfor (P): 20%
                - Oltingugurt (S): 12%
                
                Xususiyatlari:
                - Uzoq muddatli fosforli oziqlanishni ta'minlaydi
                - O'simliklar uchun qulay shaklda oltingugurtni o'z ichiga oladi
                - Mahsulot sifatini yaxshilaydi
                
                Tavsiya etilgan foydalanish:
                - Barcha tuproq turlari uchun mos keladi
                - Moyli ekinlar uchun ayniqsa samarali''',
                'description_en': '''Complex phosphorus fertilizer with nitrogen and sulfur.
                Composition:
                - Nitrogen (N): 4%
                - Phosphorus (P): 20%
                - Sulfur (S): 12%
                
                Features:
                - Provides long-term phosphorus nutrition
                - Contains sulfur in plant-available form
                - Improves product quality
                
                Recommended use:
                - Suitable for all soil types
                - Especially effective for oilseed crops''',
                'price': Decimal('128000'),
                'stock': 130,
                'available': True,
                'slug': 'ammoniated-single-superphosphate'
            },
            {
                'category': water,
                'name': 'OLTIN NPK Supra Blue 12:11:18(14)',
                'name_en': 'OLTIN NPK Supra Blue 12:11:18(14)',
                'name_uz': 'OLTIN NPK Supra Blue 12:11:18(14)',
                'description': '''Водорастворимое комплексное удобрение с серой.
                Состав:
                - Азот (N): 12%
                - Фосфор (P): 11%
                - Калий (K): 18%
                - Сера (S): 14%
                
                Особенности:
                - Полностью водорастворимое удобрение
                - Обеспечивает равномерное питание растений
                - Высокое содержание калия улучшает качество плодов
                - Сера способствует синтезу белков и аминокислот
                
                Рекомендуемое использование:
                - Подходит для корневого и листового внесения
                - Рекомендуется для овощных культур, фруктов и виноградников''',
                'description_uz': '''Oltingugurtli suvda eruvchan kompleks o'g'it.
                Tarkibi:
                - Azot (N): 12%
                - Fosfor (P): 11%
                - Kaliy (K): 18%
                - Oltingugurt (S): 14%
                
                Xususiyatlari:
                - To'liq suvda eruvchan o'g'it
                - O'simliklarning bir tekis oziqlanishini ta'minlaydi
                - Kaliyning yuqori miqdori mevalar sifatini yaxshilaydi
                - Oltingugurt oqsillar va aminokislotalar sinteziga yordam beradi
                
                Tavsiya etilgan foydalanish:
                - Ildizdan va bargdan kiritish uchun mos keladi
                - Sabzavot ekinlari, mevalar va uzumzorlar uchun tavsiya etiladi''',
                'description_en': '''Water-soluble complex fertilizer with sulfur.
                Composition:
                - Nitrogen (N): 12%
                - Phosphorus (P): 11%
                - Potassium (K): 18%
                - Sulfur (S): 14%
                
                Features:
                - Fully water-soluble fertilizer
                - Provides uniform plant nutrition
                - High potassium content improves fruit quality
                - Sulfur promotes protein and amino acid synthesis
                
                Recommended use:
                - Suitable for root and foliar application
                - Recommended for vegetable crops, fruits and vineyards''',
                'price': Decimal('155000'),
                'stock': 90,
                'available': True,
                'slug': 'oltin-npk-supra-blue-12-11-18-14'
            },
            {
                'category': water,
                'name': 'OLTIN NPK Supra Green 18:18:18+TE',
                'name_en': 'OLTIN NPK Supra Green 18:18:18+TE',
                'name_uz': 'OLTIN NPK Supra Green 18:18:18+TE',
                'description': '''Водорастворимое комплексное удобрение с микроэлементами.
                Состав:
                - Азот (N): 18%
                - Фосфор (P): 18%
                - Калий (K): 18%
                - Микроэлементы (TE): B, Zn, Cu, Mn, Fe, Mo
                
                Особенности:
                - Универсальное удобрение для всех типов почв
                - Подходит для использования как в открытом грунте, так и в теплицах
                - Микроэлементы в хелатной форме для лучшего усвоения
                
                Рекомендуемое использование:
                - Для зерновых, масличных, технических культур
                - Идеально для листовой подкормки''',
                'description_uz': '''Mikroelementli suvda eruvchan kompleks o'g'it.
                Tarkibi:
                - Azot (N): 18%
                - Fosfor (P): 18%
                - Kaliy (K): 18%
                - Mikroelementlar (TE): B, Zn, Cu, Mn, Fe, Mo
                
                Xususiyatlari:
                - Barcha tuproq turlari uchun universal o'g'it
                - Ochiq maydon va issiqxonalarda foydalanish uchun mos keladi
                - Yaxshi o'zlashtirilishi uchun xelat shaklidagi mikroelementlar
                
                Tavsiya etilgan foydalanish:
                - Don, moyli, texnik ekinlar uchun
                - Bargdan oziqlantirish uchun ideal''',
                'description_en': '''Water-soluble complex fertilizer with trace elements.
                Composition:
                - Nitrogen (N): 18%
                - Phosphorus (P): 18%
                - Potassium (K): 18%
                - Trace elements (TE): B, Zn, Cu, Mn, Fe, Mo
                
                Features:
                - Universal fertilizer for all soil types
                - Suitable for use both in open field and greenhouses
                - Chelated microelements for better absorption
                
                Recommended use:
                - For cereals, oilseeds, industrial crops
                - Perfect for foliar feeding''',
                'price': Decimal('165000'),
                'stock': 85,
                'available': True,
                'slug': 'oltin-npk-supra-green-18-18-18-te'
            },
            {
                'category': water,
                'name': 'OLTIN NPK Supra Yellow 13:40:13+TE',
                'name_en': 'OLTIN NPK Supra Yellow 13:40:13+TE',
                'name_uz': 'OLTIN NPK Supra Yellow 13:40:13+TE',
                'description': '''Водорастворимое удобрение с высоким содержанием фосфора.
                Состав:
                - Азот (N): 13%
                - Фосфор (P): 40%
                - Калий (K): 13%
                - Микроэлементы (TE): B, Zn, Cu, Mn, Fe, Mo
                
                Особенности:
                - Высокое содержание фосфора для развития корневой системы
                - Оптимально для использования в начальной стадии роста
                - Микроэлементы в хелатной форме
                
                Рекомендуемое использование:
                - Для всех типов культур, особенно требовательных к фосфору
                - Эффективно для корневой подкормки''',
                'description_uz': '''Fosfor miqdori yuqori bo'lgan suvda eruvchan o'g'it.
                Tarkibi:
                - Azot (N): 13%
                - Fosfor (P): 40%
                - Kaliy (K): 13%
                - Mikroelementlar (TE): B, Zn, Cu, Mn, Fe, Mo
                
                Xususiyatlari:
                - Ildiz tizimini rivojlantirish uchun fosforning yuqori miqdori
                - O'sishning boshlang'ich bosqichida foydalanish uchun optimal
                - Xelat shaklidagi mikroelementlar
                
                Tavsiya etilgan foydalanish:
                - Fosforga talabchan bo'lgan barcha turdagi ekinlar uchun
                - Ildizdan oziqlantirish uchun samarali''',
                'description_en': '''Water-soluble fertilizer with high phosphorus content.
                Composition:
                - Nitrogen (N): 13%
                - Phosphorus (P): 40%
                - Potassium (K): 13%
                - Trace elements (TE): B, Zn, Cu, Mn, Fe, Mo
                
                Features:
                - High phosphorus content for root system development
                - Optimal for use in early growth stage
                - Chelated microelements
                
                Recommended use:
                - For all types of crops, especially phosphorus-demanding ones
                - Effective for root feeding''',
                'price': Decimal('170000'),
                'stock': 75,
                'available': True,
                'slug': 'oltin-npk-supra-yellow-13-40-13-te'
            },
            {
                'category': water,
                'name': 'OLTIN NPK Supra Red 10:10:40+TE',
                'name_en': 'OLTIN NPK Supra Red 10:10:40+TE',
                'name_uz': 'OLTIN NPK Supra Red 10:10:40+TE',
                'description': '''Водорастворимое удобрение с высоким содержанием калия.
                Состав:
                - Азот (N): 10%
                - Фосфор (P): 10%
                - Калий (K): 40%
                - Микроэлементы (TE): B, Zn, Cu, Mn, Fe, Mo
                
                Особенности:
                - Высокое содержание калия для улучшения качества плодов
                - Повышает устойчивость к стрессовым условиям
                - Улучшает вкусовые качества продукции
                
                Рекомендуемое использование:
                - Для культур, требующих калийного питания
                - Идеально для применения в период созревания плодов''',
                'description_uz': '''Kaliy miqdori yuqori bo'lgan suvda eruvchan o'g'it.
                Tarkibi:
                - Azot (N): 10%
                - Fosfor (P): 10%
                - Kaliy (K): 40%
                - Mikroelementlar (TE): B, Zn, Cu, Mn, Fe, Mo
                
                Xususiyatlari:
                - Mevalar sifatini yaxshilash uchun kaliyning yuqori miqdori
                - Stress sharoitlariga chidamlilikni oshiradi
                - Mahsulotning ta'm xususiyatlarini yaxshilaydi
                
                Tavsiya etilgan foydalanish:
                - Kaliyga talabchan ekinlar uchun
                - Mevalarning pishish davrida qo'llash uchun ideal''',
                'description_en': '''Water-soluble fertilizer with high potassium content.
                Composition:
                - Nitrogen (N): 10%
                - Phosphorus (P): 10%
                - Potassium (K): 40%
                - Trace elements (TE): B, Zn, Cu, Mn, Fe, Mo
                
                Features:
                - High potassium content for improved fruit quality
                - Increases resistance to stress conditions
                - Improves taste qualities of products
                
                Recommended use:
                - For crops requiring potassium nutrition
                - Perfect for application during fruit ripening period''',
                'price': Decimal('175000'),
                'stock': 80,
                'available': True,
                'slug': 'oltin-npk-supra-red-10-10-40-te'
            },
            {
                'category': special,
                'name': 'OLTIN SOP Sulphate of Potash K:50%',
                'name_en': 'OLTIN SOP Sulphate of Potash K:50%',
                'name_uz': 'OLTIN SOP Kaliy Sulfat K:50%',
                'description': '''Специальное калийное удобрение.
                Состав:
                - Калий (K): 50%
                
                Особенности:
                - Не содержит хлор, идеально для культур, чувствительных к соли
                - Снижает солевой индекс почвы
                - Улучшает вкус, цвет и устойчивость продукции
                
                Рекомендуемое использование:
                - Идеально для фруктов, цветов, табака и овощей
                - Применяется для улучшения качества продукции''',
                'description_uz': '''Maxsus kaliy o'g'iti.
                Tarkibi:
                - Kaliy (K): 50%
                
                Xususiyatlari:
                - Xlor yo'q, tuzga sezgir ekinlar uchun ideal
                - Tuproqning tuz indeksini pasaytiradi
                - Mahsulotning ta'mi, rangi va chidamliligini yaxshilaydi
                
                Tavsiya etilgan foydalanish:
                - Mevalar, gullar, tamaki va sabzavotlar uchun ideal
                - Mahsulot sifatini yaxshilash uchun qo'llaniladi''',
                'description_en': '''Special potassium fertilizer.
                Composition:
                - Potassium (K): 50%
                
                Features:
                - Chlorine-free, perfect for salt-sensitive crops
                - Reduces soil salt index
                - Improves taste, color and product durability
                
                Recommended use:
                - Perfect for fruits, flowers, tobacco and vegetables
                - Used to improve product quality''',
                'price': Decimal('180000'),
                'stock': 60,
                'available': True,
                'slug': 'oltin-sop-sulphate-of-potash'
            },
            {
                'category': special,
                'name': 'Ammonium Chloride N:26%',
                'name_en': 'Ammonium Chloride N:26%',
                'name_uz': 'Ammoniy Xlorid N:26%',
                'description': '''Специальное азотное удобрение.
                Состав:
                - Азот (N): 26%
                
                Особенности:
                - Эффективен для всех типов почв и культур
                - Высокое содержание азота для активного роста
                - Быстрое усвоение растениями
                
                Рекомендуемое использование:
                - Для риса, сахарного тростника, хлопка и овощей
                - Вносится в почву в виде основного удобрения''',
                'description_uz': '''Maxsus azotli o'g'it.
                Tarkibi:
                - Azot (N): 26%
                
                Xususiyatlari:
                - Barcha tuproq turlari va ekinlar uchun samarali
                - Faol o'sish uchun azotning yuqori miqdori
                - O'simliklar tomonidan tez o'zlashtiriladi
                
                Tavsiya etilgan foydalanish:
                - Sholi, shakar qamish, paxta va sabzavotlar uchun
                - Asosiy o'g'it sifatida tuproqqa kiritiladi''',
                'description_en': '''Special nitrogen fertilizer.
                Composition:
                - Nitrogen (N): 26%
                
                Features:
                - Effective for all soil types and crops
                - High nitrogen content for active growth
                - Quick absorption by plants
                
                Recommended use:
                - For rice, sugarcane, cotton and vegetables
                - Applied to soil as basic fertilizer''',
                'price': Decimal('145000'),
                'stock': 95,
                'available': True,
                'slug': 'ammonium-chloride'
            }
        ]

        for product_data in products_data:
            Product.objects.create(**product_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated catalog'))
