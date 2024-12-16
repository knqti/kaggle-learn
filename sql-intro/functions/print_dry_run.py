from google.cloud import bigquery

def print_dry_run(client, query):
    dry_run_config = bigquery.QueryJobConfig(dry_run=True)
    test_job = client.query(query, dry_run_config)
    bytes = test_job.total_bytes_processed
    print(f'This query will use {format(bytes, ',')} bytes.')
