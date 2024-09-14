from minio import Minio
from minio.error import S3Error  # Correct import for error handling

def download_object(client, bucket_name, object_name):
    download_path = "downloaded-file.txt"
    # Download a file
    try:
        client.fget_object(bucket_name, object_name, download_path)
        print(f"File '{object_name}' downloaded successfully to '{download_path}'.")
    except S3Error as e:
        print(f"Failed to download '{object_name}': {e}")

def main():
    # Create a MinIO Client
    client = Minio(
        "127.0.0.1:9000",
        access_key="fxPvE58ypZbEqft0jrDg",
        secret_key="ysXhOW5CLNsSXiizgh4QlG8ZVuiOkyKPrVmWRJdk",
        secure=False,  # Set to True if using HTTPS
    )

    bucket_name = "my-bucket-2"
    object_name = "movies.csv"
    
    download_object(client, bucket_name, object_name)

if __name__ == "__main__":
    main()
