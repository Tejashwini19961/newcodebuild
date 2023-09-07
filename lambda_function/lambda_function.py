import datetime
import socket
import os

# Determine the module path dynamically
module_path = os.path.dirname(os.path.abspath(__file__))

def lambda_handler(event, context):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = event['requestContext']['identity']['sourceIp']
    response = f"Current Time: {current_time}\nYour IP Address: {ip_address}\nModule Path: {module_path}"
    return {
        'statusCode': 200,
        'body': response
    }
