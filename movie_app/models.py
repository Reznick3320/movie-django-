from locale import currency
from django.db import models
from django.urls import reverse

# Create your models here.

class Movie(models.Model):

    EUR = 'EUR'
    USD = 'USD'
    UAH = 'UAH'

    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (UAH, 'UAH'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=UAH)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])
        # return reverse('movie_detail', args=[self.id])

    def __str__(self):
        return f'{self.name} - {self.rating}%'