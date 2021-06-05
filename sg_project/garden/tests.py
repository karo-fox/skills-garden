import datetime
import json

from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from .models import Field, Topic
from .views import FieldListCreate, TopicListCreate



class TestModels(TestCase):

    def setUp(self):
        date_added = datetime.date(2021, 4, 1)
        last_reviewed = datetime.date(2021, 5, 18)
        self.field1 = Field.objects.create(
            name='Test field',
            description='test test test',
            date_added=date_added,
            last_reviewed=last_reviewed,
            review_frequency=14
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
    
    def test_fields_list_url_resolves(self):
        url = reverse('garden:fields')
        self.assertEqual(resolve(url).func.view_class, FieldListCreate)
    

    def test_topics_list_url_resolves(self):
        url = reverse('garden:topics', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, TopicListCreate)



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()


    def test_fields_list_view(self):
        response = self.client.get(reverse('garden:fields'))

        self.assertEqual(response.status_code, 200)


    def test_topics_list_view(self):
        response = self.client.get(reverse('garden:topics', kwargs={ 'pk': 1 }))

        self.assertEqual(response.status_code, 200)