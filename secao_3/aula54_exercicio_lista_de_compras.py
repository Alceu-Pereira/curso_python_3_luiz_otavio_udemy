lista_de_compras = []

while True:

    options = str(input('Selecione uma opção\n [i]nserir [a]pagar [l]istar: ')).lower()

    if options in 'ial':
    
        if options == 'i':
            item = str(input('Insira um item: ')).capitalize()
            lista_de_compras.append(item)

        if options == 'a':
            apagar = int(input('Escolha um índice para apagar: '))
            if not lista_de_compras:
                print('A lista está vazia.')
                continue
            try:           
                lista_de_compras.pop(apagar)
            
            except IndexError:
                print('O índice indicado não existe.')

        if options == 'l':
            if not lista_de_compras:
                print('A lista está vazia.')
            else:
                for i, v in enumerate(lista_de_compras):
                    print(i, v)
    
    else:
        print('Escolha uma opção válida')