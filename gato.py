import random

tablero = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]

puntajes = [0, 0]
racha_jugador1 = 0
racha_jugador2 = 0
numero_partida = 1

def reiniciar_tablero():
    global tablero
    tablero = [[' ', ' ', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]

def imprimir_tablero():
    print("\n")
    print("   1   2   3 ")
    print("1  " + tablero[0][0] + " | " + tablero[0][1] + " | " + tablero[0][2])
    print("  ---+---+---")
    print("2  " + tablero[1][0] + " | " + tablero[1][1] + " | " + tablero[1][2])
    print("  ---+---+---")
    print("3  " + tablero[2][0] + " | " + tablero[2][1] + " | " + tablero[2][2])

def validar_coordenada(fila, columna):
    if fila < 1 or fila > 3 or columna < 1 or columna > 3:
        print("Coordenada fuera de rango. Inténtalo nuevamente.")
        return False
    return True

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return True
    return False

def jugar_entre_jugadores():
    global racha_jugador1, racha_jugador2, puntajes, numero_partida

    jugador1 = input("Jugador 1, ingresa tu nombre: ")
    jugador2 = input("Jugador 2, ingresa tu nombre: ")

    while True:
        simbolo1 = input(f"{jugador1}, selecciona tu símbolo (X/O): ")
        if simbolo1.upper() != 'X' and simbolo1.upper() != 'O':
            print("Símbolo inválido. Inténtalo nuevamente.")
        else:
            break

    simbolo2 = 'X' if simbolo1.upper() == 'O' else 'O'

    print(f"\n{jugador1} (Símbolo: {simbolo1}) vs {jugador2} (Símbolo: {simbolo2})\n")

    reiniciar_tablero()

    while True:
        print(f"\nPartida {numero_partida}")
        imprimir_tablero()

        if numero_partida != 1:
            print("\nMarcador:")
            print(f"{jugador1} - Puntos: {puntajes[0]}, Racha: {racha_jugador1}")
            print(f"{jugador2} - Puntos: {puntajes[1]}, Racha: {racha_jugador2}")

        jugador_actual = jugador1
        simbolo_actual = simbolo1

        while True:
            fila = int(input(f"\n{jugador_actual}, ingresa la fila (1-3): "))
            columna = int(input(f"{jugador_actual}, ingresa la columna (1-3): "))

            if not validar_coordenada(fila, columna):
                continue

            if tablero[fila - 1][columna - 1] != ' ':
                print("Casilla ocupada. Inténtalo nuevamente.")
                continue

            tablero[fila - 1][columna - 1] = simbolo_actual
            break

        if verificar_ganador():
            print(f"\n¡{jugador_actual} ha ganado la partida!")
            if jugador_actual == jugador1:
                racha_jugador1 += 1
                puntajes[0] += 3
            else:
                racha_jugador2 += 1
                puntajes[1] += 3
            imprimir_tablero()
            opcion = input("\n¿Desean jugar otra partida? (S/N): ")
            if opcion.lower() == 'n':
                print("\nMarcador final:")
                print(f"{jugador1} - Puntos: {puntajes[0]}, Racha: {racha_jugador1}")
                print(f"{jugador2} - Puntos: {puntajes[1]}, Racha: {racha_jugador2}")
                break
            else:
                reiniciar_tablero()
                numero_partida += 1
                continue

        if all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
            print("\n¡Empate!")
            puntajes[0] += 1
            puntajes[1] += 1
            imprimir_tablero()
            opcion = input("\n¿Desean jugar otra partida? (S/N): ")
            if opcion.lower() == 'n':
                print("\nMarcador final:")
                print(f"{jugador1} - Puntos: {puntajes[0]}, Racha: {racha_jugador1}")
                print(f"{jugador2} - Puntos: {puntajes[1]}, Racha: {racha_jugador2}")
                break
            else:
                reiniciar_tablero()
                numero_partida += 1
                continue

        if jugador_actual == jugador1:
            jugador_actual = jugador2
            simbolo_actual = simbolo2
        else:
            jugador_actual = jugador1
            simbolo_actual = simbolo1

def jugar_contra_cpu():
    global racha_jugador1, racha_jugador2, puntajes, numero_partida

    jugador1 = input("Jugador, ingresa tu nombre: ")

    while True:
        simbolo1 = input(f"{jugador1}, selecciona tu símbolo (X/O): ")
        if simbolo1.upper() != 'X' and simbolo1.upper() != 'O':
            print("Símbolo inválido. Inténtalo nuevamente.")
        else:
            break

    simbolo2 = 'X' if simbolo1.upper() == 'O' else 'O'

    print(f"\n{jugador1} (Símbolo: {simbolo1}) vs CPU (Símbolo: {simbolo2})\n")

    reiniciar_tablero()

    while True:
        print(f"\nPartida {numero_partida}")
        imprimir_tablero()

        if numero_partida != 1:
            print("\nMarcador:")
            print(f"{jugador1} - Puntos: {puntajes[0]}, Racha: {racha_jugador1}")
            print(f"CPU - Puntos: {puntajes[1]}, Racha: {racha_jugador2}")

        jugador_actual = jugador1
        simbolo_actual = simbolo1

        while True:
            fila = int(input(f"\n{jugador_actual}, ingresa la fila (1-3): "))
            columna = int(input(f"{jugador_actual}, ingresa la columna (1-3): "))

            if not validar_coordenada(fila, columna):
                continue

            if tablero[fila - 1][columna - 1] != ' ':
                print("Casilla ocupada. Inténtalo nuevamente.")
                continue

            tablero[fila - 1][columna - 1] = simbolo_actual
            break

        if verificar_ganador():
            if jugador_actual == jugador1:
                racha_jugador1 += 1
                puntajes[0] += 3
                print(f"\n¡{jugador_actual} ha ganado la partida!")
            else:
                racha_jugador2 += 1
                puntajes[1] += 3
                print(f"\n¡CPU ha ganado la partida!")
            imprimir_tablero()
            opcion = input("\n¿Deseas jugar otra partida? (S/N): ")
            if opcion.lower() == 'n':
                print("\nMarcador final:")
                print(f"{jugador1} - Puntos: {puntajes[0]}, Racha: {racha_jugador1}")
                print(f"CPU - Puntos: {puntajes[1]}, Racha: {racha_jugador2}")
                break
            else:
                reiniciar_tablero()
                numero_partida += 1
                continue

        if all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
            print("\n¡Empate!")
            puntajes[0] += 1
            puntajes[1] += 1
            imprimir_tablero()
            opcion = input("\n¿Deseas jugar otra partida? (S/N): ")
            if opcion.lower() == 'n':
                print("\nMarcador final:")
                print(f"{jugador1} - Puntos: {puntajes[0]}, Racha: {racha_jugador1}")
                print(f"CPU - Puntos: {puntajes[1]}, Racha: {racha_jugador2}")
                break
            else:
                reiniciar_tablero()
                numero_partida += 1
                continue

        # Movimiento de la CPU
        while True:
            fila = random.randint(1, 3)
            columna = random.randint(1, 3)

            if tablero[fila - 1][columna - 1] == ' ':
                tablero[fila - 1][columna - 1] = simbolo2
                break

        jugador_actual = jugador1
        simbolo_actual = simbolo1

def jugar_gato():
    print("Bienvenido al juego de Gato\n")
    while True:
        print("Selecciona una opción:")
        print("1. Jugar entre jugadores")
        print("2. Jugar contra la CPU")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == '1':
            jugar_entre_jugadores()
        elif opcion == '2':
            jugar_contra_cpu()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")

jugar_gato()
