cpf = '74682489070'
contagem = 10
soma = 0

for i in range(0, 9):
    soma += (int(cpf[i]) * contagem)
    contagem -= 1

multiplica_soma = soma * 10
resto_por_11 = multiplica_soma % 11
primeiro_digito = 0 if resto_por_11 > 9 else resto_por_11
print(primeiro_digito)