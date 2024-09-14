from minio import Minio



'''
Download a specific version of transaction.csv file from sixgroups-finance bucket
'''


client = Minio(
        "127.0.0.1:9000",
        access_key="your access key here",
        secret_key="your secret key here",
        secure=False,
)

client.fget_object(
    "bucket_name", "file_name", "transaction_versioned.csv",
    version_id="version id to download",)