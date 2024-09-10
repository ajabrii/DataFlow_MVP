def handler(request):
    return {
        "statusCode": 200,
        "body": '{"message": "Hello from Python Backend!"}',
        "headers": {
            "Content-Type": "application/json"
        }
    }

