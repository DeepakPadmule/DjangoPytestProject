from django.urls import reverse, resolve
from mixer.backend.django import mixer


class TestGrievanceTypes():

    # def __init__(self):
    #     mixer.blend('GRSApp.GrievanceTypes', griev_type="Water")

    # def test_single_grievance_type(self):
    #     path = reverse('single_grievance_type', kwargs={'pk': "GT0001"})
    #     print("hi...........")
    #     assert resolve(path).view_name == 'single_grievance_type'

    def test_view_all_grievanceTypes_url(self):
        path = reverse('grievance_types')
        assert resolve(path).view_name == 'grievance_types'

    def test_view_all_grievances_url(self):
        path = reverse('grievances')
        assert resolve(path).view_name == 'grievances'

    def test_view_all_grievanceDetails_url(self):
        path = reverse('grievance_details')
        assert resolve(path).view_name == 'grievance_details'
