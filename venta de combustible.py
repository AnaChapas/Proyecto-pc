#Menú de combustible

#VARIABLES GENERALES
#Cantidad inicial en cada deposito
depositoR=40
depositoS=40
depositoD=40
#Contador para cantidad de galones final de deposito
fdepositoR=0
fdepositoS=0
fdepositoD=0
# 
#Variables para precio 
precioagregar=0
precioventa=0

#CODIGOS 

#Codigo de gestion de inventario

#Codigo de venta de combustible
Pregular=29.00
Psuper=30.00
Pdiesel=26.50
continuar=True
while continuar:
    print("Bienvenido al programa Gasolineras Jaguar")
    print("Elige una de las siguientes opciones:")
    print(" Escribe (1) si desea gestionar inventario")
    print(" Escribe (2) si desea comprar combustible")
    print(" Escribe (3) si desea gestionar turnos")
    print(" Escribe (4) si desea realizar el reporte de rentabilidad")
    eleccion= int(input(" Coloque la opcion elegida: "))

    if eleccion == 2:
        print("----------CARTELERA Y GALONES DISPONIBLES EN CADA DEPOSITO----------")
        print("El precio de Regular es :",Pregular, " el deposito de Regular tiene:",fdepositoR) 
        print("El precio de Super es :",Psuper, " el deposito de Super tiene:",fdepositoS )
        print("El precio de Diesel es :",Pdiesel," el deposito de Diesel tiene:",fdepositoD )
        tipocombustible=input("Que tipo de combustible desea agregar:")
        
        iffdeposito
    
    continuar=input("Desea continuar")
