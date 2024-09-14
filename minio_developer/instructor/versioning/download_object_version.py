# Download data of an object of version-ID.
from minio import Minio

client = Minio(
        "127.0.0.1:9000",
        access_key="fxPvE58ypZbEqft0jrDg",
        secret_key="ysXhOW5CLNsSXiizgh4QlG8ZVuiOkyKPrVmWRJdk",
        secure=False,
)


client.fget_object(
    "my-bucket-2", "movies.csv", "movies_versioned.csv",
    version_id="5020f154-2d8c-4f25-858e-140254e74f8b",
)

