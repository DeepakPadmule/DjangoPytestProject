from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestModels():

    def test_valid_grievance_type(self):
        grievance_type = mixer.blend('GRSApp.GrievanceTypes', griev_type="Water")
        assert grievance_type.get_type == "Water"

    def test_invalid_grievance_type(self):
        grievance_type = mixer.blend('GRSApp.GrievanceTypes', griev_type="Electricity")
        assert grievance_type.get_type != "Water"

    def test_valid_grievance_title(self):
        grievance = mixer.blend('GRSApp.Grievances', griev_title="Water Supply Issue")
        assert grievance.get_title == "Water Supply Issue"

    def test_invalid_grievance_title(self):
        grievance = mixer.blend('GRSApp.Grievances', griev_title="Electricity Supply Issue")
        assert grievance.get_title != "Water Supply Issue"

    def test_valid_grievance_status(self):
        grievance_detail = mixer.blend('GRSApp.GrievanceDetails', griev_status="Pending")
        assert grievance_detail.get_status == "Pending"

    def test_invalid_grievance_status(self):
        grievance_detail = mixer.blend('GRSApp.GrievanceDetails', griev_status="Accepted")
        assert grievance_detail.get_status != "Pending"
