from functions import login, print_dry_run

client = login()

# dataset_ref = client.dataset('chicago_taxi_trips', project='bigquery-public-data')
# dataset = client.get_dataset(dataset_ref)
# tables_list = list(client.list_tables(dataset))
# for table in tables_list:
#     print(table.table_id)
# table = dataset_ref.table('taxi_trips')
# preview = client.list_rows(table, max_results=5).to_dataframe()
# print(preview)
# preview.info()

# query_annual_trips = '''
#     SELECT
#         EXTRACT(YEAR FROM trip_start_timestamp) AS year,
#         COUNT(1) AS trips_count
#     FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
#     GROUP BY year
#     ORDER BY year DESC
# '''

# query_monthly_trips = '''
#     SELECT
#         EXTRACT(MONTH FROM trip_start_timestamp) AS month,
#         COUNT(1) AS trips_count
#     FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
#     WHERE EXTRACT(YEAR FROM trip_start_timestamp) = 2016
#     GROUP BY month
#     ORDER BY month
# '''

# print_dry_run(client, query_monthly_trips)
# job = client.query(query_monthly_trips)
# df = job.to_dataframe()
# print(df.head(12))

query_speed = '''
    WITH ParsedTable AS
    (
        SELECT 
            trip_start_timestamp,
            unique_key,
            trip_miles,
            trip_seconds
        FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
        WHERE 
            trip_start_timestamp > '2016-01-01'
            AND trip_start_timestamp < '2016-04-01'
            AND trip_seconds > 0
            AND trip_miles > 0
    )       
    SELECT 
        EXTRACT(HOUR FROM trip_start_timestamp) AS hour_of_day,
        COUNT(1) AS trip_count,
        SUM(trip_miles) / SUM(trip_seconds) * 3600 AS avg_mph
    FROM ParsedTable
    GROUP BY hour_of_day
    ORDER BY trip_count
'''
print_dry_run(client, query_speed)
df = client.query(query_speed).to_dataframe()
print(df.head(24))
# df.info()