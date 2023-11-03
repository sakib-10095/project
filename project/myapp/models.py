from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUser(AbstractUser):

    User=(

        (1,'admin'),
        (2,'teacher'),
        (3,'student'),
    )
    user_type = models.CharField(choices=User,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to="media/profile_pic")