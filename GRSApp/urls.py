from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'grievances', views.GrievanceList.as_view(), name='grievances'),
    url(r'grievances/(?P<pk>[A-Z0-9])', views.GrievanceUpdate.as_view(), name='single_grievance'),
    url(r'grievanceTypes', views.GrievanceTypeList.as_view(), name='grievance_types'),
    url(r'grievanceTypes/(?P<pk>[A-Z0-9])', views.GrievanceTypeUpdate.as_view(), name='single_grievance_type'),
    url(r'grievanceDetails', views.GrievanceDetailList.as_view(), name='grievance_details'),
    url(r'grievanceDetails/(?P<pk>[.])', views.GrievanceDetailUpdate.as_view(), name='single_grievance_detail'),
]