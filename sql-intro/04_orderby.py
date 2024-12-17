from functions import login, print_dry_run

client = login()

# dataset_ref = client.dataset("nhtsa_traffic_fatalities", project="bigquery-public-data")
# dataset = client.get_dataset(dataset_ref)

# table_list = list(client.list_tables(dataset))
# for table in table_list:
#     print(table.table_id)
# table_ref = dataset_ref.table('accident_2015')
# table = client.get_table(table_ref)

# preview = client.list_rows(table, max_results=5).to_dataframe()
# print(preview)

query = '''
    SELECT EXTRACT(DAYOFWEEK from timestamp_of_crash) AS DayOfWeek,
        COUNT(consecutive_number) AS AccidentCount,
        SUM(number_of_drunk_drivers) AS DrunkCount
    FROM `bigquery-public-data.nhtsa_traffic_fatalities.accident_2015`
    GROUP BY DayOfWeek
    ORDER BY AccidentCount DESC
'''
# print_dry_run(client, query)

job = client.query(query)
df = job.to_dataframe()
print(df)