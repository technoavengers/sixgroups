from minio import Minio
from minio.error import S3Error  # Correct import for error handling
from minio.commonconfig import Tags

def main():
    try:
        # Create a MinIO Client
        client = Minio(
            "127.0.0.1:9000",
            access_key="H3M1SCNEt5m2hVqEfEz5",
            secret_key="JAkOAMNkpEsbBZyw50FNDxPRat9k4jC8dhPHlYFF",
            secure=False,  # Set to True if using HTTPS
        )

       # Define the tags
        tags = Tags()
        tags["purpose"] = "infrastructure"
        tags["owner"] = "IT Dept"


        # Apply tags to the bucket
        client.set_bucket_tags("sixgroups-it", tags)
        print("Tags added to 'sixgroups-it' bucket.")

        # Retrieve and display the tags
        retrieved_tags = client.get_bucket_tags("sixgroups-it")
        for tag_key, tag_value in retrieved_tags.items():
            print(f"{tag_key}: {tag_value}")
    
    except S3Error as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
