def gen_1(start, end):
    for i in range(start, end):
        yield i


def gen_2(start, end):
    yield from gen_1(start, end)
    for i in range(end, end + 15):
        yield i
        

generator = gen_2(0, 3)
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())