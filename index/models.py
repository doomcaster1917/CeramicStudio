from django.db import models

class WorkingHours(models.Model):

    start_time = models.TimeField('Время начала', unique=True)
    end_time = models.TimeField('Время окончания', unique=True)

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'

    class Meta:
        verbose_name = 'Время работы'
        verbose_name_plural = 'Время работы'

class PhoneNumber(models.Model):
    phone_number = models.CharField('Телефонный номер', max_length=50)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Телефонный номер'
        verbose_name_plural = 'Телефонные номера'

class OurWorks(models.Model):

    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=250)
    image = models.ImageField(upload_to='files/', null=True)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Наши работы'

class ServicesAndPrices(models.Model):

    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=250)
    image = models.ImageField(upload_to='files/', null=True)
    price = models.IntegerField('Цена', null=True, max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'