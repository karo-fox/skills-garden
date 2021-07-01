import datetime
import json

from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from rest_framework.test import APIClient, APITestCase

from .models import Field, Topic
from .views import FieldListCreate, TopicListCreate, FieldUpdateDestroy



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
    
    def test_fields_url_resolves(self):
        url = reverse('garden:fields')
        self.assertEqual(resolve(url).func.view_class, FieldListCreate)
    

    def test_field_action_url_resolves(self):
        url = reverse('garden:field-action', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, FieldUpdateDestroy)
    

    def test_topics_url_resolves(self):
        url = reverse('garden:topics', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, TopicListCreate)



class TestFieldViews(APITestCase):

    def setUp(self):
        self.client = APIClient()


    def test_fields_get_view(self):
        response = self.client.get(reverse('garden:fields'))

        self.assertEqual(response.status_code, 200)
    

    # def test_field_edit_view(self):
    #     response = self.client.put(reverse('garden:field-action', kwargs={'pk': 1}), data={'name': 'new test name', 'description': 'new test decription', 'review_frequency': 14})

    #     self.assertEqual(response.status_code, 200)



class TestTopicViews(APITestCase):

    def setUp(self):
        self.client = APIClient()


    def test_topics_get_view(self):
        response = self.client.get(reverse('garden:topics', kwargs={ 'pk': 1 }))

        self.assertEqual(response.status_code, 200)

