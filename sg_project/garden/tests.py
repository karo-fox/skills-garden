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
        self.assertEqual(self.field1.__str__(), 'Test field')

    def test_topic_str(self):
        self.assertEqual(self.topic1.__str__(), 'Test topic')



class TestUrls(SimpleTestCase):

    def setUp(self):
        self.urlconf = 'garden.urls'

    def test_home_url_resolves(self):
        url = reverse('home', urlconf=self.urlconf)
        self.assertEqual(resolve(url).func.view_class, HomeView)



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.urlconf = 'garden.urls'

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
    
    def test_home_view(self):
        response = self.client.get(reverse('home', urlconf=self.urlconf))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertQuerysetEqual(response.context['object_list'], Field.objects.all())


    def test_field_view(self):
        response = self.client.get(reverse('field', kwargs={'pk': 1}, urlconf=self.urlconf))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'field.html')
        self.assertQuerysetEqual(response.context['topic_list'], Topic.objects.filter(field=self.field1))
    

    def test_topic_view(self):
        response = self.client.get(reverse('topic', kwargs={'pk': 1, 'field_pk': 1}, urlconf=self.urlconf))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topic.html')