from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from rest_framework.test import APIClient, APITestCase

from garden.models import Field, Topic

from .models import Entry

# class TestModel(TestCase):

#     def setUp(self):
#         self.test_user = User.objects.get_or_create(username='TestUser', password='K0n7073$7')[0]
#         self.test_user.save()
    

    
#     def tearDown(self):
#         self.test_user.delete()

class TestViews(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.get_or_create(username='TestUser', password='K0n7073$7')[0]
        self.test_user.save()
        self.client.force_authenticate(user=self.test_user)
        self.entry = Entry.objects.create(text="Test", owner=self.test_user, by_system=False)
        self.entry.save()
    
    
    def test_get_entries_view(self):
        response = self.client.get(reverse('journal:entry-list'))

        self.assertEqual(response.status_code, 200)
    
    def test_post_entry_view(self):
        data = {
            'text': 'Test Entry Text',
            'owner': self.test_user.pk,
            'by_system': False
        }
        response = self.client.post(reverse('journal:entry-list'), data)

        self.assertEqual(response.status_code, 201)
    

    def test_put_entry_view(self):
        data = {
            'text': 'Edited Test Entry Text',
            'owner': self.test_user.pk,
            'by_system': False
        }
        response = self.client.put(reverse('journal:entry-detail', kwargs={'pk': 1}), data)

        self.assertEqual(response.status_code, 200)

    def test_delete_entry_view(self):
        response = self.client.delete(reverse('journal:entry-detail', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 204)

    
    def tearDown(self):
        self.test_user.delete()
        self.entry.delete()


class TestMiddleware(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.get_or_create(username='TestUser', password='K0n7073$7')[0]
        self.test_user.save()
        self.client.force_authenticate(user=self.test_user)
        self.test_field = Field.objects.create(
            name='Test Field',
            description='test field description',
            review_frequency=4,
            owner=self.test_user
        )
        self.test_field.save()
        self.topic_data = {
            'name': "test topic",
            'description': "test topic description",
            'field': self.test_field.pk,
        }
        self.test_topic = Topic.objects.create(
            name='test topic',
            description='test topic description',
            field=self.test_field
        )
        self.test_topic.save()
    

    def test_create_entry_on_field_methods(self):
        initial_entries = self.client.get(reverse('journal:entry-list')).data
        field_data = {
            'name': 'Test Field',
            'description': 'Test field description',
            'review_frequency': 4,
            'owner': self.test_user.pk,
        }
        self.client.post(reverse('garden:field-list'), field_data)
        entries = self.client.get(reverse('journal:entry-list')).data

        self.assertEqual(len(entries), len(initial_entries) + 1)
        self.assertEqual(entries[-1]['text'], 'New Field was created')

    def test_create_entry_on_topic_revise(self):
        initial_entries = self.client.get(reverse('journal:entry-list')).data
        self.client.get(reverse('garden:topic-revise', kwargs={'field_pk': 1, 'pk': 1}))
        entries = self.client.get(reverse('journal:entry-list')).data

        self.assertEqual(len(entries), len(initial_entries) + 1)
        self.assertEqual(entries[-1]['text'], 'New Revision was created')

    
    def tearDown(self):
        self.test_user.delete()
        self.test_field.delete()
        self.test_topic.delete()