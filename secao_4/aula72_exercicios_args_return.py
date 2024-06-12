def multiplica(*args):
    total = 1
    for i in args:
        total *= i
    return total

print(multiplica(1, 2, 3, 4, 5))

def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'par'
    return 'impar'
    
print(par_ou_impar(3))