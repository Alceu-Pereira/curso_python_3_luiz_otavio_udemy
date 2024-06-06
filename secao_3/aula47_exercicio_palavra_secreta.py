palavra_secreta = 'Teste'
palavra_formada = len(palavra_secreta) * '*'
tentativas = 0

while palavra_secreta != palavra_formada:
    chute = str(input('Digite uma letra: '))

    if chute in palavra_secreta:
        for i in palavra_secreta:
            ...


    print(f'Palavra formada: {palavra_formada}')

