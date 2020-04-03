import mock
from django.urls import reverse, resolve


def get_path():
    pass


class TestUrls():

    @mock.patch('GRSApp.tests.test_urls.get_path', return_value='/grievanceType/GT-0001')
    def test_single_grievance_type_url(self, mock_get_path):
        assert resolve(get_path()).view_name == 'single_grievance_type'
        assert mock_get_path.called is True

    @mock.patch('GRSApp.tests.test_urls.get_path', return_value='/grievanceTypes')
    def test_view_all_grievance_types_url(self, mock_get_path):
        assert resolve(get_path()).view_name == 'grievance_types'
        assert mock_get_path.called is True

    @mock.patch('GRSApp.tests.test_urls.get_path', return_value='/grievance/G-0001')
    def test_single_grievance_url(self, mock_get_path):
        assert resolve(get_path()).view_name == 'single_grievance'
        assert mock_get_path.called is True

    @mock.patch('GRSApp.tests.test_urls.get_path', return_value='/grievances')
    def test_view_all_grievances_url(self, mock_get_path):
        assert resolve(get_path()).view_name == 'grievances'
        assert mock_get_path.called is True

    @mock.patch('GRSApp.tests.test_urls.get_path', return_value='/grievanceDetail/GD-0001')
    def test_single_grievance_detail_url(self, mock_get_path):
        assert resolve(get_path()).view_name == 'single_grievance_detail'
        assert mock_get_path.called is True

    @mock.patch('GRSApp.tests.test_urls.get_path', return_value='/grievanceDetails')
    def test_view_all_grievance_details_url(self, mock_get_path):
        assert resolve(get_path()).view_name == 'grievance_details'
        assert mock_get_path.called is True
