from minio import Minio
from minio.error import S3Error

def delete_object(client, bucket_name, object_name):
    try:
        client.remove_object(bucket_name, object_name)
        print(f"File '{object_name}' deleted successfully.")
    except S3Error as e:
        print(f"Failed to delete '{object_name}': {e}")

def delete_multiple_files(client, bucket_name, object_names):
    for object_name in object_names:
        delete_object(client, bucket_name, object_name)

def main():
    client = Minio(
        "127.0.0.1:9000",
        access_key="H3M1SCNEt5m2hVqEfEz5",
        secret_key="JAkOAMNkpEsbBZyw50FNDxPRat9k4jC8dhPHlYFF",
        secure=False,  # Set to True if using HTTPS
    )

    bucket_name = "sixgroups-finance"
    
    # List of files to delete
    files_to_delete = [
        "transaction_log_2023.csv",
        "account_summary_2023.csv",
    ]

    delete_multiple_files(client, bucket_name, files_to_delete)

if __name__ == "__main__":
    main()
