def generator(start, end):
    for i in range(start, end + 1):
        yield i
    return 'Acabou'

gen = generator(0, 10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))