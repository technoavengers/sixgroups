from datetime import datetime, timedelta

from minio import Minio
from minio.commonconfig import Tags

# Create a MinIO Client
client = Minio(
    "127.0.0.1:9000",
    access_key="fxPvE58ypZbEqft0jrDg",
    secret_key="ysXhOW5CLNsSXiizgh4QlG8ZVuiOkyKPrVmWRJdk",
    secure=False,  # Set to True if using HTTPS
)


def set_tags(client, bucket_name, object_name):
    try:
        tags = Tags.new_object_tags()
        tags["Project"] = "Project One"
        tags["User"] = "jsmith"
        client.set_object_tags(bucket_name, object_name, tags)
        print(f"Tags set for object '{object_name}' in bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Failed to set tags: {e}")

def main():
    bucket_name = "my-bucket-2"
    object_name = "movies.csv"

    # Ensure the bucket exists
    if not client.bucket_exists(bucket_name):
        print(f"Bucket '{bucket_name}' does not exist.")
        return

    # Ensure the object exists
    try:
        client.stat_object(bucket_name, object_name)
    except Exception as e:
        print(f"Object '{object_name}' not found in bucket '{bucket_name}'.")
        return

    set_tags(client, bucket_name, object_name)

if __name__ == "__main__":
    main()
