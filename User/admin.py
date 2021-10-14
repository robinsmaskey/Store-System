from django.contrib import admin

# Register your models here.
from User.models import PortalUser

admin.site.register(PortalUser)
