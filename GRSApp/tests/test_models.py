import pytest
from mock import patch

from ..factories import GrievanceTypesFactory, GrievancesFactory, GrievanceDetailsFactory


@pytest.fixture
def create_grievance_type():
    return GrievanceTypesFactory.create(griev_type="Water")


@pytest.fixture
def create_grievance():
    return GrievancesFactory.create(griev_title="Water Supply Issue")


@pytest.fixture
def create_grievance_status():
    return GrievanceDetailsFactory.create(griev_status="Pending")


@pytest.mark.django_db
class TestModels():

    @patch('__main__.create_grievance_type')
    def test_valid_grievance_type(self, patched_create_grievance_type):
        assert patched_create_grievance_type.called is True

    def test_invalid_grievance_type(self, create_grievance_type):
        assert create_grievance_type.get_type != "Electricity"

    def test_valid_grievance_title(self, create_grievance):
        assert create_grievance.get_title == "Water Supply Issue"

    def test_invalid_grievance_title(self, create_grievance):
        assert create_grievance.get_title != "Electricity Supply Issue"

    def test_valid_grievance_status(self, create_grievance_status):
        assert create_grievance_status.get_status == "Pending"

    def test_invalid_grievance_status(self, create_grievance_status):
        assert create_grievance_status.get_status != "Accepted"
