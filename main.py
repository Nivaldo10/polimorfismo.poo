from carro_inteligente import CarroInteligente
from carro_esportivo import CarroSportivo
from carro_corrida import CarroCorrida

def test_drive(carro):
    print(f"\nTestando {carro.__class__.__name__}:")
    carro.acelera()
    carro.exibe_velocidade()

if __name__ == "__main__":
    # Testando CarroInteligente
    carro_inteligente = CarroInteligente(10)
    carro_inteligente.estaciona()
    test_drive(carro_inteligente)

    #Testando CarroSportivo
    carro_esportivo = CarroSportivo(50)
    carro_esportivo.turbo()
    test_drive(carro_esportivo)

    carro_corrida = CarroCorrida(100)
    test_drive(carro_corrida)
