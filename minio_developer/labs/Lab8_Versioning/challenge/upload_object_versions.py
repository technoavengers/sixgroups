from minio import Minio
from minio.error import S3Error  # Correct import for error handling


'''
Upload labs/Lab8_Versioning/data/transaction_log_2023.csv file mmultiple time as transactions.csv 
in sixgroups-finance bucket
'''



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
        access_key="your access key",
        secret_key="your secret key",
        secure=False,  # Set to True if using HTTPS
    )

    bucket_name = "your bucket name"
    file_path = "location of your file to be uploaded" 
    object_name = "file name to appear in bucket"

    upload_file(client=client, bucket_name=bucket_name, file_path=file_path, object_name=object_name)

if __name__ == "__main__":
    main()