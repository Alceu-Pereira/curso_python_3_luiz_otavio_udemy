import time

def decoradora(func):
    def aninhada(*args, **kwargs):
        print(f'Decorando a função {func.__name__}...')
        time.sleep(2)
        resultado = func(*args, **kwargs)
        print(f'Função {func.__name__} decorada!')
        time.sleep(2)
        return resultado
    return aninhada

# @decoradora
def soma(x, y):
    return x + y



dez_vezes_cinco = decoradora(lambda x, y: x * y)
dez_mais_cinco = decoradora(soma)
print(dez_mais_cinco(10, 5))
print(dez_vezes_cinco(10, 5))