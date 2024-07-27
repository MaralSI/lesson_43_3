
CREATE_TABLE_STORE = """
    CREATE TABLE IF NOT EXISTS online_store
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255), 
    productid INTEGER,
    photo TEXT
    )
"""

INSERT_STORE = """
    INSERT INTO online_store(name_product, size, price, productid, photo)
    VALUES (?, ?, ?, ?, ?)
"""


CREATE_TABLE_PRODUCT_DETAIL = """
    CREATE TABLE IF NOT EXISTS products_detail
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid VARCHAR(255),
    category VARCHAR(255),
    infoproduct VARCHAR(255)
    )
"""

INSERT_DETAIL_PRODUCTS = """
    INSERT INTO products_detail(productid, category, infoproduct)
    VALUES (?, ?, ?)
"""


CREATE_STAFF = """
    CREATE TABLE IF NOT EXISTS staff
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(255),
    age VARCHAR(255),
    position VARCHAR(255)
    )
"""

INSERT_DETAIL_STAFF = """
    INSERT INTO products_detail(fullname, age, position)
    VALUES (?, ?, ?)
"""

CREATE_ORDER = """
    CREATE TABLE IF NOT EXISTS staff
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product VARCHAR(255),
    size VARCHAR(255),
    amount_product INTEGER,
    phone INTEGER,
    )
"""

INSERT_DETAIL_ORDER = """
    INSERT INTO products_detail(name_product, size, amount_product, phone)
    VALUES (?, ?, ?, ?)
"""

CREATE_LIST = """
    CREATE TABLE IF NOT EXISTS staff
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product VARCHAR(255),
    numbers_product INTEGER,
    price INTEGER,
    info_product VARCHAR(255)
    )
"""

INSERT_LIST = """
    INSERT INTO products_detail(name_product, numbers_product, price, info_product)
    VALUES (?, ?, ?, ?)
"""
