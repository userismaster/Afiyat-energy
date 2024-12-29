# Afiyat Energy Website

Каталог продуктов для компании Afiyat Energy, специализирующейся на продаже удобрений и нефтепродуктов в Узбекистане.

## Установка

1. Создайте виртуальное окружение:
```bash
python -m venv venv
```

2. Активируйте виртуальное окружение:
```bash
# Windows
venv\Scripts\activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Выполните миграции:
```bash
python manage.py migrate
```

5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

6. Запустите сервер:
```bash
python manage.py runserver
```

## Основные функции

- Каталог продуктов (нефтепродукты и удобрения)
- Корзина покупок
- Система акций и скидок
- Форма обратной связи
- Административная панель
