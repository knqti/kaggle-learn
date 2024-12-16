import pandas
from functions import login, print_dry_run, bigquery

client = login()

# dataset_ref = client.dataset(dataset_id='hacker_news', project='bigquery-public-data')
# dataset = client.get_dataset(dataset_ref)

# tables_list = list(client.list_tables(dataset))
# for table in tables_list:
    # print(table.table_id)

# table_ref = dataset_ref.table('full')
# table = client.get_table(table_ref)

# preview = client.list_rows(table, max_results=5).to_dataframe()
# print(preview)
# print(f'Schema: {table.schema}')

# query = '''
#     SELECT parent, COUNT(id) 
#     FROM `bigquery-public-data.hacker_news.full`
#     GROUP BY parent
#     HAVING COUNT(id) > 10
# '''

# safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
# job = client.query(query, job_config=safe_config)

# popular_comments = job.to_dataframe()
# popular_comments.to_parquet('popular_comments.parquet')
# print(popular_comments)

query_alias = '''
    SELECT parent, COUNT(1) AS NumOfPosts
    FROM `bigquery-public-data.hacker_news.full`
    GROUP BY parent
    HAVING COUNT(1) > 10
'''

print_dry_run(client, query_alias)

job = client.query(query_alias)
popular_comments_alias = job.to_dataframe()
popular_comments_alias.to_parquet('03_popular_comments_alias.parquet')
