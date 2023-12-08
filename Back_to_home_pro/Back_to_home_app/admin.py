from django.contrib import admin
from .models import userclass,admin_table
# Register your models here.
admin.site.register(userclass)
admin.site.register(admin_table)