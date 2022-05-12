from messaging_app.models import Message
from rest_framework import status as http_status

class DeleteMessage:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.message_id = kwargs.get('message_id')

    def validate(self):
        if self.user_id is None:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "User Id is missing"})

        if type(self.user_id) != str:
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "User Type should be of string datatype"})

        if self.message_id and not self.message_id.isdigit():
            return (False, http_status.HTTP_400_BAD_REQUEST, {"status": 1, "message": "Message should be a digit"})

        return (True, http_status.HTTP_200_OK, {"status": 0, "message": "Data is valid"})

    def delete(self):
        sucess, status_code, response = self.validate()
        if not sucess:
            return sucess, status_code, response

        try:
            if self.message_id:
                self.message_id = int(self.message_id)
                if Message.objects.filter(id = self.message_id, user_id = self.user_id).exists():
                    Message.objects.filter(id = self.message_id, user_id = self.user_id).delete()
                else:
                    return (False, http_status.HTTP_404_NOT_FOUND, {"status": 1, "message": "Message with this message id does not exist"})
            else:
                if Message.objects.filter(user_id = self.user_id).exists():
                    Message.objects.filter(user_id = self.user_id).delete()
                else:
                    return (False, http_status.HTTP_404_NOT_FOUND, {"status": 1, "message": "No messages found for this user"})

            return (True, http_status.HTTP_200_OK, {"status": 0, "message": "Deleted successfully"})

        except Exception as e:
            return (False, http_status.HTTP_500_INTERNAL_SERVER_ERROR, {"status": 1, "message": str(e)})