from rest_framework import serializers
from api.models import Student,Company,TrainingProgram
from api.models import StudentApplications
from api.models import login_db
from django.contrib.auth.models import User

class SignUpSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id',
				  'username',
				  'password',
				  'email',
				  'first_name',
				  'last_name',
				)

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('id',
				  'first_name',
				  'last_name',
				  'gender',
				  'email',
				  'college',
				  'city',
				  'state',
				  'graduation_year',
				  'mobile',
				  'telephone'
				)

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ('id',
				  'company_name',
				  'address1',
				  'address2',
				  'city',
				  'state',
				  'pin',
				  'mobile',
				  'telephone',
				  'description',
				  'website',
				  'email',
				  'password'
				)

class TrainingProgramSerializer(serializers.ModelSerializer):
	class Meta:
		model = TrainingProgram
		fields = ('id',
				  'training_name',
				  'description',
				  'eligibility',
				  'company_name',
				  'company',
				  'start_date',
				  'duration',
				  'stipend',
				  'deadline',
				  'applicants_count',
				  'status',
				  'category',
				)

class TrainingProgramSerializer_CView(serializers.ModelSerializer):
	class Meta:
		model = TrainingProgram
		fields = ('id',
				  'training_name',
				  'applicants_count',
				  'status'
				)

class StudentApplicationSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentApplications
		fields = ('id',
				  'training',
				  'student',
				  'status',
				)


class ListTrainingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = TrainingProgram
		fields = ('id',
				  'training_name',
				  'company_name',
				  'start_date',
				  'duration',
				  'stipend',
				  'deadline',
				  'status'
				)

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = login_db
		fields = ('email',
				  'password'
				)
