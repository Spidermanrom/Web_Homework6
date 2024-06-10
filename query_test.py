import sqlite3
from random import randint

def query_starter(num: int = None):
    '''Функція для виконання вибірок та повернення результату в термінал'''
    # num - слугує для вибору файлу query з sql командами
    sql_string = str()
    # Якщо не вказати номер буде вибрано випадковий номер
    if num is None:
        num = randint(1,10)
    try: # Обробка помилки. Якщо файл відсутній
        # Читання файлу sql та перетворення його в строку
        with open(f'SQL/query_{num}.sql','r', encoding='utf-8') as file:
            sql_string = file.read()
    except FileNotFoundError:
        print('We have 10 querys for select. num must be 1-10')
        return
    try: # Обробка помилок sql - виведе в термінал повідомлення про помилку та закриє зєднання з бд
        # Підключення до бази даних
        conn = sqlite3.connect('hw_06_db.db')
        cursor = conn.cursor()
        # Виконання запиту в бд
        cursor.execute(sql_string)
        # Конвертація результату для виведення в термінал
        result = cursor.fetchall()
        for line in result:
            print(line)
        # Збереження змін та закриття з'єднання
        conn.commit()
        conn.close()
        return 
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()


def main():
    # Вказати номер вибірки яку потрібно отримати
    # Сама вибірка також може редагуватися в залежності від необхідних данних
    query_starter()

if __name__ == '__main__':
    main()