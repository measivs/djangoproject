from django.db import models
from users.models import User
# Create your models here.

class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.email}"