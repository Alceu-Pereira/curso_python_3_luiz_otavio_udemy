lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
none = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Teste', falsy('Teste'))
print(f'Lista', falsy(lista))
print(f'Dicionario', falsy({}))
print(f'Conjunto', falsy(set()))
print(f'Tupla', falsy(()))
print(f'String', falsy(''))
print(f'Inteiro', falsy(0))
print(f'Flutuante', falsy(0.0))
print(f'None', falsy(None))
print(f'Falso', falsy(False))
print(f'Intervalo', falsy(range(0)))