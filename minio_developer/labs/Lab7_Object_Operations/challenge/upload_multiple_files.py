import os
from minio import Minio
from minio.error import S3Error

'''
In this lab, you are required to upload files
transaction_log_2023.csv & account_summary_2023.csv
located in labs/Lab6_Object_Operations/data
'''

def upload_file_with_metadata(client, bucket_name, file_path, object_name):
    try:
        #TODO: Create metadata for file metdata={"x":"y"}
        #TODO: Use client.fput_object(bucket_name,object_name,file_path,metadata) API to upload

        print(f"Created {result.object_name} object; etag: {result.etag}, version-id: {result.version_id}")
    except S3Error as e:
        print(f"Failed to upload '{file_path}': {e}")

def upload_multiple_files(client, bucket_name, directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            upload_file_with_metadata(client, bucket_name, file_path, filename)

def main():
    # TODO: Provide your access key & secret key here
    client = Minio(
        "127.0.0.1:9000",
        access_key="your access key",
        secret_key="your secret key",
        secure=False,
    )

    # TODO: Provide the name of the bucket where to upload
    bucket_name = "your-bucket-name"
    directory_path = "labs/Lab6_Object_Operations/data"  # Directory containing files to upload

    upload_multiple_files(client=client, bucket_name=bucket_name, directory_path=directory_path)

if __name__ == "__main__":
    main()
