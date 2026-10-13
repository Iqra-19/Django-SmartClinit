from django.contrib import admin
from .models import Doctor, Department, DoctorAvailability

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(DoctorAvailability)
