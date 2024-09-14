import requests
from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/transform_uppercase', methods=['POST'])
def transform_uppercase():
    data = request.json
    object_url = data.get("url")
    output_route = data.get("x-amz-request-route")
    output_token = data.get("x-amz-request-token")
    
    # Fetch the object using the presigned URL
    response = requests.get(object_url)
    original_content = response.text
    
    # Transform: Convert to uppercase
    transformed_content = original_content.upper()

    # Create response with required headers
    response = Response(transformed_content)
    response.headers['x-amz-request-route'] = output_route
    response.headers['x-amz-request-token'] = output_token
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
