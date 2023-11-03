from django.contrib import admin
from myapp.models import customUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class userModel(UserAdmin):
    list_display=['username','user_type']


admin.site.register(customUser,userModel)

