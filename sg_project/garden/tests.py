import datetime
import json

from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from .models import Field, Topic
from .views import HomeView, field_list_view, topic_list_view



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
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomeView)
    
    def test_fields_url_resolves(self):
        url = reverse('garden:fields')
        self.assertEqual(resolve(url).func, field_list_view)
    
    def test_topics_url_resolves(self):
        url = reverse('garden:topics', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, topic_list_view)



# class TestViews(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.urlconf = 'garden.urls'

#         self.date_added = datetime.date(2021, 4, 1)
#         self.last_reviewed = datetime.date(2021, 5, 18)
#         self.review_frequency = datetime.timedelta(14)
#         self.field1 = Field.objects.create(
#             name='Test field',
#             description='test test test',
#             date_added=self.date_added,
#             last_reviewed=self.last_reviewed,
#             review_frequency=self.review_frequency
#         )
#         self.topic1 = Topic.objects.create(
#             name='Test topic',
#             description='test test test',
#             date_added=self.date_added,
#             last_reviewed=self.last_reviewed,
#             field=self.field1
#         )
    
#     def test_home_view(self):
#         response = self.client.get(reverse('home'))
        
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'index.html')


#     def test_field_list_view(self):
#         response = self.client.get(reverse('fields', urlconf=self.urlconf))
#         # expected_response = {
#         #     'fields': [{
#         #         'pk': 1,
#         #         'name': 'Test field',
#         #         'description': 'test test test',
#         #         'date_added': self.date_added.__str__(),
#         #         'last_reviewed': self.last_reviewed.__str__(),
#         #         'review_frequency': self.review_frequency.__repr__()
#         #     }]
#         # }
#         print('-'*30)
#         print(response)
#         self.assertEqual(response.status_code, 200)
#         # self.assertEqual(json.loads(response.content), expected_response)

#     def test_topic_list_view(self):
#         response = self.client.get(reverse('topics', kwargs={ 'pk': 1 }, urlconf=self.urlconf))

#         print('-'*30)
#         print(response)

#         self.assertEqual(response.status_code, 200)