from minio import Minio
from minio.error import S3Error

def main():
    try:
        # Create a MinIO Client
        client = Minio(
            "127.0.0.1:9000",
            access_key="H3M1SCNEt5m2hVqEfEz5",
            secret_key="JAkOAMNkpEsbBZyw50FNDxPRat9k4jC8dhPHlYFF",
            secure=False,  # Set to True if using HTTPS
        )
        
        # List of bucket names to delete
        bucket_names_to_delete = ["sixgroups-marketing", "sixgroups-hr"]
        
        # Iterate over each bucket name and delete the bucket
        for bucket_name in bucket_names_to_delete:
            try:
                client.remove_bucket(bucket_name)
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