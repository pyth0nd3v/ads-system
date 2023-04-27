from django.contrib import admin

# Register your models here.
from .models import Location, Ad

# Register your models here.
admin.site.register(Location)
admin.site.register(Ad)