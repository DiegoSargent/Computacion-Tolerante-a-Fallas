import threading
import random
import time

class Caballo(threading.Thread):
    def __init__(self, nombre, apuesta_numero, distancia_total):
        super().__init__()
        self.nombre = nombre
        self.distancia_recorrida = 0
        self.velocidad = random.randint(1, 5)
        self.apuesta_numero = apuesta_numero
        self.distancia_total = distancia_total

    def run(self):
        while self.distancia_recorrida < self.distancia_total:
            self.distancia_recorrida += self.velocidad
            print(f"{self.nombre} ha recorrido {self.distancia_recorrida} metros.")
            time.sleep(1)  # Simula el tiempo de carrera

def revisar_estado(caballos):
    while True:
        time.sleep(2)  # Revisa el estado cada 2 segundos
        for caballo in caballos:
            print(f"Estado de {caballo.nombre}: {caballo.distancia_recorrida} metros.")

def simulador_carrera(caballos, apuesta_numero):
    hilos = []
    for i, caballo in enumerate(caballos):
        hilo = Caballo(f"Caballo {i + 1}", apuesta_numero, 100)
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    ganador = max(caballos, key=lambda x: x.distancia_recorrida)

    if ganador.apuesta_numero == apuesta_numero:
        print(f"¡Has ganado! {ganador.nombre} ha ganado la carrera.")
    else:
        print(f"Lo siento, {ganador.nombre} ha ganado la carrera.")

if __name__ == "__main__":
    num_caballos = 4
    caballos = [Caballo(f"Caballo {i + 1}", i + 1, 100) for i in range(num_caballos)]

    print("Bienvenido al simulador de carreras de caballos.")
    for i, caballo in enumerate(caballos):
        print(f"{i + 1}. {caballo.nombre}")

    while True:
        try:
            apuesta_numero = int(input("Elige el número del caballo en el que deseas apostar (1-4): "))
            if 1 <= apuesta_numero <= num_caballos:
                break
            else:
                print("Número no válido. Debes elegir un número de caballo entre 1 y 4.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    revisor = threading.Thread(target=revisar_estado, args=(caballos,))
    revisor.daemon = True
    revisor.start()

    simulador_carrera(caballos, apuesta_numero)