from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^addcompany/$', views.add_company.as_view(), name="addcompany"),
	url(r'^company/(?P<pk>[0-9]+)/$', views.company_details.as_view(), name="company_details"),
	url(r'^addstudent/$',views.add_student.as_view(), name="addstudent"),
	url(r'^student/(?P<pk>[0-9]+)/$',views.student_details.as_view(), name="student_details"),
	url(r'^addtraining/$',views.add_training.as_view(), name="addtraining"),
	url(r'^listtrainings/$',views.list_trainings.as_view(), name="list_trainings"),
	url(r'^training/(?P<pk>[0-9]+)/$', views.training_details.as_view(), name="training_details"),
	url(r'^studentstatus/(?P<pk>[0-9]+)/$',views.application_status.as_view(), name="status"),
	url(r'^approve/(?P<pk>[0-9]+)/$',views.training_approval.as_view(),name="approve"),	
	url(r'^apply/$',views.apply_training.as_view(),name="apply"),
	url(r'^cviewtraining/(?P<pk>[0-9]+)/$',views.company_view_training.as_view(),name="cviewtraining"),
	url(r'^alltrainings/',views.all_trainings.as_view()),
]