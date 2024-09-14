import os
from minio import Minio
from typing import List
import json

# Define the Part class to hold part number and ETag
class Part:
    def __init__(self, part_number: int, etag: str):
        self.part_number = part_number
        self.etag = etag

    def to_dict(self):
        return {
            'part_number': self.part_number,
            'etag': self.etag
        }

    @staticmethod
    def from_dict(part_dict):
        return Part(part_number=part_dict['part_number'], etag=part_dict['etag'])

def list_uploaded_parts(minioClient, bucket_name: str, object_name: str, upload_id: str) -> List[Part]:
    """
    Lists the parts that have already been uploaded and returns a list of Part objects.
    """
    uploaded_parts = []
    # List parts that have already been uploaded
    result = minioClient._list_parts(bucket_name, object_name, upload_id)
    parts = result.parts
    
    for part in parts:
        uploaded_parts.append(Part(part_number=part.part_number, etag=part.etag))
    
    return uploaded_parts


def upload_parts(minioClient, bucket_name: str, object_name: str, upload_id: str, file_path: str, part_size: int, uploaded_parts: List[Part]):
    """
    Upload parts, skipping those that have already been uploaded.
    """
    log_file = f"{object_name}_upload_log.json"  # To save uploaded part details
    with open(file_path, 'rb') as file:
        part_number = 1
        parts = uploaded_parts  # Start with already uploaded parts

        while True:
            data = file.read(part_size)  # Read a part of the file
            if not data:
                break  # Exit when no more data to read

            # Check if the part is already uploaded
            if any(p.part_number == part_number for p in uploaded_parts):
                print(f"Part {part_number} already uploaded, skipping...")
            else:
                # Upload each part using _upload_part method
                try:
                    etag = minioClient._upload_part(
                        bucket_name=bucket_name,
                        object_name=object_name,
                        data=data,
                        headers={"Content-Type": "text/csv"},
                        upload_id=upload_id,
                        part_number=part_number
                    )
                    part = Part(part_number=part_number, etag=etag)
                    parts.append(part)
                    print(f"Part {part_number} uploaded successfully with ETag: {etag}")
                except Exception as e:
                    print(f"Failed to upload part {part_number}: {e}")
                    abort_multipart_upload(minioClient, bucket_name, object_name, upload_id)
                    raise e

            part_number += 1

    return parts

def abort_multipart_upload(minioClient, bucket_name: str, object_name: str, upload_id: str):
    """
    Aborts the multipart upload session, removing all uploaded parts.
    """
    try:
        minioClient._abort_multipart_upload(bucket_name, object_name, upload_id)
        print(f"Multipart upload aborted for {object_name} with upload_id {upload_id}")
    except Exception as e:
        print(f"Failed to abort multipart upload: {e}")

if __name__ == "__main__":
    # Initialize the MinIO client
    minioClient = Minio(
        "127.0.0.1:9000",
        access_key="hgWVh2MUy0v7i2Hzq2NR",
        secret_key="hfmaMc57uRhEGy0d70XlPbqzeMdRnFyxmVSYMMdZ",
        secure=False
    )

    # Ask user for an existing upload ID or create a new one if not provided
    user_upload_id = input("Enter an existing upload ID (or press Enter to start a new upload): ").strip()


    # Define the bucket name, object name, and upload_id from the multipart upload process
    bucket_name = "my-bucket-2"
    object_name = "ratings.csv"
    file_path = "/home/training/sixgroups/minio_developer/instructor/data/ratings.csv"
    part_size = 5 * 1024 * 1024  # 5 MB parts
    log_file = f"{object_name}_upload_log.json"  # Log file to store uploaded part details

    headers = {
        "Content-Type": "text/csv"  # Specifies that the content being uploaded is a CSV file
    }
    uploaded_parts = []
    
    try:
        if user_upload_id:
            upload_id = user_upload_id
            print(f"Resuming multipart upload with upload ID: {upload_id}")
            # Load parts that have already been uploaded
            uploaded_parts = list_uploaded_parts(minioClient, bucket_name, object_name, upload_id)
        else:
            upload_id = minioClient._create_multipart_upload(bucket_name, object_name, headers)
            print(f"Upload id is {upload_id}")
        for parts in uploaded_parts:
            print(f"Already uploaded {parts}")
        parts = upload_parts(minioClient, bucket_name, object_name, upload_id, file_path, part_size, uploaded_parts)
        result = minioClient._complete_multipart_upload(bucket_name, object_name, upload_id, parts)
        print(f"Multipart upload completed successfully: Location={result.location}, ETag={result.etag}")
    except Exception as e:
        print(f"An error occurred during multipart upload: {e}")
        abort_multipart_upload(minioClient, bucket_name, object_name, upload_id)
        exit(1)  # Exit after aborting the upload
