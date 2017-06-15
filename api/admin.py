from django.contrib import admin
from api.models import Student
from api.models import Company
from api.models import TrainingProgram
from api.models import StudentApplications
# Register your models here.

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(TrainingProgram)
admin.site.register(StudentApplications)
