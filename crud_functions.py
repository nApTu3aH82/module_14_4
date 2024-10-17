import sqlite3


# from product import *

def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
    ''')
    connection.commit()
    connection.close()


# первичное наполнение таблицы, вломы писать руками, использовалось разово :))
# for product in products:
#     cursor.execute('INSERT INTO Products(title, description, price) VALUES(?, ?, ?)',
#                    (product[0], product[1], product[2]))
# connection.commit()

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products_list = cursor.fetchall()
    connection.close()
    return products_list
