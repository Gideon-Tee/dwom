from tokenize import String
from unicodedata import category

from django.test import TestCase
from item.models import Item
from django.contrib.auth.models import User
from datetime import datetime


# Create your tests here.
class TestLogin(TestCase):
    def test_login_page(self):
        self.assertTrue(True)


class TestItem(TestCase):

    def test_item_parameters(self):
        item1 = Item(
            name = "Laptop",
            price = 3500,
            # created_by = User.objects.get(username="gideon"),
            created_at = datetime.now()
        )

        self.assertTrue(item1.__str__() == item1.name)
