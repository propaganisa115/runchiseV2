import pytest as pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Restaurant
from django.test import TestCase
from django.template.defaultfilters import slugify

class ModelsTestCase(TestCase):
    def test_Restaurant(self):
        rs = Restaurant.objects.create(name="runchise", address="sarijadi blok 2",phone_number="4343243", email="runchise@gmail.com")
        rs.save()
        self.assertEqual(rs.name, "runchise")