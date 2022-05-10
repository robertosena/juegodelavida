
import copy, random, sys, time


# Constantes
ANCHO = int(input("Introduzca el ancho de la cuadricula:"))   # Ancho de la cuadrícula
ALTO = int(input("Introduzca el alto de la cuadricula:"))   # Alto de la cuadrícula

VIVO = str(input("Introduzca el carácter de la célula viva:"))   # Carácter para la celda viva
MUERTO = ' '   # Carácter para la celda muerta

# Las variables celulas y siguientesCelulas son diccionarios que contienen
# el estado actual del juego y el siguiente.
# Las claves del diccionario son tuplas que pueden tener el valor VIVO o MUERTO
siguientesCelulas = {}

# Asignamos valores aleatorios a las células iniciales
for x in range(ANCHO):
    for y in range(ALTO):
        # 50% de posibilidades de estar viva o muerta
        if random.randint(0, 1) == 0:
            siguientesCelulas[(x, y)] = VIVO
        else:
            siguientesCelulas[(x, y)] = MUERTO

while True:  # bucle principal del programa
    # Cada iteración de este bucle es una generación de la simulación del juego de la vida

    print('\n' * 50)  # Separación entre generaciones
    celulas = copy.deepcopy(siguientesCelulas)

    # Imprimimos las células por pantalla
    for y in range(ALTO):
        for x in range(ANCHO):
            print(celulas[(x, y)], end='')
        print()
    print('Pulsa Ctrl-C para parar.')

    # Calculamos la nueva generación de células en función de los valores actuales
    for x in range(ANCHO):
        for y in range(ALTO):
            # Obtenemos las coordenadas de las vecinas incluso si están en el límite
            izquierda  = (x - 1) % ANCHO
            derecha = (x + 1) % ANCHO
            arriba = (y - 1) % ALTO
            abajo = (y + 1) % ALTO

            # Calculamos el número de células vecinas vivas
            numVecinasVivas = 0
            if celulas[(izquierda, arriba)] == VIVO:
                numVecinasVivas += 1
            if celulas[(x, arriba)] == VIVO:
                numVecinasVivas += 1
            if celulas[(derecha, arriba)] == VIVO:
                numVecinasVivas += 1
            if celulas[(izquierda, y)] == VIVO:
                numVecinasVivas += 1
            if celulas[(derecha, y)] == VIVO:
                numVecinasVivas += 1
            if celulas[(izquierda, abajo)] == VIVO:
                numVecinasVivas += 1
            if celulas[(x, abajo)] == VIVO:
                numVecinasVivas += 1
            if celulas[(derecha, abajo)] == VIVO:
                numVecinasVivas += 1

            # Basamos el valor de la nueva generación en función
            # de los valores actuales
            if celulas[(x, y)] == VIVO and (numVecinasVivas == 2
                                            or numVecinasVivas == 3):
                    # Cálulas vivas con 2 o 3 vecinas vivas permanecen vivas
                    siguientesCelulas[(x, y)] = VIVO
            elif celulas[(x, y)] == MUERTO and numVecinasVivas == 2:
                # Células muertas con 2 vecinas vivas cobran vida
                siguientesCelulas[(x, y)] = VIVO
            else:
                # En cualquier otro caso continuan muertas
                siguientesCelulas[(x, y)] = MUERTO

    try:
        time.sleep(1)  # Añadimos un segundo de pausa para evitar parpadeos
    except KeyboardInterrupt:
        print("Juego de la vida de Conway")
        print("https://es.wikipedia.org/wiki/Juego_de_la_vida")
        sys.exit()  # Cuando se pulsa CTRL+C termina el programa
