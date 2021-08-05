import datetime

from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient

from .views import TextSourceViewSet, URLSourceViewSet
from .models import TextSource, URLSource

from garden.models import Field, Topic


# class TestUrls(APITestCase):

#     def setUp(self):
#         self.client = APIClient()


#     def test_text_list_url_resolves(self):
#         url = reverse('sources:text-source-list', kwargs={'pk': 1})
#         self.assertEqual(resolve(url).func.view_class, TextSourceListCreate)

#     def test_url_list_url_resolves(self):
#         url = reverse('sources:url-list', kwargs={'pk':1})
#         self.assertEqual(resolve(url).func.view_class, URLSourceListCreate)

#     def test_text_action_url_resolves(self):
#         url = reverse('sources:text-action', kwargs={'pk':1})
#         self.assertEqual(resolve(url).func.view_class, TextSourceUpdateDestroy)

#     def test_url_action_url_resolves(self):
#         url = reverse('sources:url-action', kwargs={'pk':1})
#         self.assertEqual(resolve(url).func.view_class, URLSourceUpdateDestroy)


class TestViews(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.get_or_create(
            username='TestUser', password='K0n7073$7')[0]
        self.test_user.save()
        self.client.force_authenticate(user=self.test_user)
        date_added = datetime.date(2021, 4, 1)
        last_reviewed = datetime.date(2021, 5, 18)
        self.field = Field.objects.create(
            name='Test field',
            description='test test test',
            date_added=date_added,
            last_reviewed=last_reviewed,
            review_frequency=14,
            owner=self.test_user
        )
        self.topic = Topic.objects.create(
            name='Test topic',
            description='test test test',
            date_added=date_added,
            last_reviewed=last_reviewed,
            field=self.field
        )
        self.text_src = TextSource(
            name='new name', topic=self.topic, content='new content')
        self.url_src = URLSource(
            name='new name', topic=self.topic, content='https://www.google.com/')
        self.field.save()
        self.topic.save()
        self.text_src.save()
        self.url_src.save()

    def test_text_source_get(self):
        response = self.client.get(
            reverse('sources:text-source-list', kwargs={'topic_pk': 1}))

        self.assertEqual(response.status_code, 200)

    def test_text_source_create(self):
        data = {
            'name': 'test text source',
            'content': 'test text source content'
        }
        response = self.client.post(
            reverse('sources:text-source-list', kwargs={'topic_pk': 1}), data)

        self.assertEqual(response.status_code, 201)

    def test_text_source_update(self):
        data = {
            'name': 'updated text source',
            'content': 'updated text source content'
        }
        response = self.client.put(
            reverse('sources:text-source-detail', kwargs={'topic_pk': 1, 'pk': 1}), data)

        self.assertEqual(response.status_code, 200)

    def test_text_source_delete(self):
        response = self.client.delete(
            reverse('sources:text-source-detail', kwargs={'topic_pk': 1, 'pk': 1}))

        self.assertEqual(response.status_code, 204)

    def test_url_source_get(self):
        response = self.client.get(
            reverse('sources:url-source-list', kwargs={'topic_pk': 1}))

        self.assertEqual(response.status_code, 200)

    def test_url_source_create(self):
        data = {
            'name': 'test url source',
            'content': 'https://www.google.com/'
        }
        response = self.client.post(
            reverse('sources:url-source-list', kwargs={'topic_pk': 1}), data)

        self.assertEqual(response.status_code, 201)

    def test_url_source_update(self):
        data = {
            'name': 'updated url source',
            'content': 'https://www.google.com/'
        }
        response = self.client.put(
            reverse('sources:url-source-detail', kwargs={'topic_pk': 1, 'pk': 2}), data)

        self.assertEqual(response.status_code, 200)

    def test_url_source_delete(self):
        response = self.client.delete(
            reverse('sources:url-source-detail', kwargs={'topic_pk': 1, 'pk': 2}))

        self.assertEqual(response.status_code, 204)

    def tearDown(self):
        self.test_user.delete()
        self.field.delete()
        self.topic.delete()
        self.text_src.delete()
        self.url_src.delete()
