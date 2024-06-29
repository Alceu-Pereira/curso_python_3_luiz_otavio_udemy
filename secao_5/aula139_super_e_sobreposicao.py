# class MinhaString(str):
#     def upper(self):
#         return super(MinhaString, self).upper()


# string = MinhaString('Alceu')
# print(string.upper())

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def metodo(self):
        super(B, self).metodo()
        A.metodo(self)
        B.metodo(self)
        print('C')


c = C('atributo_a', 'Outra')
c.metodo()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
print(C.mro())