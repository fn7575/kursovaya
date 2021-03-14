from django.db import models
import os
from django.contrib.auth.models import User, AbstractUser
from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import datetime
from PIL import Image

class PetOnShow(models.Model):
    class GenderChoice:
        FEMALE = 'female'
        MALE = 'male'

        choices = (
            (FEMALE, 'female'),
            (MALE, 'male'),
        )

    class ShowChoices:
        DOGS = 'dogs'
        CATS = 'cats'
        choices = (
            (DOGS, 'dogs'),
            (CATS, 'cats'),
        )
    alpha = RegexValidator(r'^[a-zA-Zа-яА-я]*$', 'Разрешены только буквенные символы.')

    nick = models.CharField('Кличка', max_length=100,validators=[alpha])
    gender = models.CharField('Пол', max_length=50, choices=GenderChoice.choices, default=GenderChoice.MALE)
    age = models.IntegerField('Возвраст', validators=[MinValueValidator(1), MaxValueValidator(30)])
    breed = models.CharField('Порода', max_length=50,validators=[alpha])
    image = models.ImageField('Фото', upload_to='pets_pics')
    likes = models.ManyToManyField(User, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    info = models.TextField('Информация о питомце', blank=True)
    show = models.CharField(max_length=10, choices=ShowChoices.choices, blank=True, null=True, default=None)
    can_vote_before_date = models.DateTimeField(blank=True, null=True, default=None)
    is_winner = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"
    def __str__(self):
        return self.nick

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length = 200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации', auto_now=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

class Comments(models.Model):
    author_name = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    article = models.ForeignKey(
         Article,
         verbose_name="Статья",
         on_delete=models.CASCADE)
    comment_text = models.TextField("Текст комментария: ")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.comment_text)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


