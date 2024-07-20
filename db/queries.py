
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