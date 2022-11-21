#!/usr/bin/env python3
# -*- encode: utf-8 -*-

def agregar_objeto():
    global objetos
    global llaves
    Objet = input("Ingrese su objeto:")
    global valores
    valor = input("Ingrese el dato ")
    objetos[Objet] = valor
    print(objetos)


objetos = {}    


while True:
    print("\n----Proyecto en Python---\n")
    print("[1]----Agregar objeto")
    print("[2]----separar")
    print("[3]----Salir")

    try:
        option = int(input("\nSelecciona una opcion: "))
        if option == 1:
                agregar_objeto()
                
        elif option == 2:
            keys = objetos.keys()
            sorted_keys = sorted(keys)
            sorted_objetos = {}
            for key in sorted_keys:
                sorted_objetos[key] = objetos[key]
            print(objetos)
            llave = sorted_objetos.keys()
            valor = sorted_objetos.values()
            print(llave)
            print(valor)
        elif option == 3:  
            exit(0)
    except:
        print("INGRESE LOS VALORES REQUERIDOS")

