from django.contrib import admin
from WebApp.models import Emp

# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'password']
admin.site.register(Emp, EmpAdmin)
