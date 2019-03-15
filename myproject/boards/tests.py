# from django.test import TestCase

# Create your tests here.

# below copied from tutorial
'''
from django.core.urlresolvers import reverse
from django.test import TestCase

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
'''
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, donationsinfo
from .models import Donor

class HomeTests(TestCase):
    def setUp(self):
        # this needs to be fixed
        self.item = Item.objects.create(warehousenum ='00081', invoicenum='2019010220', manufacturer = 'Google', item_type = 'Laptop')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        donationsinfo_url = reverse('donations_info', kwargs={'pk': self.item.pk})
        self.assertContains(self.response, 'href="{0}"'.format(donationsinfo_url))


class BoardTopicsTests(TestCase):
    def setUp(self):
        # needs to be fixed
        Item.objects.create(warehousenum ='00081', invoicenum='2019010220', manufacturer = 'Google', item_type = 'Laptop')

    def test_board_topics_view_success_status_code(self):
        url = reverse('donationsinfo', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('donationsinfo', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, donationsinfo)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        donationsinfo_url = reverse('donationsinfo', kwargs={'pk': 1})
        response = self.client.get(donationsinfo_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))
