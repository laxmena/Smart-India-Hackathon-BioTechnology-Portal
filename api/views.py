from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from api.serializers import CompanySerializer
from api.serializers import StudentSerializer
from api.serializers import TrainingProgramSerializer
from api.serializers import StudentApplicationSerializer
from api.serializers import ListTrainingsSerializer
from api.serializers import LoginSerializer
from api.serializers import TrainingProgramSerializer_CView
from api.serializers import SignUpSerializer
#from api.serializers import SfqSerializer
#from api.serializers import SfcSerializer
#from api.serializers import SfoSerializer

from api.models import Student
from api.models import Company
from api.models import TrainingProgram
from api.models import StudentApplications
from api.models import login_db
#from api.models import student_feedback_questions
#from api.models import student_feedback_choice
#from api.models import student_feedback_options

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.http import JsonResponse

from json import JSONEncoder
import json

class login(APIView):
	def get(self, request, format=None):
		serializer = LoginSerializer(data=request.data)
		if serializer.is_valid():
			userAuth = authenticate(username=serializer.data['email'], password=serializer.data['password'])
			if userAuth:
				return Response(status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
#		return Response(request.body)
		try:
			data = json.loads(str(request.body)[2:-1])
			username = data['email']
			password = data['password']
		except:	
			val = str(request.body)[2:-1].split("&")
			username = val[0].split('=')[1]
			password = val[1].split('=')[1]
		userAuth = authenticate(username=username,password=password)
		if userAuth:
			obj = User.objects.get(username=username)
			serializer = SignUpSerializer(obj)
			return Response(serializer.data)
		return Response(status="status.HTTP_400_BAD_REQUEST")



# class login(APIView):
# 	"""
# 		login

# 		URL: [ip]:8000/login/
# 		Method: POST
# 		Parameters: email, password
# 		Output: 

# 		Description:
# 			Login Method
# 	"""
# 	def post(self, request, format=None):
# 		return HttpResponse("Hello")

class logout(APIView):
	"""
	"""
	def post(self, request, format=None):
		logout(request)

class add_company(APIView):
	"""
		add_company

		URL: [ip]:8000/api/addcompany/
		Method: POST
		Parameters: company_name,
				  	address1,
				  	address2,(optional)
				  	city,
				  	state,
				  	pin,
				  	mobile,
				  	telephone,(optional)
				  	description,
				  	website,(optional)
				  	email,
				  	password
		Description
			API to create a new company profile.
	"""
	def post(self, request, format=None):
		req_data = request.body
		data = {}
		try:
			data = json.loads(str(req_data)[2:-1])
		except:
			val = str(request.body)[2:-1].split("&")
			for i in val:
				i = i.split('=')
				data[i[0]]=i[1]
		obj = Student(company_name=data['company_name'],
					  address1=data['address1'],
					  address2=data['address2'],
					  city= data['city'],
					  state = data['state'],
					  pin= data['pin'],
					  mobile= data['mobile'],
					  email = data['email'],
					  description=data['description'],
					  website=data['website'],
					  password=data['password'],
					)
		obj.save()
#		user = User.objects.create_user(obj['email'],obj['email'],obj['password'])
		return HttpResponse(obj)
		# serializer = CompanySerializer(data=data)
		# if serializer.is_valid():
		# 	serializer.save()
		# 	return Response(serializer.data, status=status.HTTP_201_CREATED)
		# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)@login_required

class company_details(LoginRequiredMixin,APIView):
	""" 
		company_details

		URL: [ip]:8000/api/company/[company_id]/
		Method: GET
		Parameters:	id,
					company_name,
				  	address1,
				  	address2,(optional)
				  	city,
				  	state,
				  	pin,
				  	mobile,
				  	telephone,(optional)
				  	description,
				  	website,(optional)
				  	email
		Output:

		Description:
			API to get the details about a company given its company_id
	"""
	def post(self,request,pk,format=None):
	    companyobj = Company.objects.get(id=pk)
	    serializer = CompanySerializer(companyobj)
	    return Response(serializer.data)
	def get(self,request,pk,format=None):
	    companyobj = Company.objects.get(id=pk)
	    serializer = CompanySerializer(companyobj)
	    return Response(serializer.data)

class add_student(APIView):
	"""
		add_student

		URL: [ip]:8000/api/addstudent/
		Method: POST
		Parameters:	first_name,
					last_name,
					gender,
					email,
					password,
					college,
					city,
					state,
					graduation_year,
					mobile,
					telephone

		Output: 

		Description:
			API to create a new student account/profile.
	"""
	def post(self, request, format=None):
		req_data = str(request.body)[2:-1]
		data = {}
		try:
			data = json.loads(req_data)

		except:
			val = str(request.body)[2:-1].split("&")
			for i in val:
				i = i.split('=')
				data[i[0]]=i[1]
		obj = Student(email=data['email'],
					  first_name=data['first_name'],
					  last_name=data['last_name'],
					  gender= data['gender'],
					  college = data['college'],
					  city = data['city'],
					  graduation_year= data['graduation_year'],
					  mobile = data['mobile'],
					)
		obj.save()
#		user = User.objects.create_user(obj['email'],obj['email'],obj['password'])
		return HttpResponse(obj)
		#return Response("Error", status=status.HTTP_400_BAD_REQUEST)


class student_details(APIView):
	"""
		student_details

		URL: [ip]:8000/api/student/[student_id]/
		Method: GET
		Parameters:	id,
				    first_name,
				    last_name,
				    gender,
				    email,
				    college,
				    city,
				    state,
				    graduation_year,
				    mobile,
				    telephone
				
		Output:

		Description:
			API to retrieve student details given the student id.
	"""
	def get(self,request,pk,format=None):
		studentobj = Student.objects.get(id=pk)
		serializer = StudentSerializer(studentobj)
		return Response(serializer.data)

	def post(self,request,pk,format=None):
		studentobj = Student.objects.get(id=pk)
		serializer = StudentSerializer(studentobj)
		return Response(serializer.data)

class add_training(APIView):
	"""
		add_training

		URL: [ip]:8000/api/addtraining/
		Method: POST
		Parameters: training_name,
					description,
				    eligibility,
				    company,
				    start_date,
				    duration,
				    stipend,
				    deadline
		Output:

		Description:
			API to create a new training program
	"""
	def post(self, request, format=None):
		req_data = str(request.body)[2:-1]
		data = {}
		try:
			data = json.loads(req_data)

		except:
			val = str(request.body)[2:-1].split("&")
			for i in val:
				i = i.split('=')
				data[i[0]]=i[1]
		obj = TrainingProgram(training_name=data['training_name'],
					  description=data['description'],
					  eligibility=data['eligibility'],
					  company= Company.objects.get(id=data['company']),
					  start_date = data['start_date'],
					  duration = data['duration'],
					  stipend= data['stipend'],
					  deadline = data['deadline'],
					)
		obj.save()
#		user = User.objects.create_user(obj['email'],obj['email'],obj['password'])
		return HttpResponse(obj)

class list_trainings(APIView):
	"""
		list_trainings

		URL: [ip]:8000/api/listtrainings/
		Method: GET
		Parameters: id,
					training_name,
				    company,
				    company_name,
				    start_date,
				    stipend,
				    deadline
		Description:
			API to list all training availabiilities
	"""
	def get(self,request,format=None):
		listOfTrainings = TrainingProgram.objects.filter(status="published")
		serializer = ListTrainingsSerializer(listOfTrainings, many=True)
		return Response(serializer.data)

	def post(self,request, format=None):
		listOfTrainings = TrainingProgram.objects.filter(status="published")
		serializer = ListTrainingsSerializer(listOfTrainings, many=True)
		return Response(serializer.data)


class all_trainings(APIView):
	"""
		list_trainings

		URL: [ip]:8000/api/listtrainings/
		Method: GET
		Parameters: id,
					training_name,
				    company,
				    company_name,
				    start_date,
				    stipend,
				    deadline
		Description:
			API to list all training availabiilities
	"""
	def get(self,request,format=None):
		listOfTrainings = TrainingProgram.objects.all()
		serializer = ListTrainingsSerializer(listOfTrainings, many=True)
		return Response(serializer.data)

	def post(self,request, format=None):
		listOfTrainings = TrainingProgram.objects.all()
		serializer = ListTrainingsSerializer(listOfTrainings, many=True)
		return Response(serializer.data)

class training_approval(APIView):
	"""
		training_approval

		URL: [ip]:8000/api/approve/[id]
		Method: POST
		Parameters:
	"""
	def get(self,request,pk,format=None):
		pk = int(pk)
		approval_status = pk%10
		pk = pk//10
		trainingObj = TrainingProgram.objects.get(id=pk)
		if approval_status == 1:
			trainingObj.status="published"
		else:
			trainingObj.status="discarded"
		trainingObj.save()
		return HttpResponse(trainingObj)
	def post(self,request,pk,format=None):
		pk = int(pk)
		approval_status = pk%10
		pk = pk//10
		trainingObj = TrainingProgram.objects.get(id=pk)
		if approval_status == 1:
			trainingObj.status="published"
		else:
			trainingObj.status="discarded"
		trainingObj.save()
		return HttpResponse(trainingObj)

class training_details(APIView):
	"""
		training_details

		URL: [ip]:8000/api/training/[training_id]/
		Method: GET
		Parameters:	id,
				    training_name,
				    description,
				  	eligibility,
				  	company,
				  	start_date,
				  	duration,
				  	stipend,
				  	deadline,
				  	applicants_count,

		Description:
			API to list details about the Training program, given the id.
	"""
	def get(self, request, pk, format=None):
		training = TrainingProgram.objects.get(id=pk)
		serializer = TrainingProgramSerializer(training)
		return Response(serializer.data)

	def post(self, request, pk, format=None):
		training = TrainingProgram.objects.get(id=pk)
		serializer = TrainingProgramSerializer(training)
		return Response(serializer.data)

class application_status(APIView):
	"""
		application_status

		URL:
		Method: GET
		Parameters: id,
					training(id),
					student(is=d),
					status
		Note:
			1		->		Processing Application
			2 		->		MCQ Screening
			3		->		Interview Process
			4		->		Company Matched
			5		->		Internship Started
			6		->		Completed Internship
			7		->		Stipend Recieved
			-ve 	->		Rejected

		Description:
			API to view the status of Student Application
	"""
	def get(self, request, pk, format=None):
		application = StudentApplications.objects.get(id=pk)
		serializer = StudentApplicationSerializer(application)
		return Response(serializer.data)

	def post(self, request, pk, format=None):
		application = StudentApplications.objects.get(id=pk)
		serializer = StudentApplicationSerializer(application)
		return Response(serializer.data)


class apply_training(APIView):
	"""
		apply_training

		URL: [ip]:8000/api/apply/
		Method: POST
		Parameters:	training(id)
					student(id)
		Descripiton:
			API to hit when student applies for an internship
	"""
	def post(self, request, format=None):
		data = {}
		req_data = str(request.body)[2:-1]
		try:
			data = json.loads(req_data)
			return HttpResponse("Try Block")	 
		except:
			val = req_data
			#return Response(req_data)
			temp = val.split('&')
			for i in temp:
				i = i.split('=')
				data[i[0]]=i[1]
		serializer = StudentApplicationSerializer(data=data)
		if serializer.is_valid():
			# serializer.data['training'] = data['training']
			# serializer.data['student'] = data['student']
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class company_view_training(APIView):
	"""
	Description:
		API returns all applied training programs by the company, latest first
	"""
	def get(self,request,pk,format=None):
		training_list = TrainingProgram.objects.all().filter(company_id=pk)
		serializer = TrainingProgramSerializer_CView(training_list, many=True)
		return Response(serializer.data)

	def post(self,request,pk,format=None):
		training_list = TrainingProgram.objects.all().filter(id=pk)
		serializer = TrainingProgramSerializer_CView(training_list, many=True)
		return Response(serializer.data)

class postStudentFeedback(APIView):
	def post(self,request,format=None):
		data = {}
		req_data = str(request.body)[2:-1]
		return HttpResponse("Response")