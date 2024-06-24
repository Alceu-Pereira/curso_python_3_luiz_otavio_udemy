class Foo:
    def __init__(self):
        self.public = 'Isto é público'
        self._protected = 'Isto é protegido'
        self.__private = 'Isto é privado'

    def metodo_publico(self):
        return 'Método público'
    
    def _metodo_protegido(self):
        return 'Método protegido'

f = Foo()
print(f.public)
print(f.metodo_publico())
print()
print(f._Foo__private)


