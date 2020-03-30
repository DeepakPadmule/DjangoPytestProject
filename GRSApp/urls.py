from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'grievances', views.GrievanceList.as_view(), name='grievances'),
    url(r'grievance/(?P<pk>G-[0-9]{4})', views.GrievanceUpdate.as_view(), name='single_grievance'),
    url(r'grievanceTypes', views.GrievanceTypeList.as_view(), name='grievance_types'),
    url(r'grievanceType/(?P<pk>GT-[0-9]{4})', views.GrievanceTypeUpdate.as_view(), name='single_grievance_type'),
    url(r'grievanceDetails', views.GrievanceDetailList.as_view(), name='grievance_details'),
    url(r'grievanceDetail/(?P<pk>GD-[0-9]{4})', views.GrievanceDetailUpdate.as_view(), name='single_grievance_detail'),
]