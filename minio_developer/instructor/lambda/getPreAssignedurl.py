from minio import Minio
from datetime import timedelta
import requests

# Initialize MinIO client
minio_client = Minio(
    "localhost:9000",
    access_key="i577ezvFkdWeUoTF15Ck",
    secret_key="XP2Jb609lvRdAGj8wskRX10G52RCbQxqt48Zt5RU",
    secure=False
)

# Generate presigned URL for downloading
presigned_url = minio_client.get_presigned_url(
    "GET",
    bucket_name="sixgroups-finance",
    object_name="sample.txt",
    expires=timedelta(minutes=10)  # URL expires in 10 minutes
)

# Print the generated presigned URL
print("Generated Presigned URL:", presigned_url)

# URL of your Flask handler
handler_url = "http://transform-service:5000/transform_uppercase"

# x-amz-request-route and x-amz-request-token values (replace with actual values)
output_route = "<outputRoute>"
output_token = "<outputToken>"

# JSON payload to send to the handler
payload = {
    "url": presigned_url,
    "x-amz-request-route": output_route,
    "x-amz-request-token": output_token
}

# Sending POST request to the handler
response = requests.post(handler_url, json=payload)

# Print the transformed content and headers
print("Response Content:", response.text)
print("Response Headers:", response.headers)

