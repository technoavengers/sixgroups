curl -X POST http://transform-service:5000/transform_uppercase \
     -H "Content-Type: application/json" \
     -d '{"url": "http://localhost:9000/sixgroups-finance/sample.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=i577ezvFkdWeUoTF15Ck%2F20240902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240902T184842Z&X-Amz-Expires=1000&X-Amz-SignedHeaders=host&X-Amz-Signature=b7056293a7ed2fc213fe2f0624543be549268b315d60a70ff46303b52ba5d66c"}'
