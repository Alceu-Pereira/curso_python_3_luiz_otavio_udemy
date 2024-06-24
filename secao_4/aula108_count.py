from itertools import count

meu_contador = count(10, 2)
range_contador = range(10, 30, 2)

print('Count')
for i in meu_contador:
    print(i)

    if i == 30:
        break

print('Range')
for j in range_contador:
    print(j)