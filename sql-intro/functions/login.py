from google.cloud import bigquery
from google.oauth2 import service_account
from pathlib import Path

def login():
    parent_path = Path(__file__).parents[1]
    secret_file = Path(parent_path) / 'credentials' / 'kaggle-learn-444706-a5d1c2262ee0.json'
    credentials = service_account.Credentials.from_service_account_file(secret_file)
    client = bigquery.Client(credentials=credentials)
    return client