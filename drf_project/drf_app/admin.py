from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)           #same as admin.site.register(Student, StudentAdmin)
class StudentAdmin(admin.ModelAdmin):     #to customize admin interface for student model
    list_display = ['id', 'name', 'roll_no', 'city']

