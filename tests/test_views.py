from django.test import TestCase, Client
from django.urls import reverse
from petshow.models import *
import tempfile
import random

class TestEventList(TestCase):
    def setUp(self):
        user = User.objects.create_user('somename', 'myemail@mail.ru', 'password1122')
        nick = ('Солнце', "Рыжик", "Бобик", "Джеки")
        gender = ('female', "male")
        age = ('1', "2", "3", "4", "5", "6","7")
        breed = ('Порода 1', "Порода 2", "Порода 3", "Порода 4", "Порода 5")
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name        
        info = ('')
        PetOnShow.objects.create(nick='Пушок', gender="male", age="5",
                                   breed="Терьер", image=image, info="",
                                   author_id=user.id)
        for x in range(1, 5000):
            PetOnShow.objects.create(nick=random.choice(nick), gender=random.choice(gender),
                                       age=random.choice(age), breed=random.choice(breed),
                                       image=image, info=info,
                                       user=user.id)