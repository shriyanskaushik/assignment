from datetime import datetime
from messaging_app.models import Message
from rest_framework import status as http_status

class AddMessage:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.timestamp = kwargs.get('timestamp')
        self.message = kwargs.get('message')
        self.is_sent = kwargs.get('isSent')

    def validate(self):
        if self.user_id is None:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "User Id is missing"})

        if self.timestamp is None:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "Timestamp is missing"})

        if self.message is None:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "Message is missing"})

        if self.is_sent is None:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "isSent is missing"})

        if type(self.user_id) != str:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "User Type should be of string datatype"})

        if type(self.message) != str:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "Message should be of string datatype"})

        if type(self.timestamp) != int:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "User Type should be of long integer datatype"})

        if type(self.is_sent) != bool:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "isSent should be of boolean datatype"})

        if len(self.user_id) == 0:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "User Id should not be an empty string"})

        if len(self.user_id) >= 16:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "User Id should be of length less than 16"})

        if not self.user_id.isalnum():
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "User Id should be alphanumeric"})

        return (True, http_status.HTTP_200_OK, {"status": 0, "message": "Data is valid"})

    def add_record(self):
        success, status_code, response = self.validate()
        if not success:
            return success, status_code, response

        try:
            date_time = datetime.fromtimestamp(self.timestamp)
            msg = Message(
                user_id = self.user_id,
                message_text = self.message,
                is_sent = self.is_sent,
                delivered_at = date_time
            )

            msg.save()
            message_id = msg.id

            response = {
                "message_id": message_id,
                "message_text": msg.message_text,
                "is_sent": msg.is_sent,
                "delivered_at": msg.delivered_at
            }

            return (True, http_status.HTTP_200_OK, {"status": 0, "message": "Success", "data": response})
        except Exception as e:
            return (False, http_status.HTTP_500_INTERNAL_SERVER_ERROR, {"status": 1, "message": str(e)})