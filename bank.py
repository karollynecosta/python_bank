from typing import List
from time import sleep

from models.client import Client
from models.account import Account

accounts: List[Account] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=============================')
    print('============ATM==============')
    print('=========Python Bank=========')

    print('Select on option:')
    print('1 - Create Account')
    print('2 - Make a withdrawal')
    print('3 - Make a deposit')
    print('4 - Make a tranference')
    print('5 - List accounts')
    print('6 - LogOFF')

    option: int = int(input())

    if option == 1:
        create_account()
    elif option == 2:
        make_withdraw()
    elif option == 3:
        make_deposit()
    elif option == 4:
        make_transference()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print('see you!')
        sleep(2)
        exit(0)
    else:
        print('Please verify the option that you want')
        sleep(2)
        menu()


def create_account() -> None:
    """
    Creat account and add to the list of all accounts
    """
    print('Please enter client data: ')

    name: str = input('Name of the client: ')
    email: str = input('Email of the client: ')
    cpf: str = input('Email of the client: ')
    birth_date: str = input('Birth Date of the client: ')

    client = Client(name, email, cpf, birth_date)

    new_account: Account = Account(client)

    new_account.append(accounts)

    print('Account created with successfull!')
    print('Your Datas: ')
    print('------------')
    print(new_account)
    sleep(2)
    menu()


def make_withdraw() -> None:
    if len(accounts) > 0:
        number: int = int(input('Inform your Account Number: '))

        account: Account = search_account_by_number(number)

        if account:
            value: float = float(input('Informe the withdraw value: '))
            account.withdraw(value)

        else:
            print("Ops, We don't find this Account Number {number}")
    else:
        print('oops, please very if there some account register .-.')
    sleep(2)
    menu()


def make_deposit() -> None:
    if len(accounts) > 0:
        number: int = int(input('Inform your Account Number: '))
        account: Account = search_account_by_number(number)

        if account:
            value: float = float(input('Inform the deposit value: '))
            account.deposit(value)
        else:
            print("Ops, We don't find this Account Number {number}")
    else:
        print('ops, there is some account register here?')
    sleep(2)
    menu()


def make_transference() -> None:
    if len(accounts) > 0:
        number: int = int(input('Inform your Account Number: '))
        account_origin: Account = search_account_by_number(number)

        if account_origin:
            number_destionation_acc: int = int(
                input('What is the destination account? '))
            account_dest: Account = search_account_by_number(
                number_destionation_acc)
            if account_dest:
                value: float = float(input('Inform the tranference value: '))
                account_origin.tranfer(value, account_dest)
            else:
                print('Please, verify the destination account!')
        else:
            print("Ops, We don't find this Account Number {number}")
    else:
        print('ops, there is some account register here?')
    sleep(2)
    menu()


def list_accounts() -> None:
    if len(accounts) > 0:
        print('Listagem de contas')
        for acc in accounts:
            print(acc)
            print('-----------')
            sleep(1)
    else:
        print('ops, there is some account register here?')
    sleep(2)
    menu()


def search_account_by_number(number: int) -> Account:
    c: Account = None

    if len(accounts) > 0:
        for acc in accounts:
            if acc.number == number:
                c = acc
    return c


if __name__ == '__main__':
    main()
