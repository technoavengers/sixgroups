from minio import Minio
from minio.error import S3Error




'''
In this lab, you are required to delete multiple bucket
sixgroups-marketing
sixgroups-hr
'''


def main():
    try:
        #TODO: Provide your Access Key and Secret Access Key
        client = Minio(
            "127.0.0.1:9000",
            access_key="your access key",
            secret_key="your secret access key",
            secure=False,  # Set to True if using HTTPS
        )
        
        #TODO: List of bucket names to delete as given in lab
        bucket_names_to_delete = ["bucket1", "bucket2"]
        
        for bucket_name in bucket_names_to_delete:
            try:
                #TODO: delete the bucket usinf client.remove_bucket(bucket_name) API
                print(f"Bucket '{bucket_name}' deleted successfully.")
            except S3Error as e:
                print(f"Error deleting bucket '{bucket_name}': {e}")
            except Exception as e:
                print(f"An error occurred while deleting '{bucket_name}': {e}")
    
    except S3Error as e:
        print(f"MinIO error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()