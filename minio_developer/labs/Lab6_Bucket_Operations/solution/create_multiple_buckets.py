from minio import Minio
from minio.error import S3Error

def main():
    # Create a Minio Client
    client = Minio(
        "127.0.0.1:9000",
        access_key="H3M1SCNEt5m2hVqEfEz5",
        secret_key="JAkOAMNkpEsbBZyw50FNDxPRat9k4jC8dhPHlYFF",
        secure=False,  # Set to True if using HTTPS
    )

    # List of bucket names to create
    # Change the bucket name as asked in lab
    bucket_names = ["sixgroups-marketing", "sixgroups-hr", "sixgroups-it","sixgroups-finance"]

    # Iterate over each bucket name and create the bucket
    for bucket_name in bucket_names:
        try:
            if not client.bucket_exists(bucket_name):
                client.make_bucket(bucket_name)
                print(f"Bucket '{bucket_name}' created successfully.")
            else:
                print(f"Bucket '{bucket_name}' already exists.")
        except S3Error as err:
            print(f"Error creating bucket '{bucket_name}': {err}")


if __name__ == "__main__":
    main()

