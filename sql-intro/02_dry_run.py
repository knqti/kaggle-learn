from credentials import login, bigquery

client = login()

# Get dry run info
query = """
    SELECT score, title
    FROM `bigquery-public-data.hacker_news.full`
    WHERE type = 'job'
"""

dry_run_config = bigquery.QueryJobConfig(dry_run=True)
test_job = client.query(query, dry_run_config)
print(f'This query will use {test_job.total_bytes_processed} bytes.')

# Safe config limit
# ONE_GB = 1000 * 1000 * 1000
# safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=ONE_GB)
# query_job = client.query(query, safe_config)
# scores = query_job.to_dataframe()
# avg_scores = scores.score.mean()
# print(avg_scores)