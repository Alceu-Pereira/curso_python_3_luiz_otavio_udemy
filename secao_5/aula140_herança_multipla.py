class A:
    ...
    def eu_sou(self):
        print('A')

class B:
    ...
    # def eu_sou(self):
    #     print('B')

class C(B, A):
    ...
    # def eu_sou(self):
    #     print('C')

c = C()
print(C.mro())