import mock
import pytest

from .. import models


@pytest.mark.django_db
class TestModels():

    @mock.patch('GRSApp.models.GrievanceTypes.get_type', return_value="Pollution")
    def test_valid_grievance_type(self, mock_get_type):
        class_obj = models.GrievanceTypes()
        assert class_obj.get_type() == "Pollution"
        assert mock_get_type.called is True

    @mock.patch('GRSApp.models.GrievanceTypes.get_type', return_value="Pollution")
    def test_invalid_grievance_type(self, mock_get_type):
        class_obj = models.GrievanceTypes()
        assert class_obj.get_type() != "Electricity"
        assert mock_get_type.called is True

    @mock.patch('GRSApp.models.Grievances.get_title', return_value="Water Supply Issue")
    def test_valid_grievance_title(self, mock_get_title):
        class_obj = models.Grievances()
        assert class_obj.get_title() == "Water Supply Issue"
        assert mock_get_title.called is True

    @mock.patch('GRSApp.models.Grievances.get_title', return_value="Water Supply Issue")
    def test_invalid_grievance_title(self, mock_get_title):
        class_obj = models.Grievances()
        assert class_obj.get_title() != "Electricity Supply Issue"
        assert mock_get_title.called is True

    @mock.patch('GRSApp.models.GrievanceDetails.get_status', return_value="Pending")
    def test_valid_grievance_status(self, mock_get_status):
        class_obj = models.GrievanceDetails()
        assert class_obj.get_status() == "Pending"
        assert mock_get_status.called is True

    @mock.patch('GRSApp.models.GrievanceDetails.get_status', return_value="Pending")
    def test_invalid_grievance_status(self, mock_get_status):
        class_obj = models.GrievanceDetails()
        assert class_obj.get_status() != "Accepted"
        assert mock_get_status.called is True
