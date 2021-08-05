import datetime

from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from rest_framework.test import APIClient, APITestCase

from .models import Field, Topic
from .views import FieldViewSet, TopicViewSet



class TestModels(TestCase):

    def setUp(self):
        self.test_user = User.objects.get_or_create(username='TestUser', password='K0n7073$7')[0]
        self.test_user.save()
        date_added = datetime.date(2021, 4, 1)
        last_reviewed = datetime.date(2021, 5, 18)
        self.field1 = Field.objects.create(
            name='Test field',
            description='test test test',
            date_added=date_added,
            last_reviewed=last_reviewed,
            review_frequency=14,
            owner=self.test_user
        )
        self.field1.save()
        self.topic1 = Topic.objects.create(
            name='Test topic',
            description='test test test',
            date_added=date_added,
            last_reviewed=last_reviewed,
            field=self.field1
        )
        self.topic1.save()
    

    def test_field_str(self):
        self.assertEqual(self.field1.__str__(), 'Test field')
    
    def test_field_get_absolute_url(self):
        self.assertEqual(self.field1.get_absolute_url(), '/garden/fields/1/')
    
    def test_field_admin_topic_link(self):
        self.assertEqual(self.field1.admin_topic_filter_link(), '<a href="/admin/garden/topic/?field__id__exact=1">topics</a>')


    def test_topic_str(self):
        self.assertEqual(self.topic1.__str__(), 'Test topic')
    
    def test_topic_get_absolute_url(self):
        self.assertEqual(self.topic1.get_absolute_url(), '/garden/fields/1/topics/1/')
    
    def test_topic_admin_link(self):
        self.assertEqual(self.topic1.admin_field_link(), '<a href="/admin/garden/field/1/change/">Test field</a>')
    

    def tearDown(self):
        self.test_user.delete()
        self.field1.delete()
        self.topic1.delete()



class TestViews(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.get_or_create(username='TestUser', password='K0n7073$7')[0]
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
        self.field.save()
        self.topic.save()
        

    def test_fields_get_view(self):
        response = self.client.get(reverse('garden:field-list'))

        self.assertEqual(response.status_code, 200)
    

    def test_fields_post_view(self):
        data = {
            'name': "test field 2",
            'description': "test description 2",
            'review_frequency': 12,
            'last_reviewed': datetime.date(2021, 7, 25)
        }
        response = self.client.post(reverse('garden:field-list'), data)

        self.assertEqual(response.status_code, 201)
    

    def test_fields_update_view(self):
        data = {
            'name': 'updated name',
            'description': 'updated description',
            'review_frequency': 20
        }
        response = self.client.put(reverse('garden:field-detail', kwargs={ 'pk': 1 }), data)

        self.assertEqual(response.status_code, 200)
    

    def test_fields_delete_view(self):
        response = self.client.delete(reverse('garden:field-detail', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 204)



    def test_topics_get_view(self):
        response = self.client.get(reverse('garden:topic-list', kwargs={'field_pk': 1}))

        self.assertEqual(response.status_code, 200)


    def test_topics_post_view(self):
        data = {
            'name': "test topic 2",
            'description': "test description 2"
        }
        response = self.client.post(reverse('garden:topic-list', kwargs={'field_pk': 1}), data)

        self.assertEqual(response.status_code, 201)

    
    def test_topics_update_view(self):
        data = {
            'name': "updated name",
            'description': 'updated description'
        }
        response = self.client.put(reverse('garden:topic-detail', kwargs={'pk': 1, 'field_pk': 1}), data)

        self.assertEqual(response.status_code, 200)


    def test_topics_delete_view(self):
        response = self.client.delete(reverse('garden:topic-detail', kwargs={'pk': 1, 'field_pk': 1}))

        self.assertEqual(response.status_code, 204)   


    def tearDown(self):
        self.test_user.delete()
        self.field.delete()
        self.topic.delete()