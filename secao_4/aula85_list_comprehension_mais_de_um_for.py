# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))

# print(lista)

lista = [
    (i, j)
    for i in range(3)
    for j in range(3)
]

print(lista)