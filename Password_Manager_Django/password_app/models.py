from django.db import models

# Create your models here.
class Password(models.Model):
    account_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    encrypted_password = models.CharField(max_length=200)
