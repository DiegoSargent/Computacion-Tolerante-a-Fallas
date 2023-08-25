import logging

# Configuración de logging
logging.basicConfig(filename='registro_errores.log', level=logging.ERROR)

def realizar_calculos(numero):
    try:
        resultado = 10 / numero
        return resultado
    except ZeroDivisionError:
        logging.error("Error: División por cero")
        print("Error: División por cero")
        return None

def main():
    while True:
        try:
            entrada_usuario = input("Ingrese un número (escriba 'exit' para salir): ")
            if entrada_usuario.lower() == 'exit':
                break
            numero_usuario = int(entrada_usuario)
            resultado_calculo = realizar_calculos(numero_usuario)
            if resultado_calculo is not None:
                print(f"El resultado es: {resultado_calculo}")
        except ValueError:
            logging.error("Error: Entrada inválida. Ingrese un número.")
            print("Error: Entrada inválida. Ingrese un número.")

if __name__ == "__main__":
    main()
