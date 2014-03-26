from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserStatistics(User):
    class Meta:
        proxy=True
        ordering = ('id',) 