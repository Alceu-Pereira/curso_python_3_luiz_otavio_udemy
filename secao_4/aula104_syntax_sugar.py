def criar_funcao(funcao):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        return funcao(*args, **kwargs)
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError(f'{parametro} deve ser str')

invertida = inverte_string('155')
print(invertida)