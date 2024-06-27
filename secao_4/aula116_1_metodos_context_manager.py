caminho_arquivo = 'C:\\Users\\AlceuP\\Desktop\\Cursos\\curso_python_3_luiz_otavio_udemy\\secao_4\\'
caminho_arquivo +=  'aula116_1_metodos_context_manager.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        [f'{str(n)}\n' for n in range(5)]
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    arquivo.seek(0, 0)
    
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha, end='')

# with open(caminho_arquivo, 'r') as arquivo:
#     ...