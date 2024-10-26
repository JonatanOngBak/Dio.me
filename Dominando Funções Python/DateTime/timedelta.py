"""import datetime

# Criando data e hora
data = datetime.datetime(2024, 10, 24, 8, 5)
print(data)

# Adicionando uma semana
data = data + datetime.timedelta(weeks=1)
print(data)
"""
from datetime import datetime, timedelta

# exemplo de um lava jato.

tipo_carro = 'M'  # "P", "M", "G"
carro_P = 30
carro_M = 45
carro_G = 60
data_atual = datetime.now()
data_atual_BR = "%H:%M, %d/%m/%Y"

if tipo_carro == 'P':
    estimativa = data_atual + timedelta(minutes=carro_P)
    print(f'O carro entrou as {data_atual.strftime(data_atual_BR)} e ficará pronto as {estimativa.strftime(data_atual_BR)}')
    
elif tipo_carro == 'M':
    estimativa = data_atual + timedelta(minutes=carro_M)
    print(f'O carro entrou as {data_atual.strftime(data_atual_BR)} e ficará pronto as {estimativa.strftime(data_atual_BR)}')
else:
    estimativa = data_atual + timedelta(minutes=carro_G)
    print(f'O carro entrou as {data_atual.strftime(data_atual_BR)} e ficará pronto as {estimativa.strftime(data_atual_BR)}')



