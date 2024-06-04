user_number = int(input('Digite um número inteiro: '))
if user_number % 2 == 0:
    print(f'O número {user_number} é par')
else:
    print(f'O número {user_number} é ímpar')

user_hour = int(input('Que horas são? [0 - 23] '))

if user_hour in range(0, 12):
    print('Bom dia!')
elif user_hour in range(12, 18):
    print('Boa tarde!')
elif user_hour in range(18, 24):
    print('Boa noite!')
else:
    print('Horário não corresponde as opções')

user_name = str(input('Digite o seu nome: '))

if len(user_name) <= 4:
    print('Seu nome é curto')
elif 5 <= len(user_name) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')