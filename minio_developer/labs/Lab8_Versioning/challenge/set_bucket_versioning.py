from minio import Minio
from minio.error import S3Error
from minio.commonconfig import ENABLED
from minio.versioningconfig import VersioningConfig


'''
Enable versioning in sixgroups-finance bucket
'''


def enable_versioning(client, bucket_name):
    try:
        #TODO: Use client.set_bucket_versioning(bucket_name, VersioningConfig(ENABLED))
        print(f"Versioning enabled for bucket '{bucket_name}'.")
    except S3Error as e:
        print(f"Failed to enable versioning for bucket '{bucket_name}': {e}")



def main():
    #TODO: Provide your access key & secret access key
    client = Minio(
        "127.0.0.1:9000",
        access_key="your access key",
        secret_key="your secret key",
        secure=False,
    )

    #TODO: Provide name of bucket where you want to set versioning
    bucket_name = "bucket_name"

    enable_versioning(client, bucket_name)


if __name__ == "__main__":
    main()
