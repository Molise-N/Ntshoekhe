from django.test import TestCase
from django.urls import reverse

class HospitalListViewTests(TestCase):
    def test_hospital_list_view(self):
        url = reverse('hospital-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'hospitals': []}  # Add expected data here
        )
