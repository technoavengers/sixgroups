from minio import Minio
from minio.commonconfig import GOVERNANCE
from minio.retention import Retention
from datetime import datetime, timedelta

# Initialize the MinIO client
minioClient = Minio(
    "127.0.0.1:9000",
    access_key="hgWVh2MUy0v7i2Hzq2NR",
    secret_key="hfmaMc57uRhEGy0d70XlPbqzeMdRnFyxmVSYMMdZ",
    secure=False
)

try:

    # Apply object lock configuration to the bucket
    config = Retention(GOVERNANCE, datetime.utcnow() - timedelta(days=10))
    minioClient.set_object_retention("new-locked-bucket", "ps.png", config)

except Exception as err:
    print(f"Error: {err}")

