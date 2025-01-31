from carro import Carro

class CarroSportivo(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)

    def turbo(self):
        self.velocidade += 10
        print("Turbo ativado! a velocidade almentou em 10 km/h")