from funciones import*
print("primero debe registrarse")
nombredes = input("ingrese su nombre:")
nombred.append(nombredes)
rutdes = int(input("ingrese su rut:"))
rutd.append(rutdes)
print("menu")
print("""
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa""")
opc = int(input("que opion desera usar:"))
if opc == 1:
    opc_1()
elif opc == 2:
    opc_2()
elif opc ==3:
    opc_3()
elif opc == 4:
    opc_4()
elif opc == 5:
    opc_5()
else:
    print("opcion no disponible")