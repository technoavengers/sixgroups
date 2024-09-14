from minio import Minio

client = Minio(
        "127.0.0.1:9000",
        access_key="MNwaY53BmP7H47io5HTV",
        secret_key="XtLwnpporgBn38SDDLV87Kd7fhJqCUhUhxpcAuwn",
        secure=False,
)

client.fget_object(
    "sixgroups-finance", "transactions.csv", "transaction_versioned.csv",
    version_id="29c88049-64c6-4a23-b9e6-a71de77fbb5e",
)
