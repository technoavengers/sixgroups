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

    if minioClient.is_object_legal_hold_enabled("new-locked-bucket", "logs_ps.png"):
        print("legal hold is enabled")
    else:
        print("legal hold is not enabled")

except Exception as err:
    print(f"Error: {err}")

