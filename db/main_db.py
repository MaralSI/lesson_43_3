import sqlite3
from db import queries


db = sqlite3.connect("db/online_store.sqlite3")
cursor = db.cursor()


async def sql_create():
    if db:
        cursor.execute(queries.CREATE_TABLE_STORE)
        cursor.execute(queries.CREATE_TABLE_PRODUCT_DETAIL)
        print('База данных подключена')
    db.commit()


async def sql_insert_store(name_product, size, price, productid, photo):
    cursor.execute(queries.INSERT_STORE, (
        name_product,
        size,
        price,
        productid,
        photo))
    db.commit()


async def sql_insert_detail_products(productid, category, infoproduct):
    cursor.execute(queries.INSERT_DETAIL_PRODUCTS, (
        productid,
        category,
        infoproduct))
    db.commit()

async def sql_insert_staff(fullname, age, position):
    cursor.execute(queries.INSERT_DETAIL_PRODUCTS, (
        fullname,
        age,
        position))
    db.commit()

async def sql_insert_list(name_product, numbers_product, price, info_product):
    cursor.execute(queries.INSERT_DETAIL_PRODUCTS, (
        name_product,
        numbers_product,
        price,
        info_product))
    db.commit()

async def sql_insert_order(name_product, size, amount_product, phone):
    cursor.execute(queries.INSERT_DETAIL_PRODUCTS, (
        name_product,
        size,
        amount_product,
        phone,
    db.commit()

