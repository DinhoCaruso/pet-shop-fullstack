from pessoa import Pessoa
from carro import Carro

p = Pessoa()
c = Carro()

p.dirige(c)

class Pessoa:
    def dirige(self, carro):
        carro.acelera()
        carro.freia()

class Carro:
    def acelera(self):
        print('Acelerando...')

    def freia(self):
        print('freiando...')
















