from minio import Minio

minio_client = Minio(
    "localhost:9000",
    access_key="i577ezvFkdWeUoTF15Ck",
    secret_key="XP2Jb609lvRdAGj8wskRX10G52RCbQxqt48Zt5RU",
    secure=False
)

headers = {
    'X-Amz-Server-Side-Encryption': 'aws:kms',
    'X-Amz-Server-Side-Encryption-Aws-Kms-Key-Id': 'minio-key'
}

with open("customers-new.csv", "rb") as file_data:
    minio_client.put_object(
        "sixgroups-finance",
        "customers-new.csv",
        file_data,
        length=-1,
        part_size=10*1024*1024,
        metadata=headers
    )
