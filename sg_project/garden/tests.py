import datetime

from django.test import TestCase
from .models import Field, Topic

class TestFields(TestCase):

    def setUp(self):
        date_added = datetime.date(2021, 4, 1)
        last_reviewed = datetime.date(2021, 5, 18)
        review_frequency = datetime.timedelta(14)
        self.field1 = Field.objects.create(
            name='Test',
            description='test test test',
            date_added=date_added,
            last_reviewed=last_reviewed,
            review_frequency=review_frequency
            )
    

    def test_str(self):
        self.assertEqual(self.field1.__str__(), 'Field: Test - 14 days, 0:00:00 - 2021-05-18')
