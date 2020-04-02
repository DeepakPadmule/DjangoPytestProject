import mock
from django.urls import reverse, resolve


class TestUrls():

    def get_path(self):
        # path = reverse('single_grievance_type', kwargs={'pk': "GT-0001"})
        # print('get_path called......')
        # print(path)
        # return path
        pass

    @mock.patch('GRSApp.tests.test_urls.TestUrls.get_path')
    def test_single_grievance_type_url(self, mock_get_path):
        mock_get_path.return_value = '/grievanceType/GT-0001'
        assert resolve(self.get_path()).view_name == 'single_grievance_type'

    @mock.patch('GRSApp.tests.test_urls.TestUrls.get_path')
    def test_view_all_grievance_types_url(self, mock_get_path):
        mock_get_path.return_value = '/grievanceTypes'
        assert resolve(self.get_path()).view_name == 'grievance_types'

    @mock.patch('GRSApp.tests.test_urls.TestUrls.get_path')
    def test_single_grievance_url(self, mock_get_path):
        mock_get_path.return_value = '/grievance/G-0001'
        assert resolve(self.get_path()).view_name == 'single_grievance'

    @mock.patch('GRSApp.tests.test_urls.TestUrls.get_path')
    def test_view_all_grievances_url(self, mock_get_path):
        mock_get_path.return_value = '/grievances'
        assert resolve(self.get_path()).view_name == 'grievances'

    @mock.patch('GRSApp.tests.test_urls.TestUrls.get_path')
    def test_single_grievance_detail_url(self, mock_get_path):
        mock_get_path.return_value = '/grievanceDetail/GD-0001'
        assert resolve(self.get_path()).view_name == 'single_grievance_detail'

    @mock.patch('GRSApp.tests.test_urls.TestUrls.get_path')
    def test_view_all_grievance_details_url(self, mock_get_path):
        mock_get_path.return_value = '/grievanceDetails'
        assert resolve(self.get_path()).view_name == 'grievance_details'
