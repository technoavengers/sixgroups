from minio import Minio
from minio.error import S3Error

def download_object(client, bucket_name, object_name, download_path):
    try:
        client.fget_object(bucket_name, object_name, download_path)
        print(f"File '{object_name}' downloaded successfully to '{download_path}'.")
    except S3Error as e:
        print(f"Failed to download '{object_name}': {e}")

def main():
    client = Minio(
        "127.0.0.1:9000",
        access_key="H3M1SCNEt5m2hVqEfEz5",
        secret_key="JAkOAMNkpEsbBZyw50FNDxPRat9k4jC8dhPHlYFF",
        secure=False,  # Set to True if using HTTPS
    )

    bucket_name = "sixgroups-finance"
    
    # Define the files to download and their local paths
    files_to_download = {
        "transaction_log_2023.csv": "downloaded_transactions_logs.csv",
        "account_summary_2023.csv": "downloaded_accounts_summary.csv"
    }

    for object_name, download_path in files_to_download.items():
        download_object(client, bucket_name, object_name, download_path)

if __name__ == "__main__":
    main()
