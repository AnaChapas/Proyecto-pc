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
#Codigo de venta de combustible
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
                            fdepositoR=fdepositoR++eleccion4
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
                                eleccion6 = int(input("¿Desea continuar con su compra?: "))
                                if eleccion6 == 1:
                                    print("")
                                    targetanum1 = int(input("Ingrese el número de su tarjeta para realizar el cobro: "))
                                    targeta1=targetanum1
                                    if targetanum1 == targeta1:
                                        print("¡Su compra fue realizada con éxito!")
                                    else:
                                        print("Número de tarjeta inválido. Intente nuevamente.")
                                else:
                                    print("")
                                    print("¿Desea regresar a menú?")
                                    print("Si desea regresar a menú, coloque 1")
                                    print("Si desea salir definitivamente del programa, coloque 2")
                                    eleccion9 = int(input("Coloque la opción elegida: "))
                                    if eleccion9 == 1:
                                        continuar = True
                                    else:
                                        continuar = False
                    else:
                        print("")
                        eleccion10=int(input("¿cuantos desea agregar? "))      
                        galones1=eleccion10/fdepositoR  
                        fdepositoR=fdepositoR-galones1        
                        if fdepositoR<0:
                            fdepositoR=fdepositoR++galones1
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
                                eleccion12 = int(input("¿Desea continuar con su compra?: "))
                                if eleccion12 == 1:
                                    print("")
                                    targetanum2 = int(input("Ingrese el número de su tarjeta para realizar el cobro: "))
                                    targeta2=targetanum2
                                    if targetanum2 == targeta2:
                                        print("¡Su compra fue realizada con éxito!")
                                    else:
                                        print("Número de tarjeta inválido. Intente nuevamente.")
                                else:
                                    print("")
                                    print("¿Desea regresar a menú?")
                                    print("Si desea regresar a menú, coloque 1")
                                    print("Si desea salir definitivamente del programa, coloque 2")
                                    eleccion9 = int(input("Coloque la opción elegida: "))
                                    if eleccion9 == 1:
                                        continuar = True
                                    else:
                                        continuar = False
            #Si se escoge la opcion 2 se realizara lo siguiente:                                 
            elif tipocombustible==2:
                    if fdepositoS <=5:
                        print("")
                        print("No puede continuar con la compra debido a que el deposito tiene bajo nivel de galones ")
                        print("¿Desea regresar a menú?")
                        print("Si desea regresar a menú, coloque 1")
                        print("Si desea salir definitivamente del programa, coloque 2")
                        eleccion15=int(input("Coloque la opcion elegida: "))
                        if eleccion15==1:
                            continuar=True
                        else: 
                            continuar=False
                    else:
                        print("")
                        print("¿Desea consumir por galón de combustible, o bien por cantidad de dinero equivalente a N galones?")
                        print("Si desea consumir por galón de combustible, coloque 1")
                        print("Si desea consumir por cantidad de dinero equivalente a N galones, coloque 2")
                        eleccion16=int(input("Coloque la opcion elegida: "))
                        if eleccion16==1:
                            print("")
                            eleccion17=int(input("¿cuantos galones desea agregar?: "))      
                            fdepositoS=fdepositoS-eleccion17
                            if fdepositoS<0:
                                fdepositoS=fdepositoS++eleccion17
                                print("No puede continuar con la compra debido a que el deposito tiene bajo nivel de galones ")
                                print("¿Desea regresar a menú?")
                                print("Si desea regresar a menú, coloque 1")
                                print("Si desea salir definitivamente del programa, coloque 2")
                                eleccion18=int(input("Coloque la opcion elegida: "))
                                print("")
                                if eleccion18==1:
                                    continuar=True
                                else: 
                                    continuar=False
                            else:
                                if fdepositoS>=0:
                                    print("")
                                    nombrecliente3=input("Ingrese su nombre completo: ")
                                    nit3=input("Ingrese su número de NIT: ")
                                    nobomba3=input("Ingrese el número de a utilizar (un número entre 1 y 4): ")
                                    print("")
                                    print("-------------------RESUMEN DE SU COMPRA-------------------")
                                    print("Nombre del cliente: ",nombrecliente3)
                                    print("NIT: ",nit3)
                                    totalconsum3=eleccion17*Pregular
                                    print("Total a pagar: Q.",totalconsum3)
                                    print("----------------------------------------------------------------------------")
                                    print("")
                                    print("Si desea continuar con su compra, coloque 1")
                                    print("Si desea cancelar su compra, coloque 2")
                                    eleccion51 = int(input("¿Desea continuar con su compra?: "))
                                    if eleccion51 == 1:
                                        print("")
                                        targetanum3 = int(input("Ingrese el número de su tarjeta para realizar el cobro: "))
                                        targeta3=targetanum3
                                        if targetanum3 == targeta3:
                                            print("¡Su compra fue realizada con éxito!")
                                        else:
                                            print("Número de tarjeta inválido. Intente nuevamente.")
                                    else:
                                        print("")
                                        print("¿Desea regresar a menú?")
                                        print("Si desea regresar a menú, coloque 1")
                                        print("Si desea salir definitivamente del programa, coloque 2")
                                        eleccion52= int(input("Coloque la opción elegida: "))
                                        if eleccion52 == 1:
                                            continuar = True
                                        else:
                                            continuar = False
                        else:
                            print("")
                            eleccion23=int(input("¿cuanto desea agregar? "))      
                            galones3=eleccion23/fdepositoS 
                            fdepositoS= fdepositoS-galones3         
                            if fdepositoS<0:
                                fdepositoS=fdepositoS++galones3
                                print("No puede continuar con la compra debido a que el deposito tiene bajo nivel de galones ")
                                print("¿Desea regresar a menú?")
                                print("Si desea regresar a menú, coloque 1")
                                print("Si desea salir definitivamente del programa, coloque 2")
                                eleccion24=int(input("Coloque la opcion elegida: "))
                                if eleccion24==1:
                                    continuar=True
                                else: 
                                    continuar=False
                            else:
                                if fdepositoS>=0:
                                    print("")
                                    nombrecliente4=input("Ingrese su nombre completo:")
                                    nit4=input("Ingrese su número de NIT: ")
                                    nobomba4=input("Ingrese el número de a utilizar (un número entre 1 y 4): ")
                                    print("")
                                    print("-------------------RESUMEN DE SU COMPRA-------------------")
                                    print("Nombre del cliente: ",nombrecliente4)
                                    print("NIT: ",nit4)
                                    print("Total a pagar: Q.",eleccion23)
                                    print("----------------------------------------------------------------------------")
                                    print("")
                                    print("Si desea continuar con su compra, coloque 1")
                                    print("Si desea cancelar su compra, coloque 2")
                                    eleccion54 = int(input("¿Desea continuar con su compra?: "))
                                    if eleccion54 == 1:
                                        print("")
                                        targetanum4 = int(input("Ingrese el número de su tarjeta para realizar el cobro: "))
                                        targeta4=targetanum4
                                        if targetanum4 == targetanum4:
                                            print("¡Su compra fue realizada con éxito!")
                                        else:
                                            print("Número de tarjeta inválido. Intente nuevamente.")
                                    else:
                                        print("")
                                        print("¿Desea regresar a menú?")
                                        print("Si desea regresar a menú, coloque 1")
                                        print("Si desea salir definitivamente del programa, coloque 2")
                                        eleccion55= int(input("Coloque la opción elegida: "))
                                        if eleccion55 == 1:
                                            continuar = True
                                        else:
                                            continuar = False                                
            #Si se escoge la opcion 3 se realizara lo siguiente:     
            else:
                if fdepositoD <=5:
                    print("")
                    print("No puede continuar con la compra debido a que el deposito tiene bajo nivel de galones ")
                    print("¿Desea regresar a menú?")
                    print("Si desea regresar a menú, coloque 1")
                    print("Si desea salir definitivamente del programa, coloque 2")
                    eleccion27=int(input("Coloque la opcion elegida: "))
                    if eleccion27==1:
                        continuar=True
                    else: 
                        continuar=False
                else:
                    print("")
                    print("¿Desea consumir por galón de combustible, o bien por cantidad de dinero equivalente a N galones?")
                    print("Si desea consumir por galón de combustible, coloque 1")
                    print("Si desea consumir por cantidad de dinero equivalente a N galones, coloque 2")
                    eleccion28=int(input("Coloque la opcion elegida: "))
                
                    if eleccion28==1:
                        print("")
                        eleccion29=int(input("¿cuantos galones desea agregar? "))      
                        fdepositoD=fdepositoD-eleccion29               
                        if fdepositoD<0:
                            fdepositoD=fdepositoD++eleccion29
                            print("No puede continuar con la compra debido a que el deposito tiene bajo nivel de galones ")
                            print("")
                            print("¿Desea regresar a menú?")
                            print("Si desea regresar a menú, coloque 1")
                            print("Si desea salir definitivamente del programa, coloque 2")
                            eleccion29=int(input("Coloque la opcion elegida: "))
                            if eleccion29==1:
                                continuar=True
                            else: 
                                continuar=False
                        else:
                            if fdepositoD>=0:
                                print("")
                                nombrecliente5=input("Ingrese su nombre completo:")
                                nit5=input("Ingrese su número de NIT: ")
                                nobomba5=input("Ingrese el número de a utilizar (un número entre 1 y 4): ")
                                print("")
                                print("-------------------RESUMEN DE SU COMPRA-------------------")
                                print("Nombre del cliente: ",nombrecliente5)
                                print("NIT: ",nit5)
                                totalconsum5=eleccion29*Pregular
                                print("Total a pagar: Q.",totalconsum5)
                                print("----------------------------------------------------------------------------")
                                print("")
                                print("Si desea continuar con su compra, coloque 1")
                                print("Si desea cancelar su compra, coloque 2")
                                eleccion56 = int(input("¿Desea continuar con su compra?: "))
                                if eleccion56 == 1:
                                    print("")
                                    targetanum5 = int(input("Ingrese el número de su tarjeta para realizar el cobro: "))
                                    targeta5=targetanum5
                                    if targetanum5 == targeta5:
                                        print("¡Su compra fue realizada con éxito!")
                                    else:
                                        print("Número de tarjeta inválido. Intente nuevamente.")
                                else:
                                    print("")
                                    print("¿Desea regresar a menú?")
                                    print("Si desea regresar a menú, coloque 1")
                                    print("Si desea salir definitivamente del programa, coloque 2")
                                    eleccion57 = int(input("Coloque la opción elegida: "))
                                    if eleccion57 == 1:
                                        continuar = True
                                    else:
                                        continuar = False
                    else:
                        print("")
                        eleccion34=int(input("¿cuanto desea agregar? "))      
                        galones5=eleccion34/fdepositoD    
                        fdepositoD=fdepositoD-galones5     
                        if fdepositoD<0:
                            fdepositoD=fdepositoD++galones5
                            print("No puede continuar con la compra debido a que el deposito tiene bajo nivel de galones ")
                            print("¿Desea regresar a menú?")
                            print("Si desea regresar a menú, coloque 1")
                            print("Si desea salir definitivamente del programa, coloque 2")
                            eleccion35=int(input("Coloque la opcion elegida: "))
                            if eleccion35==1:
                                continuar=True
                            else: 
                                continuar=False
                        else:
                            if fdepositoD>=0:
                                print("")
                                nombrecliente6=input("Ingrese su nombre completo:")
                                nit6=input("Ingrese su número de NIT: ")
                                nobomba6=input("Ingrese el número de a utilizar (un número entre 1 y 4): ")
                                print("")
                                print("-------------------RESUMEN DE SU COMPRA-------------------")
                                print("Nombre del cliente: ",nombrecliente6)
                                print("NIT: ",nit6)
                                print("Total a pagar: Q.",eleccion34)
                                print("----------------------------------------------------------------------------")
                                print("")
                                print("Si desea continuar con su compra, coloque 1")
                                print("Si desea cancelar su compra, coloque 2")
                                eleccion58 = int(input("¿Desea continuar con su compra?: "))
                                if eleccion58 == 1:
                                    print("")
                                    targetanum6 = int(input("Ingrese el número de su tarjeta para realizar el cobro: "))
                                    targeta6=targetanum6
                                    if targetanum6 == targeta6:
                                        print("¡Su compra fue realizada con éxito!")
                                    else:
                                        print("Número de tarjeta inválido. Intente nuevamente.")
                                else:
                                    print("")
                                    print("¿Desea regresar a menú?")
                                    print("Si desea regresar a menú, coloque 1")
                                    print("Si desea salir definitivamente del programa, coloque 2")
                                    eleccion59 = int(input("Coloque la opción elegida: "))
                                    if eleccion59 == 1:
                                        continuar = True
                                    else:
                                        continuar = False