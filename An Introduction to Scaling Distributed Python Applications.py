import threading
import time

# Función que simula un proceso que toma un tiempo en ejecutarse
def proceso(id, duracion):
    print(f"Proceso {id} iniciado.")
    time.sleep(duracion)
    print(f"Proceso {id} completado.")

# Lista de datos que se procesarán en hilos
datos = [2, 3, 5, 7, 11]

# Crear una lista para almacenar los hilos
hilos = []

# Crear y empezar un hilo para cada dato
for i, dato in enumerate(datos):
    hilo = threading.Thread(target=proceso, args=(i, dato))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Todos los procesos han sido completados.")
