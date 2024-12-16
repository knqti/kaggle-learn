import os
from google.cloud import bigquery
from google.oauth2 import service_account

def login():
    file = os.path.join(os.path.dirname(__file__), 'secrets', 'kaggle-learn-444706-a5d1c2262ee0.json')
    credentials = service_account.Credentials.from_service_account_file(file)
    client = bigquery.Client(credentials=credentials)
    return client
