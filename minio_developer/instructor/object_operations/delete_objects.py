from minio import Minio
from minio.deleteobjects import DeleteObject
from minio.error import S3Error

# Initialize the MinIO client
client = Minio(
        "127.0.0.1:9000",
        access_key="fxPvE58ypZbEqft0jrDg",
        secret_key="ysXhOW5CLNsSXiizgh4QlG8ZVuiOkyKPrVmWRJdk",
        secure=False,  # Set to True if using HTTPS
)

def delete_objects(client, bucket_name, object_names):
    # Delete a list of objects
    try:
        delete_objects_list = [DeleteObject(object_name) for object_name in object_names]
        errors = client.remove_objects(bucket_name, delete_objects_list)
        print(f"objects deleted")
        for error in errors:
            print(f"Error occurred when deleting object: {error}")
    except S3Error as e:
        print(f"Failed to delete objects: {e}")

def main():
    bucket_name = "my-bucket-2"
    object_names = ["movies.csv", "movies-new.csv"]

    delete_objects(client=client, bucket_name=bucket_name, object_names=object_names)

if __name__ == "__main__":
    main()
