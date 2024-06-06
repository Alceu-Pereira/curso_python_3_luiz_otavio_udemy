texto = 'Alceu'
iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

for i in texto:
    print(i)
