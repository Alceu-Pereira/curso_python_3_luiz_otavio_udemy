x = 1

def escopo():
    x = 10

    def outra_funcao():
        global y
        x = 12
        y = 2
        print(x, y)
    outra_funcao()
    print(x)

print(x)
escopo()

print(x)