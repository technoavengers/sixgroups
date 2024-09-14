from minio import Minio
from minio.error import S3Error


'''
In this lab, you are required to create multiple bucket
sixgroups-marketing
sixgroups-finance
sixgroups-it
sixgroups-hr
'''


def main():

    #TODO: Provide your Access Key and Secret Access Key
    client = Minio(
        "127.0.0.1:9000",
        access_key="give_your_access_key_here",
        secret_key="give_your_secret_access_key_here",
        secure=False,  # Set to True if using HTTPS
    )

    #TODO: Change the bucket name as asked in lab
    bucket_names = ["bucket1", "bucket2", "bucket3"]

    for bucket_name in bucket_names:
        try:
             #TODO: write if else block to check whether bucket exist?
             # API to check for bucket existence - client.bucket_exists(bucket_name)
             #TODO : if bucket does not exist, make a new bucket
             # API to make a bucket - client.make_bucket(bucket_name)
             #TODO:  else print that bucket already exists
             print('')
        except S3Error as err:
            print(f"Error creating bucket '{bucket_name}': {err}")


if __name__ == "__main__":
    main()

