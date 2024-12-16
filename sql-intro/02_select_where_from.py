from google.cloud import bigquery
from google.oauth2 import service_account

credential_file = '/home/kevin/Code/kaggle-learn/credentials/kaggle-learn-444706-a5d1c2262ee0.json'
credentials = service_account.Credentials.from_service_account_file(credential_file)
client = bigquery.Client(credentials=credentials)

project = 'bigquery-public-data'
dataset_ref = client.dataset("openaq", project=project)
dataset = client.get_dataset(dataset_ref)

tables = list(client.list_tables(dataset))
# for table in tables:
    # print(table.table_id)
table_id = 'global_air_quality'
table_ref = dataset_ref.table(table_id)
table = client.get_table(table_ref)

# df = client.list_rows(table, max_results=5).to_dataframe()
# print(df)

query = f"""
    SELECT city
    FROM `bigquery-public-data.openaq.global_air_quality`
    WHERE country = 'US'
"""

df = client.query(query).to_dataframe()
#print(df.city.value_counts().head())
print(df.info())