from models.client import Client
from models.account import Account

joao: Client = Client('Joao Silva', 'joao@gmail.com',
                      '123.456.789-81', '22/08/99')

print(joao)

joao_account = Account = Account(joao)
print(joao_account)
