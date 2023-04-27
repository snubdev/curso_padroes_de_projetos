class Singleton:

    __instace = None

    def __init__(self):
        if not Singleton.__instace:
            print('O método __init__ foi chamado...')
        else:
            print(f'A instância já foi criada: {self.get_instance()}')

    @classmethod
    def get_instance(cls):
        if not cls.__instace:
            cls.__instace = Singleton()
        return cls.__instace


s1 = Singleton()  # A classe é inicializada, mas o objeto não é criado
print(f'Objeto criado agora: {Singleton.get_instance()}')

s2 = Singleton()  # Instância já criada