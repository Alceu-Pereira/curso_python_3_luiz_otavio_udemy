a = 18
b = 'k'

try:
    c = a / b
except ZeroDivisionError:
    print('Dividiu por zero.')

except NameError:
    print(f'Falta uma variável')

except Exception:
    print('Erro desconhecido')