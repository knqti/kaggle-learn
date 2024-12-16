from functions import login

client = login()

# dataset_ref = client.dataset('openaq', project='bigquery-public-data')
# dataset = client.get_dataset(dataset_ref)

# table_ref = dataset_ref.table('global_air_quality')
# table = client.get_table(table_ref)

# preview = client.list_rows(table, max_results=5).to_dataframe()
# print(preview)
# print(table.schema)

# first_query = '''
#     SELECT country
#     FROM `bigquery-public-data.openaq.global_air_quality`
#     WHERE unit = 'ppm'
# '''

# df = client.query(first_query).to_dataframe()
# print(df['country'].value_counts())
# print(df.shape[0])

query_unique_countries = '''
    SELECT DISTINCT country
    FROM `bigquery-public-data.openaq.global_air_quality`
    WHERE unit = 'ppm'
'''

# dry_run_config = bigquery.QueryJobConfig(dry_run=True)
# test_job = client.query(query_unique_countries, dry_run_config)
# print(f'This query will use {test_job.total_bytes_processed} bytes.')

df = client.query(query_unique_countries).to_dataframe()
print(f'Countries that use ppm: {df.shape[0]}')
print(df['country'].value_counts())