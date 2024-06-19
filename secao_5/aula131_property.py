class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta
    # def get_cor(self):
    #     print('GET COR')
    #     return self.tinta

    @property
    def cor_tampa(self):
        print('Cor tampa')

####################################

caneta = Caneta('azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
caneta.cor_tampa
