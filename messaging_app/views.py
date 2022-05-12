from urllib import request, response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from messaging_app.wrapper.get_messages import GetMessage
from messaging_app.wrapper.add_message import AddMessage
from messaging_app.wrapper.delete_message import DeleteMessage

# Create your views here.

class Message(APIView):
    def post(self, request):
        data = request.data
        data.update( {"user_id": request.query_params.get('user_id')} )
        success, status_code, response = AddMessage(**data).add_record()
        return Response(response, status = status_code)

    def get(self, request):
        data = {
            "user_id" : request.query_params.get('user_id'),
            "limit" : request.query_params.get('limit'),
            "start" : request.query_params.get('start')
        }
        success, status_code, response = GetMessage(**data).get_response()
        return Response(response, status=status_code)

    def delete(self, request):
        data = {
            "user_id" : request.query_params.get('user_id'),
            "message_id": request.query_params.get('message_id')
        }
        success, status_code, response = DeleteMessage(**data).delete()
        return Response(response, status=status_code)