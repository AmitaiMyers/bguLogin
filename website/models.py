from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    idNumber = models.CharField(max_length=50)

