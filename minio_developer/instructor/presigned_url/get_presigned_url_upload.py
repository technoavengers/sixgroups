from minio import Minio
from datetime import timedelta

# Initialize the MinIO client
minioClient = Minio(
     "127.0.0.1:9000",
      access_key="hgWVh2MUy0v7i2Hzq2NR",
      secret_key="hfmaMc57uRhEGy0d70XlPbqzeMdRnFyxmVSYMMdZ",
    secure=False
)

try:
    # Generate a presigned URL for downloading an object, valid for 1 day
    presigned_url = minioClient.get_presigned_url(
        method="PUT",
        bucket_name="logs-bucket",
        object_name="new-object.csv",
        expires=timedelta(days=1)
    )

    print("Presigned URL:", presigned_url)
except Exception as err:
    print(f"Error: {err}")