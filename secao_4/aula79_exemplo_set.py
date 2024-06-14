letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra)

    if 'l' in letras:
        break

    print(letras)