from banks.models import Account, Client, Branch
import datetime


def compute_wealthy():
    age_group = [0, 0, 0, 0]
    wealth_group = [0, 0, 0, 0]
    for account in Account.objects.all():
        if account.balance > 600000:
            # we consider 600000 to be rich
            client = account.client
            client_age = age(client.birthday)
            # Could be done in a cleaner way using class to filter client, but too lazy
            if client_age < 20:
                age_group[0] += 1
                wealth_group[0] += account.balance
            elif client_age < 40:
                age_group[1] += 1
                wealth_group[1] += account.balance
            elif client_age < 60:
                age_group[2] += 1
                wealth_group[2] += account.balance
            else:
                age_group[3] += 1
                wealth_group[3] += account.balance
    if age_group[0] > 0:
        print(f'There are {age_group[0]} wealthy people younger than 20 '
              f'and they possess {wealth_group[0]/age_group[0]} euros in average')
    else:
        print(f'There are no wealthy people younger than 20 ')
    if age_group[1] > 0:
        print(
            f'There are {age_group[1]} wealthy people between 20 '
            f'and 40 and they possess {wealth_group[1] / age_group[1]} euros in average')
    else:
        print(f'There are no wealthy people between 20 and 40 ')
    if age_group[2] > 0:
        print(
            f'There are {age_group[2]} wealthy people between 40 '
            f'and 60 and they possess {wealth_group[2] / age_group[2]} euros in average')
    else:
        print(f'There are no wealthy people between 40 and 60 ')
    if age_group[3] > 0:
        print(
            f'There are {age_group[3]} wealthy people older '
            f'than 60 and they possess {wealth_group[3] / age_group[3]} euros in average')
    else:
        print(f'There are no wealthy people older than 60 ')

def notify_branches():
    for branch in Branch.objects.all():
        clients_gold = []
        clients_silver = []
        for account in Account.objects.all():
            if account.branch == branch:
                if account.balance > 600000:
                    clients_gold.append([account.client, account.balance])
                elif account.balance > 500000:
                    clients_silver.append([account.client, account.balance])
        if clients_gold:
            print(f'Hi Branch {branch.bank.name} from {branch.city}, you have {len(clients_gold)} potential gold '
                  f'clients who are :')
            for client in clients_gold:
                print(f'name: {client[0]}    balance: {client[1]}')
        if clients_silver:
            print(f'Hi Branch {branch.bank.name} from {branch.city}, you have {len(clients_silver)} potential silver '
                  f'clients who are :')
            for client in clients_silver:
                print(f'name: {client[0]}    balance: {client[1]}')


def age(birthday):
    today = datetime.date.today()
    years = today.year - birthday.year
    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        years -= 1
    return years