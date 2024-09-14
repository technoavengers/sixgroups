from minio import Minio
from minio.commonconfig import REPLACE, CopySource
from minio.error import S3Error
from datetime import datetime, timezone
from minio.commonconfig import Tags

def create_bucket(client, bucket_name):
    try:
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")
        else:
            print(f"Bucket '{bucket_name}' already exists.")
    except S3Error as err:
        print(f"Error: {err}")

def copy_object(client, source_bucket, destination_bucket, source_object, destination_object, metadata):
    try:
        result = client.copy_object(
            destination_bucket,
            destination_object,
            CopySource(source_bucket, source_object),
            metadata=metadata,
            metadata_directive=REPLACE
        )
        print(f"File '{source_object}' copied successfully from '{source_bucket}' to '{destination_bucket}'.")
        print(f"Object Name: {result.object_name}, Version ID: {result.version_id}")
        return destination_bucket, destination_object
    except S3Error as e:
        print(f"Failed to copy '{source_object}': {e}")
        return None, None

def set_object_tags(client, bucket_name, object_name, tags):

    try:
        client.set_object_tags(bucket_name, object_name, tags)
        print(f"Tags {tags} added to object '{object_name}' in bucket '{bucket_name}'.")
    except S3Error as e:
        print(f"Failed to set tags for '{object_name}': {e}")

def main():
    client = Minio(
        "127.0.0.1:9000",
        access_key="H3M1SCNEt5m2hVqEfEz5",
        secret_key="JAkOAMNkpEsbBZyw50FNDxPRat9k4jC8dhPHlYFF",
        secure=False,  # Set to True if using HTTPS
    )

    source_bucket = "sixgroups-finance"
    destination_bucket = "sixgroups-finance-archive"
    source_object = "transaction_log_2023.csv"
    destination_object = "transaction_logs.csv"
    metadata = {"test_meta_key": "test_meta_value"}
    tags = Tags()
    tags["status"] = "archived"
    tags["type"] = "transaction"

    # Create destination bucket
    create_bucket(client, destination_bucket)
    
    # Copy file from source bucket to destination bucket
    destination_bucket_name, destination_object_name = copy_object(
        client,
        source_bucket,
        destination_bucket,
        source_object,
        destination_object,
        metadata
    )

    # Add tags to the copied object
    if destination_bucket_name and destination_object_name:
        set_object_tags(client, destination_bucket_name, destination_object_name, tags)

if __name__ == "__main__":
    main()
