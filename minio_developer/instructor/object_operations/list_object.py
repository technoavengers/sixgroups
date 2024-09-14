from minio import Minio
from minio.error import S3Error  # Correct import for error handling

def list_objects(client, bucket_name):
    # List all objects in the bucket 
    try:
        objects = client.list_objects(bucket_name)
        print("Objects in the bucket:")
        for obj in objects:
            print(obj.object_name)
    except S3Error as e:
        print(f"Failed to list objects in '{bucket_name}': {e}")

def main():
    # Create a MinIO Client
    client = Minio(
        "127.0.0.1:9000",
        access_key="fxPvE58ypZbEqft0jrDg",
        secret_key="ysXhOW5CLNsSXiizgh4QlG8ZVuiOkyKPrVmWRJdk",
        secure=False,  # Set to True if using HTTPS
    )

    bucket_name = "my-bucket-2"
    
    list_objects(client=client, bucket_name=bucket_name)

if __name__ == "__main__":
    main()
