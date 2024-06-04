while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')

    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
    except ValueError:
        print('Digite apenas números do tipo float')
        continue

    operadores_validos = '+-/*'
    operador = input('Digite o operador (+ - / *): ')
    while operador[0] not in operadores_validos:
       operador = input('Operador inválido.\n Digite um operador válido (+ - / *): ')

    if operador == '+':
        print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')
    elif operador == '-':
        print(f'{numero_1} - {numero_2} = {numero_1 - numero_2}')
    elif operador == '*':
        print(f'{numero_1} x {numero_2} = {numero_1 * numero_2}')
    else:
        print(f'{numero_1} / {numero_2} = {numero_1 / numero_2}')

    sair = input('Deixa sair? [s]im: ').lower()

    if sair == 's':
        break