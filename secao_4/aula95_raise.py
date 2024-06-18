# print(123)
# raise ValueError('Erro de valor')
# print(456)

def divide(n, d):
    # try:
    #     return n / d
    # except ZeroDivisionError:
    #     print('___________')
    #     raise
    if not isinstance(d, (int, float)):
        raise TypeError(f'{d} precisa ser do tipo int ou float')


    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero.')
    return n / d

print(divide(8, 'd'))