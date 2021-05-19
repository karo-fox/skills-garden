import datetime

from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from .models import Field, Topic
from .views import HomeView



class TestModels(TestCase):

    def setUp(self):
        date_added = datetime.date(2021, 4, 1)
        last_reviewed = datetime.date(2021, 5, 18)
        review_frequency = datetime.timedelta(14)
        self.field1 = Field.objects.create(
            name='Test field',
            description='test test test',
            date_added=date_added,
            last_reviewed=last_reviewed,
            review_frequency=review_frequency
        )
        self.topic1 = Topic.objects.create(
            name='Test topic',
            description='test test test',
            date_added=date_added,
            last_reviewed=last_reviewed,
            field=self.field1
        )
    

    def test_field_str(self):
        self.assertEqual(self.field1.__str__(), 'Field: Test field - 14 days, 0:00:00 - 2021-05-18')

    def test_topic_str(self):
        self.assertEqual(self.topic1.__str__(), 'Topic: Test topic - Test field - 2021-05-18')



class TestUrls(SimpleTestCase):

    def setUp(self):
        self.urlconf = 'garden.urls'

    def test_home_url_resolves(self):
        url = reverse('home', urlconf=self.urlconf)
        self.assertEqual(resolve(url).func.view_class, HomeView)



class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.urlconf = 'garden.urls'
    
    def test_home_view(self):
        response = self.client.get(reverse('home', urlconf=self.urlconf))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertQuerysetEqual(response.context['object_list'], Field.objects.all())
