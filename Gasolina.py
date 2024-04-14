
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
if eleccion==2:
 print("El precio de Regular es :",Pregular, " el deposito de Regular tiene:",fdepositoR) 
 print("El precio de Super es :",Psuper, " el deposito de Super tiene:",fdepositoS )
 print("El precio de Diesel es :",Pdiesel," el deposito de Diesel tiene:",fdepositoD )

#Codigo de gestión de turnos
salariotrabajadores=0
#Codigo de reporte de rentabilidad