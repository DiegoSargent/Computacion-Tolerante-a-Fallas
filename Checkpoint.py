import pickle

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

# Función para verificar si alguien ha ganado
def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if all(cell == jugador for cell in fila):
            return True

    for col in range(3):
        if all(tablero[row][col] == jugador for row in range(3)):
            return True

    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

# Función para guardar la partida
def guardar_partida(tablero, jugador_actual):
    partida = {'tablero': tablero, 'jugador_actual': jugador_actual}
    with open('partida_guardada.pickle', 'wb') as archivo:
        pickle.dump(partida, archivo)

# Función para cargar la partida
def cargar_partida():
    try:
        with open('partida_guardada.pickle', 'rb') as archivo:
            partida = pickle.load(archivo)
            return partida['tablero'], partida['jugador_actual']
    except FileNotFoundError:
        return [[' ' for _ in range(3)] for _ in range(3)], 'X'  # Inicializa el tablero si no se encuentra una partida guardada

# Función principal
def jugar_gato():
    tablero, jugador_actual = cargar_partida()

    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {jugador_actual}")

        fila = int(input("Ingresa el número de fila (0, 1, 2): "))
        columna = int(input("Ingresa el número de columna (0, 1, 2): "))

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador_actual
        else:
            print("Esa casilla ya está ocupada. Inténtalo de nuevo.")
            continue

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break

        if ' ' not in [cell for row in tablero for cell in row]:
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = 'O' if jugador_actual == 'X' else 'X'

        guardar_partida(tablero, jugador_actual)

if __name__ == "__main__":
    jugar_gato()
