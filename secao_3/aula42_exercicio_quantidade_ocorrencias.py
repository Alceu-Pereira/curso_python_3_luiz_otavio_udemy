string = 'O Python é uma linguagem de programação multiparadigma criada por Guido van Rossum.'.lower()

string_2 = 'AAAAABbBBBBBB'.lower()

i = 0
maior = 0
letra_maior = ''

while i < len(string_2):
    if string_2[i] != ' ':
        letra_atual = string_2[i]
        contar_letra_atual = string_2.count(letra_atual.lower())
        
        if maior <= contar_letra_atual:
            maior = contar_letra_atual
            letra_maior = letra_atual

    i += 1


print(f'A letra "{letra_maior}" teve mais ocorrências aparecendo {maior} vezes na frase')

 
