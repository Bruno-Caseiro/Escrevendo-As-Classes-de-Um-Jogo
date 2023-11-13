class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo.lower() == 'mago':
            ataque = 'usou magia'
        elif self.tipo.lower() == 'guerreiro':
            ataque = 'usou espada'
        elif self.tipo.lower() == 'monge':
            ataque = 'usou artes marciais'
        elif self.tipo.lower() == 'ninja':
            ataque = 'usou shuriken'
        else:
            ataque = 'usou um ataque indefinido'

        print(f"O {self.tipo} {self.nome} atacou usando {ataque}")

heroi1 = Heroi("Tristan", 30, "Guerreiro")
heroi2 = Heroi("Harry", 200, "Mago")

heroi1.atacar()
heroi2.atacar()