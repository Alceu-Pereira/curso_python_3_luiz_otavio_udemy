class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando


    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando')
            return

        print(f'{self.nome} está filmando')
        self.filmando = True

    def parar_filmar(self):
        if self.filmando:
            print('Parando de filmar')
            self.filmando = False
            return
        print('A câmera não está filmando')

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar')
            return
        
        print(f'{self.nome} está fotografando')

c1 = Camera('Camera 1')
c2 = Camera('Camera 2')
c1.filmar()
c1.parar_filmar()
c1.fotografar()
