from minio import Minio
from minio.lifecycleconfig import LifecycleConfig, Rule, Expiration, Transition
from minio.commonconfig import ENABLED, Filter

# Initialize the MinIO client
minioClient = Minio(
    "127.0.0.1:9000",
    access_key="hgWVh2MUy0v7i2Hzq2NR",
    secret_key="hfmaMc57uRhEGy0d70XlPbqzeMdRnFyxmVSYMMdZ",
    secure=False
)

try:
    # get the bucket lifecycle configuration
    lifecycle = minioClient.delete_bucket_lifecycle("logs-bucket")


except Exception as err:
    print(f"Error: {err}")
