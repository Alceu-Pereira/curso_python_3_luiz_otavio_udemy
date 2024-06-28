import json

caminho_arquivo = 'C:\\Users\\AlceuP\\Desktop\\Cursos\\curso_python_3_luiz_otavio_udemy\\secao_4\\'
caminho_arquivo += 'aula117_json.json'
# pessoa = {
#     'nome': 'Alceu',
#     'sobrenome': 'Pereira',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }


# with open(caminho_arquivo, 'w', encoding='UTF8') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)

with open(caminho_arquivo, 'r', encoding='UTF8') as arquivo:
    pessoa = json.load(arquivo)
print(pessoa['nome'])