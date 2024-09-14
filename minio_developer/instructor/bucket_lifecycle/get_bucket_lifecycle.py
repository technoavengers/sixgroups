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
    lifecycle = minioClient.get_bucket_lifecycle("logs-bucket")
     # Iterate over each rule in the lifecycle configuration
    for rule in lifecycle.rules:
        print(f"Rule ID: {rule.rule_id}")
        print(f"Status: {rule.status}")
        
        # Print expiration details if they exist
        if rule.expiration:
            print(f"Expiration: {rule.expiration.days} days")
        
        # Print transition details if they exist
        if rule.transition:
            print(f"Transition after: {rule.transition.days} days")
            print(f"Transition to storage class: {rule.transition.storage_class}")
        
        # Print filter details if they exist
        if rule.rule_filter:
            print(f"Filter Prefix: {rule.rule_filter.prefix}")

except Exception as err:
    print(f"Error: {err}")
