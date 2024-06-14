perguntas = [
    {
    'Pergunta': 'Quanto é 2 + 2? ',
     'Opções': ['1', '3', '4', '5'],
     'Resposta': '4',
     },

    {
    'Pergunta': 'Quanto é 5 * 5? ',
     'Opções': ['25', '55', '10', '51'],
     'Resposta': '25',
     },

    {
    'Pergunta': 'Quanto é 10/2? ',
     'Opções': ['4', '5', '2', '1'],
     'Resposta': '5',
     },
]

acertos = erros = 0

for i in range(len(perguntas)):
    print(f'Pergunta: {perguntas[i]['Pergunta']}')
    print(f'\nOpções:')
    for j in range(4):
        if perguntas[i]['Opções'][j] == perguntas[i]['Resposta']:
            resposta_correta = str(j)
        print(f'{j}) {perguntas[i]['Opções'][j]}')


    resposta = input('Escolha uma opção: ')
    
    if resposta == resposta_correta:
        acertos += 1
    else:
        erros += 1

print(f'Você acertou {acertos} perguntas e errou {erros}!')