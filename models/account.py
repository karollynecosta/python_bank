from models.client import Client
from utils.helper import format_float_to_str_moeda


class Account:
    code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__number: int = Account.code
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total_balance: float = self._total_balance_calculate
        Account.code += 1

    def __str__(self: object) -> str:
        return f'Account number: {self.number} \nClient: {self.client.name} \nTotal Balance: {format_float_to_str_moeda(self.total_balance)}'

    @property
    def number(self: object) -> int:
        return self.__number

    @property
    def client(self: object) -> Client:
        return self.__client

    @property
    def balance(self: object) -> float:
        return self.__balance

    @balance.setter
    def balance(self: object, value: float) -> None:
        self.__balance = value

    @property
    def limit(self: object) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def total_balance(self: object) -> float:
        return self.__total_balance

    @total_balance.setter
    def total_balance(self: object, value: float) -> None:
        self.__total_balance = value

    @property
    def _total_balance_calculate(self: object) -> float:
        return self.balance + self.limit

    def deposit(self: object, value: float) -> None:
        if value > 0:
            self.balance = self.balance + value
            self.total_balance = self._total_balance_calculate
            print(f'Deposit of {value} successfully finished!')
        else:
            print('The value must be more than 0, try again!')

    # withdraw = sacar
    def withdraw(self: object, value: float) -> None:
        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._total_balance_calculate
            else:
                rest: float = self.balance - value  # negative value
                self.limit = self.limit + rest
                self.balance = 0
                self.total_balance = self._total_balance_calculate
                print(
                    'You are consuming your limit, but withdraw successfully finished!')
        else:
            print('Withdraw failed. Try again!')

    def tranfer(self: object, value: float, destination: object) -> None:
        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._total_balance_calculate
                destination.balance = destination.balance + value
                destination.total_balance = destination._total_balance_calculate
            else:
                rest: float = self.balance - value  # negative value
                self.balance = 0
                self.limit = self.limit + rest
                self.total_balance = self._total_balance_calculate
                destination.balance = destination.balance + value
                destination.total_balance = destination._total_balance_calculate
                print('Your do not have limit to this transfer')
        else:
            print('Ops, something wrog with your transference!')
