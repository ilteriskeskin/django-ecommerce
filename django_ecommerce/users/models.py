from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=12)
    slug = models.SlugField()
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.username
