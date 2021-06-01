import datetime
import json

from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from .models import Field, Topic
from .views import HomeView, FieldView, field_list_view, topic_list_view



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

    def test_home_url_resolves(self):
        url = reverse('garden:home')
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_field_url_resolves(self):
        url = reverse('garden:field', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, FieldView)
    
    def test_fields_list_url_resolves(self):
        url = reverse('garden:fields-list')
        self.assertEqual(resolve(url).func, field_list_view)
    
    def test_topics_list_url_resolves(self):
        url = reverse('garden:topics-list', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, topic_list_view)



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
    
    def test_home_view(self):
        response = self.client.get(reverse('garden:home'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_field_view(self):
        response = self.client.get(reverse('garden:field', kwargs={ 'pk': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'field.html')


    def test_fields_list_view(self):
        response = self.client.get(reverse('garden:fields-list'))

        self.assertEqual(response.status_code, 200)

    def test_topics_list_view(self):
        response = self.client.get(reverse('garden:topics-list', kwargs={ 'pk': 1 }))

        self.assertEqual(response.status_code, 200)