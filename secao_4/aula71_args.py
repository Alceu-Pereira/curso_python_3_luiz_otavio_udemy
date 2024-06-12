x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for i in args:
        total += i
    return total

print(soma(x, y, *resto))
numeros = 1, 2, 3, 4, 5
print(soma(*numeros))

