from django.urls import reverse, resolve


class TestUrls():

    def test_single_grievance_type_url(self):
        path = reverse('single_grievance_type', kwargs={'pk': "GT-0001"})
        assert resolve(path).view_name == 'single_grievance_type'

    def test_view_all_grievance_types_url(self):
        path = reverse('grievance_types')
        assert resolve(path).view_name == 'grievance_types'

    def test_single_grievance_url(self):
        path = reverse('single_grievance', kwargs={'pk': "G-0001"})
        assert resolve(path).view_name == 'single_grievance'

    def test_view_all_grievances_url(self):
        path = reverse('grievances')
        assert resolve(path).view_name == 'grievances'

    def test_single_grievance_detail_url(self):
        path = reverse('single_grievance_detail', kwargs={'pk': "GD-0001"})
        assert resolve(path).view_name == 'single_grievance_detail'

    def test_view_all_grievance_details_url(self):
        path = reverse('grievance_details')
        assert resolve(path).view_name == 'grievance_details'
