from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
	"""
	Model: Student
	Description:
		Table contains details about registered Students.
	Number of Fields: 14
	Fields: 
		id 					(Auto Generated)	
		email 			(unique)					max_length = 100
		first_name										max_length = 50
		last_name			(optional)					max_length = 50
		gender											'M' or 'F' or 'O'
		college											max_length = 100
		address1										max_length = 100
		address2			(optional)					max_length = 100
		city											max_length = 50
		state											max_length = 50
		graduation_year		(default = next year)		Integer Field
		mobile											IntegerField
		telephone			(optional)					IntegerField
		inserted_on			
	"""
	email = models.EmailField(max_length=100)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50,blank = True)
	gender = models.CharField(max_length=6,default='male')
	college = models.CharField(max_length=100)
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100,blank = True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	graduation_year = models.IntegerField(default=date.today().year+1)
	mobile = models.IntegerField()
	login_credential = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	telephone = models.IntegerField(null=True,blank=True)
	inserted_on = models.DateTimeField('Record inserted on',auto_now_add=True, blank=True)

class Company(models.Model):
	"""
	Model: Company
	Description:
		Table contains details about the registered Companies.
	Number of Fields: 12
	Fields:	
		id 					(Auto Generated)
		company_name						max_length = 100
		address1							max_length = 100
		address2			(optional)		max_length = 100
		city								max_length = 50
		state								max_length = 50
		pin									IntegerField
		mobile								IntegerField
		telephone			(optional)		IntegerField
		description			(optional)		max_length = 500
		website				(optional)		max_length = 100
		email 			(unique)		max_length = 100
		inserted_on
	"""
	company_name = models.CharField(max_length=100)
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100,blank = True,null = True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	pin = models.IntegerField()
	mobile = models.IntegerField()
	telephone = models.IntegerField(blank=True,null=True)
	description = models.CharField(max_length=500,blank = True,null = True)
	website = models.CharField(max_length=100,blank = True,null = True)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100,default="password",null=True)
	inserted_on = models.DateTimeField('Record inserted on',auto_now_add=True, blank=True)

	class Meta:
		ordering = ('company_name',)

class TrainingProgram(models.Model):
	"""
	Model: TrainingProgram
	Description:
		Table contains details about Published Training Programs.
	Number of Fields: 11 
	Fields:
		id 					(Auto Generated)
		training_name							max_length = 200
		description 							max_length = 500
		eligibility			(optional)			max_length = 300
		company 			Foreign key 		ConnectedTo: Company
		start_date 								DateTimeField
		duration 								max_length = 50
		stipend 			(optional)			IntegerField
		deadline 								DateTimeField
		applications_count						IntegerField	
		inserted_on
		status 									max_length = 20
	Note:
		1. company field is a foreign key
		2. duration is charfield, Insert value in the following format
			10 Days (or) 2 Weeks (or) 6 Months
			Format: (Integer Field) + (Days or Weeks or Months)
		3. Status can have either one of three options,
				(i)   "under review"
				(ii)  "published"
				(iii) "discarded"
	"""
	training_name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	eligibility = models.CharField(max_length=300, blank=True)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	company_name = models.CharField(max_length=100, default = "Unnamed")
	start_date = models.DateField('Training Start Date')
	duration = models.CharField(max_length=50)
	stipend = models.IntegerField(blank=True)
	deadline = models.DateField('Application Deadline')
	applicants_count = models.IntegerField(default=0)
	category = models.CharField(max_length=100, default="production",null=True)
	inserted_on = models.DateField('Record inserted on',auto_now_add=True, blank=True)
	status = models.CharField(max_length=20,default="under review")
	
	class Meta:
		ordering = ('inserted_on',)

class StudentApplications(models.Model):
	"""
	Model: StudentApplications
	Description:
		Table contains applications of students to training programmes
	Number of Fields: 5
	Fields:
		id 				(Auto Generated)
		training 		Foreign Key 		ConnectedTo: TrainingProgram
		student 		Foreign Key 		ConnectedTo: Student
		status			default = 0			IntegerField
		inserted_on
	Note:
		status is an Integer Field, in which each value abstracts a meaning
		Status:
			1		->		Processing Application
			2 		->		MCQ Screening
			3		->		Interview Process
			4		->		Company Matched
			5		->		Internship Started
			6		->		Completed Internship
			7		->		Stipend Recieved
			-ve 	->		Rejected
	"""
	training = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	status = models.IntegerField(default=1)
	inserted_on = models.DateField('Record inserted on',auto_now_add=True, blank=True)

	class Meta:
		ordering = ('inserted_on',)

class login_db(models.Model):
	"""
	"""
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=100)

class question_bank(models.Model):
	"""
	Model: question_bank
	Description:
		Table contains all multiple choice questions for screening test,
	which can be queried by using the training id.
	Number of Fields: 8
	Fields:
		id 				(Auto Generated)
		training 		Foreign Key 		ConnectedTo: TrainingProgram
		question 							max_length = 200
		answer 								max_length = 50
		choice1 							max_length = 50
		choice2 							max_length = 50
		choice3 							max_length = 50
		inserted_on  						
	"""
	training = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
	question = models.CharField(max_length=200)
	answer = models.CharField(max_length=50)
	choice1 = models.CharField(max_length=50)
	choice2 = models.CharField(max_length=50)
	choice3 = models.CharField(max_length=50)
	inserted_on = models.DateField('Record inserted on',auto_now_add=True, blank=True)

	class Meta:
		ordering = ('inserted_on','training')

class mcq_result(models.Model):
	"""
	Model: mcq
	Description:
		Table contains every MCQ submissions by the Students.
	Number of Fields: 
	Fields:
		id 				(Auto Generated)
		student 		Foreign Key 		ConnectedTo: Student
		question 		Foreign Key 		ConnectedTo: question_bank
		result 			IntegerField		Either 0 or 1
		inserted_on 	
	Note:
		result field will have values either 0 or 1
		0 - Wrong Answer
		1 - Correct answer
	"""
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	question = models.ForeignKey(question_bank, on_delete=models.CASCADE)
	result = models.IntegerField(default=0)
