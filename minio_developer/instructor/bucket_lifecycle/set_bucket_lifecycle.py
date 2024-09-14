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

# Create LifecycleConfig rules
config = LifecycleConfig(
    [
        Rule(
            ENABLED,
            rule_filter=Filter(prefix="logs/"),
            rule_id="rule1",
            transition=Transition(days=30, storage_class="S3_STANDARD"),
        ),
        Rule(
            ENABLED,
            rule_filter=Filter(prefix="tmp/"),
            rule_id="rule2",
            expiration=Expiration(days=365),
        ),
    ],
)


try:
    # Set the bucket lifecycle configuration
    minioClient.set_bucket_lifecycle("logs-bucket", config)
    print("Lifecycle policy applied successfully.")

except Exception as err:
    print(f"Error: {err}")
