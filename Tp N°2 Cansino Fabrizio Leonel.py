# Alumno: Cansino Fabrizio Leonel

# Ejercicio 1
def ejercicio1():
    num = int(input("Ingresá un número entero: "))
    contador = 0
    num = abs(num)

    if num == 0:
        contador = 1
    else:
        while num > 0:
            num = num // 10
            contador += 1

    print("Cantidad de dígitos:", contador)


# Ejercicio 2
def ejercicio2():
    num = input("Ingresá un número decimal: ")

    enteros = 0
    decimales = 0
    punto = False

    for c in num:
        if c == ".":
            punto = True
        else:
            if punto == False:
                enteros += 1
            else:
                decimales += 1

    print("Dígitos enteros:", enteros)
    print("Dígitos decimales:", decimales)


# Ejercicio 3
def ejercicio3():
    entrada = input("Ingresá números: ").split()
    lista = []

    for x in entrada:
        lista.append(int(x))

    print("Números compuestos:")

    for num in lista:
        divisores = 0
        for i in range(1, num + 1):
            if num % i == 0:
                divisores += 1

        if divisores > 2:
            print(num)


# Ejercicio 4
def ejercicio4():
    entrada = input("Ingresá números: ").split()
    lista = []

    for x in entrada:
        lista.append(int(x))

    # a) Con auxiliar
    invertido = []
    for i in range(len(lista)-1, -1, -1):
        invertido.append(lista[i])

    print("Con auxiliar:", invertido)

    # b) Sin auxiliar
    n = len(lista)
    for i in range(n // 2):
        aux = lista[i]
        lista[i] = lista[n - 1 - i]
        lista[n - 1 - i] = aux

    print("Sin auxiliar:", lista)


# Ejercicio 5
def ejercicio5():
    entrada = input("Ingresá números: ").split()
    lista = []

    for x in entrada:
        lista.append(float(x))

    resultado = []

    for num in lista:
        parte = str(int(abs(num)))
        pares = 0
        impares = 0

        for d in parte:
            if int(d) % 2 == 0:
                pares += 1
            else:
                impares += 1

        if pares == 2 or impares >= 2:
            resultado.append(num)

    print("Resultado:", resultado)


# Ejercicio 6
def ejercicio6():
    entrada = input("Ingresá números: ").split()
    lista = []

    for x in entrada:
        lista.append(int(x))

    k = int(input("Ingresá K: "))

    resultado = []

    for num in lista:
        resultado.append(num)
        if num % k == 0:
            resultado.append(k)

    print("Resultado:", resultado)


# Ejercicio 7
def ejercicio7():
    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))

    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            num = int(input(f"[{i}][{j}]: "))
            fila.append(num)
        matriz.append(fila)

    print("\nMatriz:")
    for fila in matriz:
        print(fila)

    print("\nPromedio filas:")
    for i in range(filas):
        suma = 0
        for j in range(columnas):
            suma += matriz[i][j]
        print(suma / columnas)

    print("\nPromedio columnas:")
    for j in range(columnas):
        suma = 0
        for i in range(filas):
            suma += matriz[i][j]
        print(suma / filas)


# Ejercicio 8
def ejercicio8():
    def factorial(n):
        res = 1
        for i in range(1, n+1):
            res *= i
        return res

    n = int(input("Tamaño matriz: "))
    matriz = []

    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(int(input(f"[{i}][{j}]: ")))
        matriz.append(fila)

    suma = 0
    for i in range(n):
        suma += matriz[i][i]

    vector = []

    for i in range(n):
        for j in range(n):
            if factorial(matriz[i][j]) >= suma:
                vector.append(matriz[i][j])

    sin_rep = []
    for x in vector:
        if x not in sin_rep:
            sin_rep.append(x)

    print("Vector:", sin_rep)


# Ejercicio 9
def ejercicio9():
    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))

    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f"[{i}][{j}]: ")))
        matriz.append(fila)

    k = int(input("Fila (k): "))
    h = int(input("Columna (h): "))

    elem = matriz[k][h]

    mayor_fila = True
    for j in range(columnas):
        if matriz[k][j] > elem:
            mayor_fila = False

    menor_col = True
    for i in range(filas):
        if matriz[i][h] < elem:
            menor_col = False

    if mayor_fila and menor_col:
        print("Es punto silla")
    else:
        print("No es punto silla")


# Ejercicio 10
def ejercicio10():
    n = int(input("Tamaño matriz: "))
    matriz = []

    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(int(input(f"[{i}][{j}]: ")))
        matriz.append(fila)

    simetrica = True

    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                simetrica = False

    if simetrica:
        print("Es simétrica")
    else:
        print("No es simétrica")


# =========================
# MENÚ PRINCIPAL
# =========================

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Ejercicio 8")
        print("9. Ejercicio 9")
        print("10. Ejercicio 10")
        print("0. Salir")

        op = input("Elegí una opción: ")

        if op == "1":
            ejercicio1()
        elif op == "2":
            ejercicio2()
        elif op == "3":
            ejercicio3()
        elif op == "4":
            ejercicio4()
        elif op == "5":
            ejercicio5()
        elif op == "6":
            ejercicio6()
        elif op == "7":
            ejercicio7()
        elif op == "8":
            ejercicio8()
        elif op == "9":
            ejercicio9()
        elif op == "10":
            ejercicio10()
        elif op == "0":
            print("Fin del programa")
            break
        else:
            print("Opción inválida")


# Ejecutar
menu()