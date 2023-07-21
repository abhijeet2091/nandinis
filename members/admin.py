from django.contrib import admin
from .models import User

class User_Admin(admin.ModelAdmin):
    list_display=('email', 'mobile', 'first_name', 'last_name', 'address1',
                  'address2', 'address3', 'address4', 'address5', 'address6')

admin.site.register(User, User_Admin)
