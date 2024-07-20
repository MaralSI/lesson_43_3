
CREATE_TABLE_STORE = """
    CREATE TABLE IF NOT EXISTS online_store
    (id INTERGER PRIMARY KEY AUTOINTEGER,
    name_product VARCHAR(255),
    size VACHAR(255)
    price VACHAR(255)
    photo TEXT
    product_id INTEGER
    )
"""


INSERT_STORE = """
    INSERT_INFO online_store(name_product, size, price, product_id, category, info_product, photo)
    VALUES(?, ?, ?, ?, ?, ?, ?)
"""