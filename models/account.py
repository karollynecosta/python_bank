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

    @property
    def _total_balance_calculate(self: object) -> float:
        return self.balance + self.limit

    def deposit(self: object, value: float) -> None:
        pass

    # withdraw = transferir
    def withdraw(self: object, value: float, destination: object) -> None:
        pass
