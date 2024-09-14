from minio import Minio
from minio.error import S3Error  # Correct import for error handling

def main():
    try:
        # Create a MinIO Client
        client = Minio(
            "127.0.0.1:9000",
            access_key="H3M1SCNEt5m2hVqEfEz5",
            secret_key="JAkOAMNkpEsbBZyw50FNDxPRat9k4jC8dhPHlYFF",
            secure=False,  # Set to True if using HTTPS
        )

        # List all buckets
        buckets = client.list_buckets()
        print("Existing buckets:")
        for bucket in buckets:
            print(bucket.name)
    
    except S3Error as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
