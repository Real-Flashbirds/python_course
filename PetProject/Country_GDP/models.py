from django.db import models

# Create your models here.


class Region(models.Model):
    """
    Model definition of a bank
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Country(models.Model):
    """
    Model definition of a bank
    """
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=4)
    flag = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class GDP(models.Model):
    """
    Model definition of a bank
    """
    number = models.DecimalField(max_digits=15, decimal_places=0)

    def __str__(self):
        return (f'{self.number}')


class FieldGDP(models.Model):
    GDP = models.ForeignKey(GDP, on_delete=models.CASCADE)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f'In the year {self.year}, the country {self.country} had a GDP of {self.GDP} for a population of ' \
               f'{self.population}, which makes a GPD/PPP of {self.GDP/self.population}'
