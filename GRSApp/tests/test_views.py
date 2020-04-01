import pytest

from django.urls import reverse
from rest_framework import status

from ..factories import GrievanceTypesFactory, GrievancesFactory, GrievanceDetailsFactory


@pytest.fixture
def grievance_types_fixture():
    GrievanceTypesFactory.create_batch(10)


@pytest.fixture
def grievances_fixture():
    GrievancesFactory.create_batch(10)


@pytest.fixture
def grievance_details_fixture():
    GrievanceDetailsFactory.create_batch(10)


@pytest.mark.django_db
class TestViews():

    def test_valid_single_grievance_type(self, client, grievance_types_fixture):
        grievance_types_fixture
        path = reverse('single_grievance_type', kwargs={'pk': "GT-0001"})
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    def test_invalid_single_grievance_type(self, client, grievance_types_fixture):
        grievance_types_fixture
        path = reverse('single_grievance_type', kwargs={'pk': "GT-0111"})
        response = client.get(path)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_all_grievance_types(self, client, grievance_types_fixture):
        grievance_types_fixture
        path = reverse('grievance_types')
        response = client.get(path)
        print(response.data)
        assert response.status_code == status.HTTP_200_OK

    def test_valid_single_grievance(self, client, grievances_fixture):
        grievances_fixture
        path = reverse('single_grievance', kwargs={'pk': "G-0001"})
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    def test_invalid_single_grievance(self, client, grievances_fixture):
        grievances_fixture
        path = reverse('single_grievance', kwargs={'pk': "G-0111"})
        response = client.get(path)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_all_grievances(self, client, grievances_fixture):
        grievances_fixture
        path = reverse('grievances')
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    def test_single_grievance_detail(self, client, grievance_details_fixture):
        grievance_details_fixture
        path = reverse('single_grievance_detail', kwargs={'pk': "GD-0001"})
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    def test_all_grievance_details(self, client, grievance_details_fixture):
        grievance_details_fixture
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
