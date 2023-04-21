from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


def upload_to_images(instance, filename):
    return 'zeon/images/%s' % filename

# Create your models here.
class Computers(models.Model):
    cpu = models.CharField('Процессор', max_length=255, null=False, blank=False, unique=True)
    gpu = models.CharField('Видеокарта', max_length=255, null=True, unique=True)
    operativka = models.CharField('Оперативная память', max_length=255, null=True, unique=True)
    mother=models.CharField('Материнская плата', max_length=255, null=True, unique=True)
    ssd=models.CharField('ССД', max_length=255, null=True, unique=True)
    hdd=models.CharField('Жесткий диск', max_length=255, null=True, unique=True)
    corpus=models.CharField('Корпус', max_length=255, null=True, unique=True)
    perifiria=models.CharField('Периферия', max_length=255, null=True, unique=True)
    image = models.ImageField('Изображение', null=True, blank=True, db_index=True, upload_to=upload_to_images)

    def photo_tag(self):
        return mark_safe('<img src="%s" width="70" height="70" />' % self.image.url)

    def __str__(self):
        return self.corpus


    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'

class Tarifs(models.Model):
    nazvanie = models.CharField('Название', max_length=255, null=False, blank=False, unique=True)
    opisanie = models.CharField('Описание', max_length=255, null=True, unique=True)
    price = models.CharField('Цена', max_length=255, null=True, unique=True)
    image = models.ImageField('Изображение', null=True, blank=True, db_index=True, upload_to=upload_to_images)

    def photo_tag(self):
        return mark_safe('<img src="%s" width="70" height="70" />' % self.image.url)

    def __str__(self):
        return self.nazvanie

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'