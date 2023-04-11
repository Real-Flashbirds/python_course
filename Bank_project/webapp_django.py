from django.db import models


class Bank(models.Model):
    """
    Model definition of a bank
    """
    name = models.CharField(max_length=100)
    number = models.DecimalField(max_digits=8, decimal_places=0)
    country = models.CharField(max_length=100)

    def __str__(self):
        return (f'{self.name}, {self.country}')


class Branch(models.Model):
    """
    Model definition of a bank branch
    """
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)


class Client(models.Model):
    """
    Model definition of a client
    """
    name = models.CharField(max_length=100)
    birthday = models.DateField()


class Account(models.Model):
    """
    Model definition of a bank account
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    max_withdrawal = models.DecimalField(max_digits=8, decimal_places=2)
    max_debt = models.DecimalField(max_digits=8, decimal_places=2)
