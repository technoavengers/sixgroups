import os
from minio import Minio
from minio.error import S3Error


def upload_file_with_metadata(client, bucket_name, file_path, object_name):
    try:
        metadata = {"department": "finance"}
        result = client.fput_object(bucket_name, object_name, file_path, metadata=metadata)
        print(f"Created {result.object_name} object; etag: {result.etag}, version-id: {result.version_id}")
    except S3Error as e:
        print(f"Failed to upload '{file_path}': {e}")

def upload_multiple_files(client, bucket_name, directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            upload_file_with_metadata(client, bucket_name, file_path, filename)

def main():
    client = Minio(
        "127.0.0.1:9000",
        access_key="H3M1SCNEt5m2hVqEfEz5",
        secret_key="JAkOAMNkpEsbBZyw50FNDxPRat9k4jC8dhPHlYFF",
        secure=False,
    )

    bucket_name = "sixgroups-finance"
    directory_path = "labs/Lab6_Object_Operations/data"  # Directory containing files to upload

    upload_multiple_files(client=client, bucket_name=bucket_name, directory_path=directory_path)

if __name__ == "__main__":
    main()
