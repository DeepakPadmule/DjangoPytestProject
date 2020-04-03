import mock
import pytest

from django.urls import reverse
from rest_framework import status
from django.test import Client

from ..factories import GrievanceTypesFactory, \
                        GrievancesFactory, \
                        GrievanceDetailsFactory
from ..models import GrievanceTypes, Grievances, GrievanceDetails
from ..serializers import GrievanceTypesSerializer, GrievancesSerializer, GrievanceDetailsSerializer


@pytest.fixture
def create_grievance_types_using_fixture():
    return GrievanceTypesFactory.create()


@pytest.fixture
def create_grievances_using_fixture():
    return GrievancesFactory.create()


@pytest.fixture
def create_grievance_details_using_fixture():
    GrievanceDetailsFactory.create()


client = Client()


def get_response():
    return '1'


@pytest.mark.django_db
class TestViews():

    def test_valid_single_grievance_type(self, create_grievance_types_using_fixture):
        create_grievance_types_using_fixture
        path = reverse('single_grievance_type', kwargs={'pk': "GT-0001"})
        response = client.get(path)
        print('response status code')
        print(response.status_code)
        assert response.status_code == status.HTTP_200_OK

    def test_invalid_single_grievance_type(self, create_grievance_types_using_fixture):
        create_grievance_types_using_fixture
        path = reverse('single_grievance_type', kwargs={'pk': "GT-0111"})
        response = client.get(path)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @mock.patch('GRSApp.models.GrievanceTypes.get_all_grievance_types', return_value=GrievanceTypes.objects.all())
    def test_all_grievance_types(self, mock_grievance_type):
        GrievanceTypesFactory.create_batch(10)
        response = client.get(reverse('grievance_types'))
        all_data = GrievanceTypes.get_all_grievance_types()
        serializer = GrievanceTypesSerializer(all_data, many=True)
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK
        assert mock_grievance_type.called is True

    def test_valid_single_grievance(self, create_grievances_using_fixture):
        create_grievances_using_fixture
        path = reverse('single_grievance', kwargs={'pk': "G-0001"})
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    def test_invalid_single_grievance(self, create_grievances_using_fixture):
        create_grievances_using_fixture
        path = reverse('single_grievance', kwargs={'pk': "G-0111"})
        response = client.get(path)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @mock.patch('GRSApp.models.Grievances.get_all_grievances', return_value=Grievances.objects.all())
    def test_all_grievances(self, mock_grievance):
        GrievancesFactory.create_batch(10)
        path = reverse('grievances')
        response = client.get(path)
        list_data = Grievances.get_all_grievances()
        serializer = GrievancesSerializer(list_data, many=True)
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK
        assert mock_grievance.called is True

    def test_single_grievance_detail(self, create_grievance_details_using_fixture):
        create_grievance_details_using_fixture
        path = reverse('single_grievance_detail', kwargs={'pk': "GD-0001"})
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    @mock.patch('GRSApp.models.GrievanceDetails.get_all_grievance_details', return_value=GrievanceDetails.objects.all())
    def test_all_grievance_details(self, mock_grievance_details):
        GrievanceDetailsFactory.create_batch(10)
        path = reverse('grievance_details')
        response = client.get(path)
        list_data = GrievanceDetails.get_all_grievance_details()
        serializer = GrievanceDetailsSerializer(list_data, many=True)
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK
        assert mock_grievance_details.called is True

    def test_post_grievance_type(self):
        path = reverse('grievance_types')
        griev_data = {
            "griev_type": "Road"
        }
        response = client.post(path, data=griev_data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_valid_post_grievance(self):
        path = reverse('grievances')
        griev_data = {
            "griev_title": "Road Issue",
            "griev_desc": "We are suffering with road issues."
        }
        response = client.post(path, data=griev_data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_invalid_post_grievance(self):
        path = reverse('grievances')
        griev_data = {
            "griev_title": "",
            "griev_desc": "We are suffering with road issues."
        }
        response = client.post(path, data=griev_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
