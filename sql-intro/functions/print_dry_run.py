from google.cloud import bigquery

def b_to_gb(bytes):
    gb = format(bytes / (1023 ** 3), '.2f')
    return gb

def print_dry_run(client, query):
    dry_run_config = bigquery.QueryJobConfig(dry_run=True)
    test_job = client.query(query, dry_run_config)
    bytes = test_job.total_bytes_processed
    gb_size = b_to_gb(bytes)
    print(f'This query will use {format(bytes, ',')} bytes ({gb_size} GB).')
