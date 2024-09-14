from minio import Minio
from minio.error import S3Error  # Correct import for error handling

def create_bucket(client, bucket_name):
    # Create a bucket
    try:
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")
        else:
            print(f"Bucket '{bucket_name}' already exists.")
    except S3Error as err:
        print(f"Error: {err}")

def upload_file(client, bucket_name, file_path, object_name):
    # Upload a file
    try:
        client.fput_object(bucket_name, object_name, file_path)
        print(f"File '{file_path}' uploaded successfully as '{object_name}'.")
    except S3Error as e:
        print(f"Failed to upload '{file_path}': {e}")

def main():
    # Create a MinIO Client
    client = Minio(
        "127.0.0.1:9000",
        access_key="fxPvE58ypZbEqft0jrDg",
        secret_key="ysXhOW5CLNsSXiizgh4QlG8ZVuiOkyKPrVmWRJdk",
        secure=False,  # Set to True if using HTTPS
    )

    bucket_name = "my-bucket-2"
    file_path = "data/movies.csv" 
    object_name = "movies.csv"

    create_bucket(client=client, bucket_name=bucket_name)
    upload_file(client=client, bucket_name=bucket_name, file_path=file_path, object_name=object_name)

if __name__ == "__main__":
    main()
