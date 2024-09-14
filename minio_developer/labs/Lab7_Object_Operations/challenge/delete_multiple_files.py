from minio import Minio
from minio.error import S3Error


'''
In this lab, you are required to delete transaction_log_2023.csv & account_summary_2023 from
sixgroup-finance bucket

'''


def delete_object(client, bucket_name, object_name):
    try:
        #TODO: Use client.remove_object(bucket_name, object_name) to remove object from bucket
        print(f"File '{object_name}' deleted successfully.")
    except S3Error as e:
        print(f"Failed to delete '{object_name}': {e}")

def delete_multiple_files(client, bucket_name, object_names):
    for object_name in object_names:
        delete_object(client, bucket_name, object_name)

def main():
    #TODO: Provide your access key and secret access key below
    client = Minio(
        "127.0.0.1:9000",
        access_key="your access key",
        secret_key="your secret access key",
        secure=False,  # Set to True if using HTTPS
    )

    #TODO: Name of bucket from where to delete
    bucket_name = "bucket name"
    
    #TODO: list of files to delete as provided in lab
    files_to_delete = [
        "file 1 name",
        "file 2 name",
    ]

    delete_multiple_files(client, bucket_name, files_to_delete)

if __name__ == "__main__":
    main()
