from django.contrib import admin

from .models import Link, UserPage


admin.site.register(UserPage)
admin.site.register(Link)