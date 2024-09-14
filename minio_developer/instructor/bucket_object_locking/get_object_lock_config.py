from minio import Minio
from minio.commonconfig import GOVERNANCE
from minio.objectlockconfig import DAYS, ObjectLockConfig

# Initialize the MinIO client
minioClient = Minio(
    "127.0.0.1:9000",
    access_key="hgWVh2MUy0v7i2Hzq2NR",
    secret_key="hfmaMc57uRhEGy0d70XlPbqzeMdRnFyxmVSYMMdZ",
    secure=False
)

try:


    # get object lock configuration 
    config = minioClient.get_object_lock_config("new-compliance-bucket")
    print(f"mode: {config._mode} duration: {config._duration}")


except Exception as err:
    print(f"Error: {err}")

