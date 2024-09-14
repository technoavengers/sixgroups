from minio import Minio
from datetime import timedelta


policy = '''{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": ["s3:GetObject"],
            "Resource": ["arn:aws:s3:::logs-bucket/tmp/*"]
        }
    ]
}'''

# Initialize the MinIO client
minioClient = Minio(
     "127.0.0.1:9000",
      access_key="hgWVh2MUy0v7i2Hzq2NR",
      secret_key="hfmaMc57uRhEGy0d70XlPbqzeMdRnFyxmVSYMMdZ",
    secure=False
)

try:
    minioClient.set_bucket_policy("logs-bucket", policy)

except Exception as err:
    print(f"Error: {err}")