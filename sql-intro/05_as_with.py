import pandas
import matplotlib
import matplotlib.pyplot as plt
import tkinter
from functions import login, print_dry_run

client = login()

dataset_ref = client.dataset('crypto_bitcoin', project='bigquery-public-data')
dataset = client.get_dataset(dataset_ref)
table_ref = dataset_ref.table('transactions')
table = client.get_table(table_ref)
preview = client.list_rows(table, max_results=5).to_dataframe()
# print(preview)
# print(preview.columns)

query = '''
    WITH DateOnly AS
    (
        SELECT DATE (block_timestamp) AS date
        FROM bigquery-public-data.crypto_bitcoin.transactions
    )
    SELECT
        date,
        COUNT(1) as total_transactions
    FROM DateOnly
    GROUP BY date
    ORDER BY date
'''

print_dry_run(client, query)
df = client.query(query).to_dataframe()
# print(df.head())
# df.info()
