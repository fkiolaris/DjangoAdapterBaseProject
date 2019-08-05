from django.shortcuts import render

# Create your views here.
import requests
import json
from rest_framework.views import APIView
from utils.requests import List, Detail
from utils.schemas import Apps
from rest_framework import status
from manageAppsAPIAdapter.settings import APPS_TYPE, CMS_HEADER
from rest_framework.response import Response

# Create your views here.
class AppsAPIList(APIView):
    def get(self, request, format=None):
        return List.get(APPS_TYPE).toResponse()

    def post(self, request, format=None):
        payload = None
        try:
            payload = request.body
            response = Apps.addApp(json.loads(payload.decode("utf-8")))
            if not response == True:
                return Response({
                            "status": "Error",
                            "message": str(response),
                            "data": {}
                            },
                            status = status.HTTP_400_BAD_REQUEST,
                            headers=CMS_HEADER)
        except:
            return Response({
                            "status": "Error",
                            "message": "Given Data is not a valid JSON",
                            "data": {}
                            },
                            status = status.HTTP_400_BAD_REQUEST,
                            headers=CMS_HEADER)

        return List.post(APPS_TYPE, request.body).toResponse()

class AppsAPIDetail(APIView):
    def get(self, request, id, format=None):
        return Detail.get(APPS_TYPE, id).toResponse()

    def delete(self, request, id, format=None):
        return Detail.delete(APPS_TYPE, id).toResponse()
        
    def patch(self, request, id, format=None):
        payload = None
        try:
            payload = request.body
            response = Apps.editApp(json.loads(payload.decode("utf-8")))
            if not response == True:
                return Response({
                            "status": "Error",
                            "message": str(response),
                            "data": {}
                            },
                            status = status.HTTP_400_BAD_REQUEST,
                            headers=CMS_HEADER)            
        except:
            return Response({
                            "status": "Error",
                            "message": "Given Data is not a valid JSON",
                            "data": {}
                            },
                            status = status.HTTP_400_BAD_REQUEST,
                            headers=CMS_HEADER)        
        return Detail.patch(APPS_TYPE, id, payload).toResponse()