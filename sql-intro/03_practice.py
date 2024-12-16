import pandas as pd
from functions import login, print_dry_run
from pathlib import Path

# == Test local paraquet dataframe ==
# df_path = Path(__file__).parent / '03_popular_comments_alias.parquet'
# df = pd.read_parquet(df_path)
# print(df.head())
# sort_df = df.sort_values('f0_', ascending=False)
# print(f'\nHead: \n{sort_df.head()}')

# == Exercise 03 ==
client = login()

# dataset_ref = client.dataset(dataset_id='hacker_news', project='bigquery-public-data')
# dataset = client.get_dataset(dataset_ref)
# table_ref = dataset_ref.table('full')
# table = client.get_table(table_ref)
# preview = client.list_rows(table, max_results=5).to_dataframe()
# print(preview.columns)

# query = '''
#     SELECT `by` AS author, COUNT(1) AS NumPosts
#     FROM `bigquery-public-data.hacker_news.full`
#     GROUP BY author
#     HAVING COUNT(1) > 10000
# '''

# print_dry_run(client, query)
# job = client.query(query)
# authors_10k = job.to_dataframe()
# authors_10k.to_parquet('03_authors_10k.parquet')

# df_path = Path(__file__).parent / '03_authors_10k.parquet'
# df = pd.read_parquet(df_path)
# # print(df.head())
# sort_df = df.sort_values('NumPosts', ascending=False)
# print(f'\nHead: \n{sort_df.head()}')

query_deleted = '''
    SELECT COUNT(1)
    FROM `bigquery-public-data.hacker_news.full`
    WHERE deleted = True
'''

print_dry_run(client, query_deleted)

