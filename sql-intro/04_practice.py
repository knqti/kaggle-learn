import pandas
from functions import login, print_dry_run

client = login()

# == Preview Data ==
# dataset_ref = client.dataset("world_bank_intl_education", project="bigquery-public-data")
# dataset = client.get_dataset(dataset_ref)
# tables_list = list(client.list_tables(dataset))
# for table in tables_list:
#     print(table.table_id)
# table_ref = dataset_ref.table('international_education')
# table = client.get_table(table_ref)
# df = client.list_rows(table, max_results=5).to_dataframe()
# print(f'==Head==\n{df.head()}')
# print(f'==Info==')
# df.info()
# print(f'==Columns==\n {df.columns}')
# print(f'==Stats==\n {df.describe()}')

# query_ed_spend = '''
#     SELECT
#         country_name,
#         AVG(value) AS AvgEdSpdPct
#     FROM `bigquery-public-data.world_bank_intl_education.international_education`
#     WHERE 
#         indicator_code = 'SE.XPD.TOTL.GD.ZS'
#         AND year >= 2010 
#         AND year <= 2017
#     GROUP BY country_name
#     ORDER BY AvgEdSpdPct DESC
# '''
# print_dry_run(client, query_ed_spend)
# job_ed_spend = client.query(query_ed_spend)
# df = job_ed_spend.to_dataframe()
# print(df.head())
# print(df[df['country_name'].str.contains('United States', case=False)])
# print(df.shape)

query_interesting_codes = '''
    SELECT 
        indicator_code,
        indicator_name,
        COUNT(1) AS num_rows
    FROM `bigquery-public-data.world_bank_intl_education.international_education`
    WHERE year = 2016
    GROUP BY 
        indicator_code,
        indicator_name
    HAVING num_rows > 175
    ORDER BY num_rows DESC
'''
print_dry_run(client, query_interesting_codes)
job = client.query(query_interesting_codes)
df = job.to_dataframe()
print(df.head(10))