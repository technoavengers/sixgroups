from minio import Minio
from minio.error import S3Error  # Correct import for error handling
from minio.commonconfig import Tags



'''
In this lab, you are required to add tags
{"purpose": "infrastructure", "owner": "IT Dept"} 
to the sixgroups-it bucket.
'''


def main():
    try:
        #TODO: Provide your Access Key and Secret Access Key
        client = Minio(
            "127.0.0.1:9000",
            access_key="your access key",
            secret_key="your secret key",
            secure=False,  # Set to True if using HTTPS
        )

        tags = Tags()
        #TODO: Add your tags here
        #tags["key"] = "value"        

        #TODO: Use client.set_bucket_tags("bucket-name", tags) API to apply the tags
        #TODO: Use appropriate bucket name in above code
        print("Tags added to bucket.")


        #TODO: Use client.get_bucket_tags("bucket-name") API to retrieve the tags
        #TODO: Use appropriate bucket name in above code
        #TODO: Save the output of above code in variable name " retrieved_tags"
        for tag_key, tag_value in retrieved_tags.items():
            print(f"{tag_key}: {tag_value}")
    except S3Error as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()