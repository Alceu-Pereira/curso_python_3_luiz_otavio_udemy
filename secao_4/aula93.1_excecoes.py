a = 18
b = 'k'

try:
    c = a / b
except ZeroDivisionError:
    print('Dividiu por zero.')

except NameError as name_error:
    print(f'Falta definir a variável {name_error.name}')

except Exception:
    print('Erro desconhecido')