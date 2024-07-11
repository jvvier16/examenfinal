trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajador_sueldo=[]
sueldos=[]
nombred=[]
rutd=[]
import time
import random
aleatorio = random.randint(300000,2500000)

def registro():
    print("primero debe registrarse")
    nombredes = input("ingrese su nombre")
    rutdes = int(input(""))
def opc_1():
    print("generar sueldos random")
    for x in range(9):
        lol = print(trabajadores[x],aleatorio)
        sueldos.append(aleatorio)
        trabajador_sueldo.append(lol)
def opc_2():
    sueldos.sort
    print("sueldo entre 300.000 a 1.300.000")
    if sueldos >1300000:
        print(sueldos)
    else:
        print("mayores a 1.300.000")
        print(sueldos)
def opc_3():
    sueldos.sort
    print("sueldo menor",sueldos[0])
    print("sueldo mayor",sueldos[9])
    sueldo =sueldos[0] + sueldos[9]
    sueldop = sueldo/2
    print("sueldo promedio",sueldop)
    media= (sueldo[0]+sueldo[1]+sueldo[2]+sueldo[3]+sueldo[4]+sueldo[5]+sueldo[6]+sueldo[7]+sueldo[8]+sueldo[9])**1/10
    print("medida geometrica",media)
def opc_4():
    import csv
    nombre_archivo = input("que nombre le dara al archivo:")
    with(nombre_archivo,"csv","","e"):
      print("archivo creado")  
    for x in range(9):
        print("nombre          sueldo      desvuento salud            descuento afp               sueldo bruto    ")
        print(trabajadores[x], sueldos[x], descuentos=sueldos[x]*0.12,descuentoa= sueldos[x]*0.07,sueldof=sueldos[x]*0.19)
def opc_5():
    print("finalisando programa")
    print("desarollador",nombred)
    print("rut",rutd)
    time.sleep(3)
