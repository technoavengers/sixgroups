from minio import Minio
from minio.error import S3Error  # Correct import for error handling


def upload_file(client, bucket_name, file_path, object_name):
    # Upload a file
    try:
        result = client.fput_object(bucket_name, object_name, file_path)
        print(f"Created {result.object_name} object; etag: {result.etag}, version-id: {result.version_id}")
    except S3Error as e:
        print(f"Failed to upload '{file_path}': {e}")

def main():
    # Create a MinIO Client
    client = Minio(
        "127.0.0.1:9000",
        access_key="MNwaY53BmP7H47io5HTV",
        secret_key="XtLwnpporgBn38SDDLV87Kd7fhJqCUhUhxpcAuwn",
        secure=False,  # Set to True if using HTTPS
    )

    bucket_name = "sixgroups-finance"
    file_path = "labs/Lab7_Versioning/data/transaction_log_2023.csv" 
    object_name = "transactions.csv"

    upload_file(client=client, bucket_name=bucket_name, file_path=file_path, object_name=object_name)

if __name__ == "__main__":
    main()
