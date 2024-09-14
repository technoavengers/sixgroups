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
    policy = minioClient.get_bucket_policy("logs-bucket")
    print(policy)

except Exception as err:
    print(f"Error: {err}")