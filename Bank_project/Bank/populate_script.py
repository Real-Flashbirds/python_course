import datetime
import random
import time

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Bank_project.Bank.settings")

import django
django.setup()

from banks.models import Client, Bank, Branch, Account

def populate():
    b = Bank(name='RABO', number=1, country='NL')
    b.save()
    br = Branch(bank=b, city='Eindhoven')
    br.save()
    c = Client(branch=Branch.objects.first(), name='(enter your name here)', birthday='1990-01-01')
    c.save()
    a = Account(client=Client.objects.first(), branch=Branch.objects.first(), balance=10000, max_withdrawal=2000, max_debt=2000)
    a.save()
    #one additional bank
    b2 = Bank(name='Revolut', number=2, country='NL')
    b2.save()
    #3 branches per bank
    br2 = Branch(bank=b, city='Amsterdam')
    br2.save()
    br3 = Branch(bank=b, city='Rotterdam')
    br3.save()
    br4 = Branch(bank=b2, city='Vilnius')
    br4.save()
    br5 = Branch(bank=b2, city='Eindhoven')
    br5.save()
    br5 = Branch(bank=b2, city='London')
    br5.save()
    #10 clients per branch
    for branch in Branch.objects.all():
        for n in range(10):
            rand_birth_date = random_date()
            rand_name = str(random.randint(0,1000000)) #They are robots and are called by numbers
            my_new_client = Client(branch=branch, name=rand_name, birthday=rand_birth_date)
            my_new_client.save()
    # 1 accoutn per client
    for client in Client.objects.all():
        account = Account(client=client, branch=client.branch, balance=random.randint(0, 1000000), max_withdrawal=2000,
                          max_debt=2000)
        account.save()


def random_date():
    d = random.randint(1, int(time.time()))
    return datetime.date.fromtimestamp(d).strftime('%Y-%m-%d')

if __name__ == "__main__":
    populate()