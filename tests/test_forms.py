from django.test import TestCase
from petshow.forms import *

class TestForms(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('TestUser', 'kostya.petrov@mail.ru', 'john')

    def test_FormComment(self):
        form = CommentForm(self.user, data={
            'article': '1',
            'author_name': self.user.id,
            'comment_text': 'Спасибо, хорошая статья!'
        })
        status = form.is_valid()
        self.assertTrue(status)

    def test_ContactForm(self):
        form = ContactForm(data={
            'subject': 'Не могу зарегистрироваться',
            'email': 'petya.ivanov@gmail.com',
            'message': 'Здравствуйте, не могу зарегистрироваться, выдает ошибку.'
        })
        status = form.is_valid()
        self.assertTrue(status)