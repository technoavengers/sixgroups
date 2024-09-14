from minio import Minio
from minio.error import S3Error  # Correct import for error handling

def main():
    try:
        # Create a MinIO Client
        client = Minio(
            "127.0.0.1:9000",
            access_key="fxPvE58ypZbEqft0jrDg",
            secret_key="ysXhOW5CLNsSXiizgh4QlG8ZVuiOkyKPrVmWRJdk",
            secure=False,  # Set to True if using HTTPS
        )
        
        bucket_name_to_delete = "my-bucket-python"
        
        # Delete a bucket
        client.remove_bucket(bucket_name_to_delete)
        print(f"Bucket '{bucket_name_to_delete}' deleted successfully.")
    
    except S3Error as e:
        print(f"MinIO error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
