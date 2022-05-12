from django.db import models

# Create your models here.
class Message(models.Model):
    user_id = models.CharField(max_length=16, default="")
    message_text = models.CharField(max_length=500, default="")
    is_sent = models.BooleanField(default=True)
    delivered_at = models.DateTimeField(blank = True)