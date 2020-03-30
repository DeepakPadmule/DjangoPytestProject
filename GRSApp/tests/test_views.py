import pytest

from django.urls import reverse
from mixer.backend.django import mixer

from rest_framework import status


@pytest.mark.django_db
class TestViews():

    def test_valid_single_grievance_type(self, client):
        mixer.blend('GRSApp.GrievanceTypes')
        path = reverse('single_grievance_type', kwargs={'pk': "GT-0001"})
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    def test_invalid_single_grievance_type(self, client):
        mixer.blend('GRSApp.GrievanceTypes')
        path = reverse('single_grievance_type', kwargs={'pk': "GT-0005"})
        response = client.get(path)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_all_grievance_types(self, client):
        mixer.blend('GRSApp.GrievanceTypes')
        path = reverse('grievance_types')
        response = client.get(path)
        print(response.data)
        assert response.status_code == status.HTTP_200_OK

    def test_valid_single_grievance(self, client):
        mixer.blend('GRSApp.Grievances')
        path = reverse('single_grievance', kwargs={'pk': "G-0001"})
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    def test_invalid_single_grievance(self, client):
        mixer.blend('GRSApp.Grievances')
        path = reverse('single_grievance', kwargs={'pk': "G-0005"})
        response = client.get(path)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_all_grievances(self, client):
        mixer.blend('GRSApp.Grievances')
        path = reverse('grievances')
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    def test_single_grievance_detail(self, client):
        mixer.blend('GRSApp.GrievanceDetails')
        path = reverse('single_grievance_detail', kwargs={'pk': "GD-0001"})
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    def test_all_grievance_details(self, client):
        mixer.blend('GRSApp.GrievanceDetails')
        path = reverse('grievance_details')
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    def test_post_grievance_type(self, client):
        path = reverse('grievance_types')
        griev_data = {
            "griev_type": "Road"
        }
        response = client.post(path, data=griev_data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_valid_post_grievance(self, client):
        path = reverse('grievances')
        griev_data = {
            "griev_title": "Road Issue",
            "griev_desc": "We are suffering with road issues."
        }
        response = client.post(path, data=griev_data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_invalid_post_grievance(self, client):
        path = reverse('grievances')
        griev_data = {
            "griev_title": "",
            "griev_desc": "We are suffering with road issues."
        }
        response = client.post(path, data=griev_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST