def cria_funcao(multiplicador):
    def multiplica(multiplicado):
        return multiplicador * multiplicado
    return multiplica


dobra = cria_funcao(2)
triplica = cria_funcao(3)
quadriplica = cria_funcao(4)

for i in range(3):
    print(dobra(i))
    print(triplica(i))
    print(quadriplica(i))
    print()