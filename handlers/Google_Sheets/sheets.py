from Google_Sheets.config_sheets import service, google_sheet_id_users
from aiogram import Dispatcher, types

def update_google_sheet_products(name_product, size, price, product_id, category, info_product):
    try:
        range_name = 'Лист1!A:G'
        
        row = [name_product, size, price, product_id, category, info_product]
        
        service.spreadsheets().values().append(
            spreadsheetId=google_sheet_id_users,
            range=range_name,
            valueInputOption='RAW',
            insertDataOption='INSERT_ROWS',
            body={'values': [row]}
        ).execute()
        
        print(f'Данные - {row}')
        
    except Exception as e:
        print(f'Ошибка при добавлении в таблицу - {e}')
        