from django.test import TestCase
from django.urls import reverse

from animals.models import Animal


class AnimalModelTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')


class AnimaViewsTestCase(TestCase):
    def test_animal_homepage(self):
        response = self.client.get(reverse("animals:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Animal list</h1>")
