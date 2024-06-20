def dec_param(nome):

    def decorador(func):

        def aninhanada(*args, **kwargs):
            resultado = func(*args, **kwargs)

            return resultado, f'{nome}'
        
        return aninhanada

    return decorador

@dec_param(nome='terceiro')
@dec_param(nome='segundo')
@dec_param(nome='primeiro')
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)