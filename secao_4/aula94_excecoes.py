try:
    print('Abrindo arquivo')
    # 8 / 0
except ZeroDivisionError:
    print('Dividindo por zero')
else:
    print('Não houveram erros')
finally:
    print('Fechando arquivo')