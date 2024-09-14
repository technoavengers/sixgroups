from minio import Minio
from minio.error import S3Error



'''
In this lab, you are required to download transaction_log_2023.csv & account_summary_2023 from
sixgroup-finance bucket
'''


def download_object(client, bucket_name, object_name, download_path):
    try:
        #TODO: USE client.fget_object(bucket_name, object_name, download_path) API to download
        print(f"File '{object_name}' downloaded successfully to '{download_path}'.")
    except S3Error as e:
        print(f"Failed to download '{object_name}': {e}")

def main():
    #TODO: Use your access key and secret access key
    client = Minio(
        "127.0.0.1:9000",
        access_key="your access key",
        secret_key="your secret key",
        secure=False,  # Set to True if using HTTPS
    )

    bucket_name = "sixgroups-finance"
    
    #TODO Define the files to download and their local paths
    files_to_download = {
        "file_name 1": "downloaded_transactions_logs.csv",
        "file_name 2": "downloaded_accounts_summary.csv"
    }

    for object_name, download_path in files_to_download.items():
        download_object(client, bucket_name, object_name, download_path)

if __name__ == "__main__":
    main()
