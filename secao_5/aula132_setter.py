class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None


    @property
    def get_cor(self):
        return self._cor
    
    @get_cor.setter
    def get_cor(self, nova_cor):
        self._cor = nova_cor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, nova_cor):
        self._cor_tampa = nova_cor
    
caneta = Caneta('vermelha')
print(caneta.get_cor)

caneta.get_cor = 'rosa'
print(caneta.get_cor)


print(caneta.cor_tampa)


caneta.cor_tampa = 'verde'
print(caneta.cor_tampa)