def criar_funcao(funcao):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        return funcao(*args, **kwargs)
    return interna

def inverte_string(string):
    return string[::-1]

def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError(f'{parametro} deve ser str')

funcao_checa = criar_funcao(inverte_string)
invertida = funcao_checa(155)
print(invertida)