import random

lista_de_cpfs = []

while len(lista_de_cpfs) < 10:
    cpf = ''
    for i in range(11):
        cpf += str(random.randint(0, 9))

    contagem = 10
    soma = 0

    for i in range(0, 9):
        soma += (int(cpf[i]) * contagem)
        contagem -= 1

    multiplica_soma = soma * 10
    resto_por_11 = multiplica_soma % 11
    primeiro_digito = 0 if resto_por_11 > 9 else resto_por_11

    soma = 0
    contagem_2 = 11

    for i in range(0, 10):
        soma += (int(cpf[i]) * contagem_2)
        contagem_2 -= 1

    multiplica_soma = soma * 10
    resto_por_11 = multiplica_soma % 11
    segundo_digito = 0 if resto_por_11 > 9 else resto_por_11

    cpf_calculado = f'{cpf[:9]}{primeiro_digito}{segundo_digito}'

    if cpf_calculado == cpf:
        lista_de_cpfs.append(cpf)

for i in lista_de_cpfs:
    print(i)