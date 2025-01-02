import os
import sqlite3
import json
from datetime import datetime

def get_mysql_type(sqlite_type):
    """Конвертирует тип SQLite в тип MySQL"""
    sqlite_type = sqlite_type.upper()
    if 'INTEGER' in sqlite_type:
        return 'INT'
    elif 'REAL' in sqlite_type:
        return 'DOUBLE'
    elif 'TEXT' in sqlite_type:
        return 'TEXT'
    elif 'BLOB' in sqlite_type:
        return 'BLOB'
    elif 'DATETIME' in sqlite_type:
        return 'DATETIME'
    elif 'BOOLEAN' in sqlite_type:
        return 'TINYINT(1)'
    elif 'VARCHAR' in sqlite_type:
        return sqlite_type
    else:
        return 'TEXT'

def convert_sqlite_to_sql():
    """Конвертирует базу данных SQLite в SQL дамп"""
    
    sqlite_file = 'db.sqlite3'
    output_file = 'database_dump.sql'
    database_name = 'salox289_afiyat'  # Обновленное имя базы данных с префиксом
    
    # Подключаемся к SQLite
    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()
    
    # Получаем список всех таблиц
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Добавляем заголовок SQL файла
        f.write("-- MySQL dump generated from SQLite\n")
        f.write(f"-- Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("SET FOREIGN_KEY_CHECKS=0;\n")
        f.write("SET SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO';\n")
        f.write("SET time_zone = '+00:00';\n\n")
        
        # Выбираем базу данных
        f.write(f"USE `{database_name}`;\n\n")
        
        # Обрабатываем каждую таблицу
        for table in tables:
            table_name = table[0]
            
            # Пропускаем системные таблицы SQLite
            if table_name.startswith('sqlite_'):
                continue
                
            print(f"Обработка таблицы: {table_name}")
            
            # Получаем структуру таблицы
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            
            # Создаем CREATE TABLE запрос
            f.write(f"\n-- Table structure for table `{table_name}`\n")
            f.write(f"DROP TABLE IF EXISTS `{table_name}`;\n")
            f.write(f"CREATE TABLE `{table_name}` (\n")
            
            # Добавляем определения колонок
            column_defs = []
            primary_key = None
            for col in columns:
                col_id, col_name, col_type, not_null, default, is_pk = col
                
                # Определяем тип MySQL
                mysql_type = get_mysql_type(col_type)
                
                # Особая обработка для session_key
                if table_name == 'django_session' and col_name == 'session_key':
                    mysql_type = 'VARCHAR(40)'
                
                # Собираем определение колонки
                col_def = f"  `{col_name}` {mysql_type}"
                if not_null:
                    col_def += " NOT NULL"
                if default is not None:
                    if isinstance(default, str):
                        col_def += f" DEFAULT '{default}'"
                    else:
                        col_def += f" DEFAULT {default}"
                if is_pk:
                    primary_key = col_name
                    # Добавляем AUTO_INCREMENT только для числовых первичных ключей
                    if mysql_type in ['INT', 'BIGINT']:
                        col_def += " AUTO_INCREMENT"
                
                column_defs.append(col_def)
            
            # Добавляем PRIMARY KEY
            if primary_key:
                column_defs.append(f"  PRIMARY KEY (`{primary_key}`)")
            
            f.write(",\n".join(column_defs))
            f.write("\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;\n\n")
            
            # Получаем все данные из таблицы
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()
            
            if rows:
                # Записываем данные
                f.write(f"-- Dumping data for table `{table_name}`\n")
                
                # Создаем INSERT запросы
                for row in rows:
                    values = []
                    for i, value in enumerate(row):
                        if value is None:
                            values.append('NULL')
                        elif isinstance(value, (int, float)):
                            values.append(str(value))
                        elif isinstance(value, bool):
                            values.append('1' if value else '0')
                        else:
                            # Проверяем, похоже ли значение на дату
                            try:
                                # Пытаемся распарсить дату
                                date_obj = datetime.strptime(str(value), '%Y-%m-%d %H:%M:%S.%f')
                                # Форматируем дату для MySQL
                                value = date_obj.strftime('%Y-%m-%d %H:%M:%S')
                            except ValueError:
                                # Если это не дата, просто продолжаем
                                pass
                            
                            # Экранируем специальные символы
                            value = str(value).replace("'", "''")
                            values.append(f"'{value}'")
                    
                    f.write(f"INSERT INTO `{table_name}` ({', '.join([f'`{c[1]}`' for c in columns])}) ")
                    f.write(f"VALUES ({', '.join(values)});\n")
                
                f.write("\n")
        
        # Добавляем footer
        f.write("\nSET FOREIGN_KEY_CHECKS=1;\n")
    
    conn.close()
    print(f"\nГотово! SQL дамп сохранен в файл: {output_file}")
    print("Теперь вы можете импортировать этот файл через phpMyAdmin")

if __name__ == '__main__':
    convert_sqlite_to_sql()
