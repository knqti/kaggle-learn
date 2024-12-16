from google.cloud import bigquery
from google.oauth2 import service_account

credential_file = '/home/kevin/Code/kaggle-learn/credentials/kaggle-learn-444706-a5d1c2262ee0.json'
credentials = service_account.Credentials.from_service_account_file(credential_file)
scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])

# Create a "Client" object
client = bigquery.Client(credentials=credentials)

# Construct a reference to the "hacker_news" dataset
dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")

# API request - fetch the dataset
#dataset = client.get_dataset(dataset_ref)

# List all the tables in the "hacker_news" dataset
# tables = list(client.list_tables(dataset))

# Print names of all tables in the dataset (there are four?)
# for table in tables:  
#     print(table.table_id)

# Reference the "full" table
table_ref = dataset_ref.table('full')

# API request - fetch the table
table = client.get_table(table_ref)
#print(table.schema)

# Make a Pandas dataframe
# Preview the first five lines of the "full" table
df = client.list_rows(table, max_results=5).to_dataframe()
#print(df.info())
print(df['by'])