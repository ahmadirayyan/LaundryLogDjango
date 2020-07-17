from django.db import models
from datetime import datetime

# Create your models here.
class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191, null=True)
    email = models.CharField(max_length=191, null=True, unique=True)
    password = models.CharField(max_length=191, null=False)
    created_at = models.DateTimeField(default=datetime.utcnow)
    updated_at = models.DateTimeField(default=datetime.utcnow)