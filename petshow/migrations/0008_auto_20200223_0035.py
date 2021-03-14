# Generated by Django 2.1.14 on 2020-02-22 21:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petshow', '0007_petonshow_is_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=200, verbose_name='текст комментария:'),
        ),
        migrations.AlterField(
            model_name='petonshow',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Возвраст'),
        ),
        migrations.AlterField(
            model_name='petonshow',
            name='breed',
            field=models.CharField(max_length=50, verbose_name='Порода'),
        ),
        migrations.AlterField(
            model_name='petonshow',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male')], default='male', max_length=50, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='petonshow',
            name='image',
            field=models.ImageField(upload_to='pets_pics', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='petonshow',
            name='info',
            field=models.TextField(blank=True, verbose_name='Информация о питомце'),
        ),
        migrations.AlterField(
            model_name='petonshow',
            name='nick',
            field=models.CharField(max_length=100, verbose_name='Кличка'),
        ),
    ]