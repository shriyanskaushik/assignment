from messaging_app.models import Message
from rest_framework import status as http_status

class GetMessage:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.limit = kwargs.get('limit')
        self.start = kwargs.get('start')

    def validate(self):
        if self.user_id is None:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "User Id is missing"})

        if type(self.user_id) != str:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "User Type should be of string datatype"})

        return (True, http_status.HTTP_200_OK, {"status": 0, "message": "Data is valid"})

    def get_response(self):
        sucess, status_code, response = self.validate()
        if not sucess:
            return sucess, status_code, response

        try:
            self.limit = int(self.limit) if self.limit and self.limit.isdigit() else 10
            self.start = int(self.start) if self.start and self.start.isdigit() else 1
            messages = Message.objects.filter(
                user_id = self.user_id,
                id__gte = self.start
            ).order_by('-id')[:self.limit]

            response = []
            for msg in messages:
                msg_data = {
                    "message_id": msg.id,
                    "message_text": msg.message_text,
                    "is_sent": msg.is_sent,
                    "delivered_at": msg.delivered_at
                }
                response.append(msg_data)

            return (True, http_status.HTTP_200_OK, {"status": 0, "message": "Success", "data": response})
        except Exception as e:
            return (False, http_status.HTTP_500_INTERNAL_SERVER_ERROR, {"status": 1, "message": str(e)})