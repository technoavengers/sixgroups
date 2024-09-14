
from minio import Minio
from minio.commonconfig import REPLACE, CopySource
from minio.error import S3Error
from datetime import datetime, timezone
from minio.commonconfig import Tags

'''
In this lab, you are required to create a new bucket sixgroups-finance-archive
and then copy transaction_log_2023.csv from ssixgroups-finance tosixgroups-finance-archive

'''

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
        #TODO: Make a note how copy object is called
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
        #TODO: USE client.set_object_tags(bucket_name, object_name, tags) API to apply tags   
        print(f"Tags {tags} added to object '{object_name}' in bucket '{bucket_name}'.")
    except S3Error as e:
        print(f"Failed to set tags for '{object_name}': {e}")

def main():
    #TODO: Provide your access key & Secret key
    client = Minio(
        "127.0.0.1:9000",
        access_key="your access key",
        secret_key="your secret key",
        secure=False,  # Set to True if using HTTPS
    )

    #TODO: Provide source bucket name
    source_bucket = "source bucket name"

    #TODO: Provide destination bucket name
    destination_bucket = "destination bucket name"

    #TODO: Source file name to copy
    source_object = "transaction_log_2023.csv"

    #TODO: Destination file name after copy
    destination_object = "transaction_logs.csv"

    #TODO: Define metadata, for example metadata = {"x": "y"}

    tags = Tags()
    #TODO: Define tags, for example tags["status"] = "archived"
    tag["tag_name 1"]="tag_value"
    tag["tag_name 2"]="tag_value"

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

