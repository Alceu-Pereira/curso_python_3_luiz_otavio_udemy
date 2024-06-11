def soma(x, y, z=None):
    if z is not None:
        print(x + y + z)
    else:
        print(x + y)


soma(1, 2, 3)
soma(10, 23)
soma(100, 200)
soma(z=3, y=2, x=1)