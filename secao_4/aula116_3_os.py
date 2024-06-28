import os

caminho_arquivo = 'C:\\Users\\AlceuP\\Desktop\\Cursos\\curso_python_3_luiz_otavio_udemy\\secao_4\\'
caminho_arquivo +=  'aula116_3.txt'

with open(caminho_arquivo, 'w+', encoding='UTF-8') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Ãáà\n')
    arquivo.writelines(
        [f'{str(n)}\n' for n in range(5)]
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    

os.rename(caminho_arquivo, 'C:\\Users\\AlceuP\\Desktop\\Cursos\\curso_python_3_luiz_otavio_udemy\\secao_4\\aula116teste.txt')