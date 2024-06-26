from sys import setrecursionlimit

setrecursionlimit(1002)

def fatorial(number):

    if number <= 1:
        return number
    
    return number * (fatorial(number - 1))


print(fatorial(1001))