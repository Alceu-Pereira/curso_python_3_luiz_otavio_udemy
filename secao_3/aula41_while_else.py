string = 'Alceu Pereira'
i = 0
while i < len(string):
    letra = string[i]
    print(letra)
    i += 1

    if string[i] == ' ':
        break

else:
    print('Não encontrei espaço na STR')

print('Há espaços na str')