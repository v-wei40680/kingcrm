from django.test import TestCase

from crm.models import CustomerInfo

class CustomerInfoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomerInfo.objects.create(name='lisa', source=0, consult_courses='sqlite3 group', status=0, consultant='bar')

    def test_consultant_label(self):
        customer = CustomerInfo.objects.first()
        name = customer.name
        self.assertEquals(name, 'bar')
