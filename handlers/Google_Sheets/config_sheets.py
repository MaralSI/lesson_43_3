from google_oauth2 import service_account
from googleapiclient.discovery import build



SERVICE_ACCOUNT_FILE = 'lesson_43_2.json'

cred = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)


google_sheet_id_users = '1mq7RdomF6gGpgSOwYZzfVZhdBybOJnQZta2armfCHpM'

service = build('sheets', 'v4', credentials=creds)

