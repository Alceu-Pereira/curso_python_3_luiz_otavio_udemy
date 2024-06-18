class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def default_user(cls, user='admin', password='admin'):
       instancia = cls()
       instancia.user = user
       instancia.password = password
       return instancia

    @staticmethod
    def log(msg):
        print('log:', msg)

c1 = Connection()
c1.user = 'Alceu'
c1.password = 123
print(c1.user)
print(c1.password)



c2 = Connection.default_user()
print(c2.user)
print(c2.password)


Connection.log('Log')