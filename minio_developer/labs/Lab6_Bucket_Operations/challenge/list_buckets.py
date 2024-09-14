from minio import Minio
from minio.error import S3Error  # Correct import for error handling


'''
In this lab, you are required to list all the buckets
'''

def main():
    #TODO: Provide your Access Key and Secret Access Key
    client = Minio(
            "127.0.0.1:9000",
            access_key="your_access_key_here",
            secret_key="your_secret_access_key_here",
            secure=False,  # Set to True if using HTTPS
        )
    try:
        #TODO: List all buckets and save it in bucket variable
        # API to list all buckets -- client.list_buckets
        print("Existing buckets:")
        for bucket in buckets:
            print(bucket.name)
    
    except S3Error as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

