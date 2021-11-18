from django.contrib import admin
from .models import UserRequest, UserRequestResult
# Register your models here.


admin.site.register(UserRequest)
admin.site.register(UserRequestResult)