import os
import shutil
import subprocess

def clean_pyc_files():
    """Удаляет все .pyc файлы и __pycache__ директории"""
    for root, dirs, files in os.walk('.'):
        # Удаляем __pycache__ директории
        if '__pycache__' in dirs:
            shutil.rmtree(os.path.join(root, '__pycache__'))
        
        # Удаляем .pyc файлы
        for file in files:
            if file.endswith('.pyc'):
                os.remove(os.path.join(root, file))

def collect_static():
    """Собирает статические файлы"""
    subprocess.run(['python', 'manage.py', 'collectstatic', '--noinput'])

def compile_messages():
    """Компилирует файлы переводов"""
    subprocess.run(['python', 'manage.py', 'compilemessages'])

def create_deploy_directory():
    """Создает директорию для деплоя и копирует нужные файлы"""
    deploy_dir = 'deploy'
    
    # Создаем директорию если её нет
    if os.path.exists(deploy_dir):
        shutil.rmtree(deploy_dir)
    os.makedirs(deploy_dir)

    # Список файлов и директорий для копирования
    items_to_copy = [
        'manage.py',
        'requirements.txt',
        'passenger_wsgi.py',
        'core',
        'catalog',
        'contacts',
        'notifications',
        'static_root',
        'media_root',
        'templates',
        'translations',
    ]

    # Копируем файлы и директории
    for item in items_to_copy:
        if os.path.exists(item):
            if os.path.isdir(item):
                shutil.copytree(item, os.path.join(deploy_dir, item))
            else:
                shutil.copy2(item, deploy_dir)

def main():
    print("Начинаем подготовку к деплою...")
    
    print("1. Очистка .pyc файлов и __pycache__...")
    clean_pyc_files()
    
    print("2. Сбор статических файлов...")
    collect_static()
    
    print("3. Компиляция файлов переводов...")
    compile_messages()
    
    print("4. Создание директории для деплоя...")
    create_deploy_directory()
    
    print("\nПодготовка завершена!")
    print("Теперь вы можете заархивировать содержимое папки 'deploy' и загрузить на сервер.")

if __name__ == '__main__':
    main()
