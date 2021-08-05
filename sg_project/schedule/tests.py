import datetime

from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from rest_framework.test import APIClient, APITestCase

from garden.models import Field, Topic

from .models import Revision
from .views import RevisionViewSet


class TestModel(TestCase):

    def setUp(self):
        self.test_user = User.objects.get_or_create(username='TestUser', password='K0n7073$7')[0]
        self.test_user.save()
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
        self.field.save()
        self.true_rev = Revision.objects.create(
            date=datetime.date(2021, 8, 1),
            field=self.field
        )
        self.true_rev.save()
        self.false_rev = Revision.objects.create(
            date=datetime.date(2020, 12, 31),
            field=self.field
        )
        self.false_rev.save()

    
    def test_is_active(self):
        self.assertEqual(self.true_rev.is_active(), True)
        self.assertEqual(self.false_rev.is_active(), False)
    

    def tearDown(self):
        self.test_user.delete()
        self.field.delete()
        self.true_rev.delete()
        self.false_rev.delete()


class TestRevisionViews(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.get_or_create(username='TestUser', password='K0n7073$7')[0]
        self.test_user.save()
        self.client.force_authenticate(user=self.test_user)
        self.field = Field.objects.create(
            name='Test field',
            description='test test test',
            date_added=datetime.date(2021, 4, 1),
            last_reviewed=datetime.date(2021, 5, 18),
            review_frequency=14,
            owner=self.test_user
        )
        self.field.save()
        self.rev = Revision.objects.create(
            date=datetime.date(2021, 5, 6),
            field=self.field
        )
        self.rev.save()
    

    def test_revision_get_view(self):
        response = self.client.get(reverse('schedule:revision-list'))

        self.assertEqual(response.status_code, 200)
    
    def test_revision_post_view(self):
        data = {
            'date': datetime.date(2021, 8, 1),
            'field': self.field.pk,
        }
        response = self.client.post(reverse('schedule:revision-list'), data)

        self.assertEqual(response.status_code, 201)

    def test_revision_update_view(self):
        data = {
            'date': datetime.date(2021, 9, 12),
            'field': self.field.pk
        }
        response = self.client.put(reverse('schedule:revision-detail', kwargs={'pk': 1}), data)

        self.assertEqual(response.status_code, 200)
    
    def test_revision_delete_view(self):
        response = self.client.delete(reverse('schedule:revision-detail', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 204)
    

    def tearDown(self):
        self.test_user.delete()
        self.field.delete()
        self.rev.delete()



class TestRevisionMixin(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.get_or_create(username='TestUser', password='K0n7073$7')[0]
        self.test_user.save()
        self.client.force_authenticate(user=self.test_user)
        self.field = Field.objects.create(
            name='test field',
            description='test field description',
            review_frequency=3,
            owner=self.test_user,
        )
        self.field.save()
        self.topic = Topic.objects.create(
            name='test topic',
            description='test topic description',
            field=self.field
        )
        self.topic.save()
    

    def test_revise_action(self):
        response = self.client.post(reverse('garden:topic-revise', kwargs={'field_pk': 1, 'pk': 1}))

        self.assertEqual(response.status_code, 200)
    
    def test_revise_creates_revision(self):
        initial_revisions = self.client.get(reverse('schedule:revision-list')).data
        self.client.post(reverse('garden:topic-revise', kwargs={'field_pk': 1, 'pk': 1}))
        revisions = self.client.get(reverse('schedule:revision-list')).data

        revision_date = datetime.date.today() + datetime.timedelta(days=self.field.review_frequency)

        self.assertEqual(len(revisions), len(initial_revisions) + 1)
        self.assertEqual(revisions[-1]['field'], self.field.pk)
        self.assertEqual(revisions[-1]['date'], revision_date.isoformat())


    def tearDown(self):
        self.test_user.delete()
        self.field.delete()
        self.topic.delete()