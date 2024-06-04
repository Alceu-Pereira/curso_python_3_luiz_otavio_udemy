contador = 0

while contador < 100:
    contador += 1
    
    if contador >= 6 and contador <= 20:
        continue

    if contador == 40:
        break

    print(contador)
    
    