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
    bucket_name ="new-governance-bucket"
    if not minioClient.bucket_exists(bucket_name):
            minioClient.make_bucket(bucket_name,object_lock=True)
            print(f"Bucket '{bucket_name}' created successfully.")

    # Set up object lock configuration for the bucket (Governance mode, 15 days)
    config = ObjectLockConfig(GOVERNANCE, 15, DAYS)

    # Apply object lock configuration to the bucket
    minioClient.set_object_lock_config("new-governance-bucket", config)
    print("Object lock configuration set successfully.")

except Exception as err:
    print(f"Error: {err}")

