import datetime

from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from .views import HomeView, FieldView, TopicView

from garden.models import Field, Topic


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('client:home')
        self.assertEqual(resolve(url).func.view_class, HomeView)


    def test_field_url_resolves(self):
        url = reverse('client:field', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, FieldView)


    def test_topic_url_resolves(self):
        url = reverse('client:topic', kwargs={'pk': 1, 'field_pk': 1})
        self.assertEqual(resolve(url).func.view_class, TopicView)



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.Field = Field.objects.create(name="TEST", description="test test test", date_added=datetime.date(2021, 5, 13),
                                          last_reviewed=datetime.date(2021, 6, 1), review_frequency=14)
        self.Topic = Topic.objects.create(name="TEST", description="test test test", date_added=datetime.date(2021, 5, 13),
                                          last_reviewed=datetime.date(2021, 6, 1), field=self.Field)
    

    def test_home_view(self):
        response = self.client.get(reverse('client:home'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    

    def test_field_view(self):
        response = self.client.get(self.Field.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'field.html')  


    def test_topic_view(self):
        response = self.client.get(self.Topic.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'topic.html')