import requests

# Presigned URL (from the first step)
presigned_url = "http://127.0.0.1:9000/logs-bucket/new-object.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=hgWVh2MUy0v7i2Hzq2NR%2F20240905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240905T111727Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b36dcec18f857325e1d0c7ebb2b0c3af3984cddc24b81f986b08a25cba56e7e8"

# Upload the file to the presigned URL
with open("/home/training/sixgroups/minio_developer/instructor/data/movies.csv", "rb") as file_data:
    response = requests.put(presigned_url, data=file_data)

if response.status_code == 200:
    print("Upload successful")
else:
    print(f"Upload failed: {response.status_code}")