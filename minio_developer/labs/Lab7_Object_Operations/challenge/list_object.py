from minio import Minio
from minio.error import S3Error  # Correct import for error handling



'''
In this lab, you are required to list all the files under
sixgroup-finance bucket
'''

def list_objects(client, bucket_name):
    # List all objects in the bucket 
    try:
        #TODO: Use client.list_objects(bucket_name) API to list objects
        print("Objects in the bucket:")
        for obj in objects:
            print(obj.object_name)
    except S3Error as e:
        print(f"Failed to list objects in '{bucket_name}': {e}")

def main():
    #TODO: Provide your access key and secret key
    client = Minio(
        "127.0.0.1:9000",
        access_key="your access key",
        secret_key="your secret key",
        secure=False,  # Set to True if using HTTPS
    )
    #TODO: Provide appropriate bucket name 
    bucket_name = "bucket-name"
    
    list_objects(client=client, bucket_name=bucket_name)

if __name__ == "__main__":
    main()
