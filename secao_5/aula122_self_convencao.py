class Carro:
    def __init__(outra_coisa, nome):
        outra_coisa.nome = nome
        
    def acelerar(outra_coisa):
        print(f'{outra_coisa.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
Carro.acelerar(Carro('Fusca'))
