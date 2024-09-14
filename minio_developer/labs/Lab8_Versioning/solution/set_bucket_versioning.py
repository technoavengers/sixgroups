from minio import Minio
from minio.error import S3Error
from minio.commonconfig import ENABLED
from minio.versioningconfig import VersioningConfig

def enable_versioning(client, bucket_name):
    try:
        client.set_bucket_versioning(bucket_name, VersioningConfig(ENABLED))
        print(f"Versioning enabled for bucket '{bucket_name}'.")
    except S3Error as e:
        print(f"Failed to enable versioning for bucket '{bucket_name}': {e}")



def main():
    client = Minio(
        "127.0.0.1:9000",
        access_key="H3M1SCNEt5m2hVqEfEz5",
        secret_key="JAkOAMNkpEsbBZyw50FNDxPRat9k4jC8dhPHlYFF",
        secure=False,
    )

    bucket_name = "sixgroups-finance"

    enable_versioning(client, bucket_name)


if __name__ == "__main__":
    main()
