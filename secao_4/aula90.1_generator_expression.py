import sys

iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable)
generator = (n for n in range(10000))
lista = [n for n in range(10000)]

print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

for i in generator:
    print(i) if i < 5000 else None