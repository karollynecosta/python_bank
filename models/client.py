from datetime import date
from utils.helper import date_to_string, string_to_date


class Client:
    contador: int = 101

    # Register of the client
    def __init__(self: object, name: str, email: str, cpf: str, birth_date: str) -> None:
        self.__code: int = Client.contador
        self.__name: str = name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__birth_date: date = string_to_date(birth_date)
        self.__register_date: date = date.today()
        Client.contador += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def birth_date(self: object) -> str:
        return date_to_string(self.__birth_date)

    @property
    def register_date(self: object) -> str:
        return date_to_string(self.__register_date)

    def __str__(self: object) -> str:
        return f'Code: {self.code} \nNome: {self.name} \nBirth Date: {self.birth_date} \nRegister Date: {self.register_date}'
