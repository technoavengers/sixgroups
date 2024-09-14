from minio import Minio
from minio.error import S3Error  # Correct import for error handling
from minio.commonconfig import ComposeSource

def delete_object(client, bucket_name, object_name):
    # Delete a file
    try:
        client.remove_object(bucket_name, object_name)
        print(f"File '{object_name}' deleted successfully.")
    except S3Error as e:
        print(f"Failed to delete '{object_name}': {e}")

def main():
    # Create a MinIO Client
    client = Minio(
        "127.0.0.1:9000",
        access_key="hgWVh2MUy0v7i2Hzq2NR",
        secret_key="hfmaMc57uRhEGy0d70XlPbqzeMdRnFyxmVSYMMdZ",
        secure=False,  # Set to True if using HTTPS
    )

    try:
        # Define the source objects from different buckets
        sources = [
            ComposeSource("sixgroups-admin", "tags.csv"),
            ComposeSource("sixgroups-compliance", "customer_file.csv")
        ]

        # Compose objects from different buckets into one
        result = client.compose_object("sixgroups-compliance", "customer_movies.csv", sources)
        print("Object composed successfully with ETag:", result.etag)
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()