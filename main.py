def getTable(number, limit):
    with open("Tablas de multiplicar.txt", 'a') as file:
        file.write(f"\nLa tabla del {number} es:\n")

        for i in range(1, limit + 1):
            result = number * i
            file.write(f"{number} x {i} = {result}\n")


def getConceptandDef():
    concept = input("Ingrese el concepto: ")
    definition = input("Ingrese la definición: ")

    with open("Conceptos y definiciones.txt", 'a') as file:
        file.write(f"\nConcepto: {concept}\nDefinición: {definition}\n")


def getFullName():
    full_name = input("Ingrese su nombre completo: ")

    with open("Nombres completos.txt", 'a') as file:
        file.write(f"{full_name}\n")


while True:
    print("-----Menú principal-----")
    print("1. Generar tabla de multiplicar")
    print("2. Concepto y definición")
    print("3. Nombre completo")
    print("4. Salir del programa")

    main_menu = int(input("Ingrese una opción: "))

    if main_menu == 1:
        user_number = int(input("Ingrese la tabla que desea: "))
        user_limit = int(input("Ingrese dónde termina la tabla: "))
        getTable(user_number, user_limit)

    elif main_menu == 2:
        getConceptandDef()

    elif main_menu == 3:
        getFullName()

    elif main_menu == 4:
        print("Saliendo del programa...")
        break
