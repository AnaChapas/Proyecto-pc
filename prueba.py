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
    print("")
    print("¡Bienvenido al programa Gasolineras Jaguar!")
    print("Elige una de las siguientes opciones:")
    print(" Escribe 1 si desea gestionar inventario")
    print(" Escribe 2 si desea comprar combustible")
    print(" Escribe 3 si desea gestionar turnos")
    print(" Escribe 4 si desea realizar el reporte de rentabilidad")
    eleccion= int(input(" Coloque la opcion elegida: "))

    if eleccion == 2:
            print("")
            print("--------------CARTELERA Y GALONES DISPONIBLES EN CADA DEPOSITO--------------")
            print("El precio de Regular es: Q.",Pregular, " el deposito de Regular tiene:",fdepositoR," galones") 
            print("El precio de Super es: Q.",Psuper, " el deposito de Super tiene:",fdepositoS," galones" )
            print("El precio de Diesel es: Q.",Pdiesel," el deposito de Diesel tiene:",fdepositoD," galones" )
            print("----------------------------------------------------------------------------")
            print("")
            print("Si desea agregarle a su carro regular, coloque 1: ")
            print("Si desea agregarle a su carro super, coloque 2: ")
            print("Si desea agregarle a su carro disel, coloque 3: ")
            tipocombustible=int(input("¿Qué tipo de combustible desea agregar? "))
            
            #Si se escoge la opcion 1 se realizara lo siguiente:     
            if tipocombustible==1:
                if fdepositoR <=5:
                    print("")
                    print("No puede continuar con la compra debido a que el deposito tiene bajo nivel de galones ")
                    print("¿Desea regresar a menú?")
                    print("Si desea regresar a menú, coloque 1")
                    print("Si desea salir definitivamente del programa, coloque 2")
                    eleccion2=int(input("Coloque la opcion elegida: "))
                    if eleccion2==1:
                        continuar=True
                    else: 
                        continuar=False
                else:
                    print("")
                    print("¿Desea consumir por galón de combustible, o bien por cantidad de dinero equivalente a N galones?")
                    print("Si desea consumir por galón de combustible, coloque 1")
                    print("Si desea consumir por cantidad de dinero equivalente a N galones, coloque 2")
                    eleccion3=int(input("Coloque la opcion elegida: "))
                
                    if eleccion3==1:
                        eleccion4=int(input("¿cuantos galones desea agregar? "))      
                        fdepositoR=fdepositoR-eleccion4               
                        if fdepositoR<0:
                            print("No puede continuar con la compra debido a que el deposito tiene bajo nivel de galones ")
                            print("¿Desea regresar a menú?")
                            print("Si desea regresar a menú, coloque 1")
                            print("Si desea salir definitivamente del programa, coloque 2")
                            eleccion5=int(input("Coloque la opcion elegida: "))
                            if eleccion5==1:
                                continuar=True
                            else: 
                                continuar=False
                        else:
                            if fdepositoR>=0:
                                nombrecliente1=input("Ingrese su nombre completo:")
                                nit1=input("Ingrese su número de NIT: ")
                                nobomba1=input("Ingrese el número de a utilizar (un número entre 1 y 4):")
                                print("")
                                print("-------------------RESUMEN DE SU COMPRA-------------------")
                                print("Nombre del cliente: ",nombrecliente1)
                                print("NIT: ",nit1)
                                totalconsum1=eleccion4*Pregular
                                print("Total a pagar: Q.",totalconsum1)
                                print("----------------------------------------------------------------------------")
                                print("")
                                print("Si desea continuar con su compra, coloque 1")
                                print("Si desea cancelar su compra, coloque 2")
                                eleccion6=input("¿Desea continuar con su compra?:")
                                if eleccion6==1:
                                    print("")
                                    targetanum1=int(input("Ingrese el número de su targeta para realizar el cobro: "))
                                    if targetanum1==targetanum1:
                                        print("¡Su compra fue realizada con exito!")                                        
                                else:
                                    if eleccion==2:
                                        print("")
                                        print("¿Desea regresar a menú?")
                                        print("Si desea regresar a menú, coloque 1")
                                        print("Si desea salir definitivamente del programa, coloque 2")
                                        eleccion9=int(input("Coloque la opcion elegida: "))
                                        if eleccion9==1:
                                            continuar=True
                                        else: 
                                         continuar=False
                    else:
                        print("")
                        eleccion10=int(input("¿cuantos desea agregar? "))      
                        galones1=eleccion10/fdepositoR  
                        FdepositoR=fdepositoR-galones1        
                        if fdepositoR<0:
                            print("No puede continuar con la compra debido a que el deposito tiene bajo nivel de galones ")
                            print("¿Desea regresar a menú?")
                            print("Si desea regresar a menú, coloque 1")
                            print("Si desea salir definitivamente del programa, coloque 2")
                            eleccion11=int(input("Coloque la opcion elegida: "))
                            if eleccion11==1:
                                continuar=True
                            else: 
                                continuar=False
                        else:
                             if fdepositoR>=0:
                                nombrecliente2=input("Ingrese su nombre completo:")
                                nit2=input("Ingrese su número de NIT: ")
                                nobomba2=input("Ingrese el número de a utilizar (un número entre 1 y 4):")
                                print("")
                                print("-------------------RESUMEN DE SU COMPRA-------------------")
                                print("Nombre del cliente: ",nombrecliente2)
                                print("NIT: ",nit2)
                                print("Total a pagar: Q.",eleccion10)
                                print("----------------------------------------------------------------------------")
                                print("")
                                print("Si desea continuar con su compra, coloque 1")
                                print("Si desea cancelar su compra, coloque 2")
                                eleccion12=input("¿Desea continuar con su compra?: ")
                                if eleccion12==1:
                                    print("")
                                    targetanum2=int(input("Ingrese el número de su targeta para realizar el cobro: "))
                                    if targetanum2==targetanum2:
                                        print("¡Su compra fue realizada con exito!")
                                else:
                                    if eleccion12==2:
                                        print("")
                                        print("¿Desea regresar a menú?")
                                        print("Si desea regresar a menú, coloque 1")
                                        print("Si desea salir definitivamente del programa, coloque 2")
                                    eleccion50=int(input("Coloque la opcion elegida: "))
                                    if eleccion50==1:
                                       continuar=True
                                    else: 
                                        continuar=False