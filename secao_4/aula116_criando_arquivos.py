caminho_arquivo = 'C:\\Users\\AlceuP\\Desktop\\Cursos\\curso_python_3_luiz_otavio_udemy\\secao_4\\'
caminho_arquivo += 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo!')
    print('Arquivo será fechado.')