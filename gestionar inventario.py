#Menú de combustible

#VARIABLES GENERALES
#Cantidad inicial en cada deposito
depositoR=40
depositoS=40
depositoD=40
#Contador para cantidad de galones final de deposito
fdepositoR=40
fdepositoS=40
fdepositoD=40
#Precios de gasolina
Pregular=29.00
Psuper=30.00
Pdiesel=26.50
#Variables para precio 
precioagregar=0
precioventa=0

#CODIGOS 
continuar=True
while continuar:
    print("")
    print("¡Bienvenido al programa Gasolineras Jaguar!")
    print("Elige una de las siguientes opciones:")
    print(" Escribe 1 si desea gestionar inventario")
    print(" Escribe 2 si desea comprar combustible")
    print(" Escribe 3 si desea gestionar turnos")
    print(" Escribe 4 si desea realizar el reporte de rentabilidad")
    eleccion= int(input(" Coloque la opcion elegida: "))
#Codigo de gestion de inventario
