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
from .views import home, donations_info
from .models import Item

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
        donations_info_url = reverse('donations_info', kwargs={'pk': self.item.pk})
        self.assertContains(self.response, 'href="{0}"'.format(donations_info_url))


class BoardTopicsTests(TestCase):
    def setUp(self):
        # needs to be fixed
        Item.objects.create(warehousenum ='00081', invoicenum='2019010220', manufacturer = 'Google', item_type = 'Laptop')

    def test_board_topics_view_success_status_code(self):
        url = reverse('donations_info', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('donations_info', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, donations_info)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        donations_info_url = reverse('donations_info', kwargs={'pk': 1})
        response = self.client.get(donations_info_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
