# utils/utils.py

from django.http import JsonResponse
from rest_framework.response import Response

def custom_response(data=None, message="Success", code=200):
    if code ==200:
        response = {
            "response": data,
            "status": {
                "message": message,
                "code": code
            }
        }
    else :
        response = {
            "status": {
                "message": message,
                "code": code
            }
        }

    return Response(response, status=code)
