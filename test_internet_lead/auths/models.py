from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(User):
    def save(self, *args, **kwargs):
            # do anything you need before saving
            super(CustomUser, self).save(*args, **kwargs)
            # do anything you need after saving

    def __str__(self):
        return self.user.username