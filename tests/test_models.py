from django.test import TestCase
from petshow.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import datetime

class AuthTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

    def test_authenticate(self):
        auth_user = authenticate(username='myusername', password='mypassword')
        self.assertTrue(auth_user is not None and auth_user.is_authenticated)

    def test_wrong_password(self):
        auth_user = authenticate(username='myusername', password='mypad')
        self.assertFalse(auth_user is not None and auth_user.is_authenticated)

    def tearDown(self):
        self.user.delete()