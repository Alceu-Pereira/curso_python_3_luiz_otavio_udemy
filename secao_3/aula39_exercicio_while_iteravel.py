nome = 'Alceu Pereira'
nova_str = ''
tamanho_nome = len(nome)
indice_nome = 0

while indice_nome < tamanho_nome:
    nova_str += f'*{nome[indice_nome]}'
    indice_nome += 1

nova_str += '*'
print(nova_str)