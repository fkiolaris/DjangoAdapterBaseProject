
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manageAppsAPIAdapter.settings import MEDIA_OBJECT_URL, CMS_HEADER

class List:
    @staticmethod
    def get(mModel : str):
        try:
            requestHeaders = CMS_HEADER
            response = requests.get(MEDIA_OBJECT_URL + mModel, headers = requestHeaders)
            payload = json.loads(response.text)
            return ReqResponse(payload, status.HTTP_200_OK, CMS_HEADER)
        except Exception as ex:
            return ReqResponse(None, status.HTTP_400_BAD_REQUEST, CMS_HEADER,  str(ex), "Error")    

    @staticmethod
    def post(mModel : str, payload):
        try:
            requestHeaders = CMS_HEADER
            print("URL:" + MEDIA_OBJECT_URL + mModel)
            response = requests.post(MEDIA_OBJECT_URL + mModel, data=payload, headers = requestHeaders)
            payload = json.loads(response.text)
            return ReqResponse(payload, status.HTTP_200_OK, CMS_HEADER)
        except Exception as ex:
            return ReqResponse(None, status.HTTP_400_BAD_REQUEST, CMS_HEADER,  str(ex), "Error")   

class Detail:
    @staticmethod
    def get(mModel : str, id : str):
        try:
            requestHeaders = CMS_HEADER
            print(MEDIA_OBJECT_URL + mModel + "/" + id)
            response = requests.get(MEDIA_OBJECT_URL + mModel + "/" + id, headers = requestHeaders)
            payload = json.loads(response.text)
            return ReqResponse(payload, status.HTTP_200_OK, CMS_HEADER)
        except Exception as ex:
            return ReqResponse(None, status.HTTP_400_BAD_REQUEST, CMS_HEADER,  str(ex), "Error")

    @staticmethod
    def patch(mModel : str, id : str, payload):
        try:
            requestHeaders = CMS_HEADER
            response = requests.patch(MEDIA_OBJECT_URL + mModel + "/" + id, data=payload, headers = requestHeaders)
            payload = json.loads(response.text)
            return ReqResponse(payload, status.HTTP_200_OK, CMS_HEADER)
        except Exception as ex:
            return ReqResponse(None, status.HTTP_400_BAD_REQUEST, CMS_HEADER,  str(ex), "Error")  

    @staticmethod
    def delete(mModel : str, id : str):
        try:
            requestHeaders = CMS_HEADER
            response = requests.delete(MEDIA_OBJECT_URL + mModel + "/" + id, headers = requestHeaders)
            payload = json.loads(response.text)
            return ReqResponse(payload, status.HTTP_200_OK, CMS_HEADER)
        except Exception as ex:
            return ReqResponse(None, status.HTTP_400_BAD_REQUEST, CMS_HEADER,  str(ex), "Error")     

class ReqResponse:
    def __init__(self, data : json, statusCode, headers, message = None, status = None):
        if message == None and status == None:
            self._instance2(statusCode, data, headers)
        else:
            self._instance1(data, statusCode, headers, message, status)

    def _instance2(self, statusCode, data, headers):
        self.response = data
        self.statusCode = statusCode
        self.headers = headers
    
    def _instance1(self, data : json, statusCode, headers, message, status):
        self.response = {}
        self.statusCode = statusCode
        self.headers = headers

        if not status == None:
            self.response["status"] = status
        if not data == None:
            self.response["data"] = data
        if not message == None:
            self.response["message"] = message
        print(str(self.response))

    def toResponse(self):
        return Response(
                    self.response,
                    status = self.statusCode,
                    headers = self.headers
                )

    def toDictionary(self):
        mdict = {
            "response" : self.response,
            "statusCode" : self.statusCode
        }
        return mdict

def requestResponse(data : json, statusCode, headers, message, status):
    response = {}
    if data == None:
        response["data"] = data
    if headers == None:
        response["headers"] = headers
    if message == None:
        response["message"] = message
    if status == None:
        response["status"] = status
    if statusCode == None:
        response["statusCode"] = statusCode
    return response