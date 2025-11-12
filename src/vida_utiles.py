import random

def crear_tablero(filas: int, columnas: int) -> list[list[bool]]:
    """
    Crea un nuevo tablero vacío, con todas las células muertas.
    Parametros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
    Devuelve:
        Una lista de listas con todos los elementos False.
    """
    res = []
    matriz = []
    columna = []
    for i in range(columnas):
        columna.append(False)
    for i in range(filas):
        matriz.append(columna)
    return matriz

def crear_tablero_aleatorio(filas: int, columnas: int, probabilidad_vida: float) -> list[list[bool]]:
    """
    Crea un tablero con células vivas distribuidas aleatoriamente.

    Parámetros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
        probabilidad_vida (float): Un valor entre 0.0 y 1.0 que representa la
                                   probabilidad de que una célula esté viva.

    Devuelve:
        Una lista de listas que representa el tablero con células vivas (True) y muertas (False).
    """
    tabla = crear_tablero(filas, columnas)
    for i in tabla:
        for j in i:
            if random.random() < probabilidad_vida:
                i[j] = True

    return tabla
            
        
    random.random()

def insertar_patron(tablero: list[list[bool]], patron: list[list[bool]], pos_fila: int, pos_col: int):
    """
    Inserta un patrón (una pequeña matriz) en el tablero en una posición dada.
    Parámetros:
        tablero (list[list[bool]]): El tablero donde se insertará el patrón.
        patron (list[list[bool]]): El patrón a insertar.
        pos_fila (int): La fila en la que se insertará la esquina superior izquierda del patrón.
        pos_col (int): La columna en la que se insertará la esquina superior izquierda del patrón.
    
    for j in tablero[pos_fila:]:
        subfila_a_modificar = tablero[pos_col:]
        if patron[0] > subfila_a_modificar:
            return tablero
        subfila_a_modificar = patron[i]s
        for 

        return tablero
    """
    filas_patron = len(patron)
    columnas_patron = len(patron[0])
    filas_tablero = len(tablero)
    columnas_tablero = len(tablero[0])
    
    for f in range(filas_patron):
        if pos_fila+f>=filas_tablero:
            break
        for c in range(columnas_patron):
            if pos_col+c>=columnas_tablero:
                break
            tablero[pos_fila+f][pos_col+c]=patron[f][c]
    return tablero


def contar_vecinos(tablero: list[list[bool]], fila: int, col: int) -> int:
    """
    Cuenta el número de vecinos vivos de una célula en la posición (fila, col).
    El tablero es toroidal, lo que significa que los bordes se conectan.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
        fila (int): La fila de la célula.
        col (int): La columna de la célula.
    Devuelve:
        El número de vecinos vivos (int).
    """
    for i in range():
        for j in columna:


def calcular_siguiente_generacion(tablero):
    """
    Calcula el estado del tablero en el siguiente paso de tiempo basándose en las reglas
    del Juego de la Vida.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
    Devuelve:
        Una nueva lista de listas que representa el tablero en la siguiente generación.
    """
    # TODO: Ejercicio 5
    pass
