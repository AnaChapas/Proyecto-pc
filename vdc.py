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
                        galones=fdepositoR-eleccion4               
                        if galones<0:
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
                            if galones>=0:
                                nombrecliente1=input("Ingrese su nombre completo:")
                                nit1=input("Ingrese su número de NIT: ")
                                nobomba1=input("Ingrese el número de a utilizar (un número entre 1 y 4)")
                                print("")
                                print("-------------------RESUMEN DE SU COMPRA-------------------")
                                print("Nombre del cliente: ",nombrecliente1)
                                print("NIT: ",nit1)
                                totalconsum1=galones*Pregular
                                print("Total a pagar: Q.",totalconsum1)
                                print("----------------------------------------------------------------------------")
                                print("")
                                print("Si desea continuar con su compra, coloque 1")
                                print("Si desea cancelar su compra, coloque 2")
                                eleccion6=input("¿Desea continuar con su compra")
                                if eleccion6==1:
                                    targetanum1=int(input("Ingrese el número de su targeta para realizar el cobro: "))
                                    if targetanum1==targetanum1:
                                        print("¡Su compra fue realizada con exito!")
                                        print("¿Desea factura?")
                                        print("Si desea factura, coloque 1 ")
                                        print("Si no desea factura coloque 2")
                                        eleccion7=int(input("Coloque la opcion elegida: "))
                                        if eleccion7==1:
                                            print("")
                                            print("---------------------------FACTURA--------------------------")
                                            print("--Datos del certificado--")
                                            print("NIT:7745452-0")
                                            print("Gasolineras Jaguar, S.A.")
                                            print("--Datos del cliente--")
                                            print("Nombre del cliente: ",nombrecliente1)
                                            print("NIT: ",nit1)
                                            print("Total a pagar: Q.",totalconsum1)
                                            print("--Datos del cliente--")
                                            print("Se hecharon ",galones, " galones de regular")
                                            print("----------------------------------------------------------------------------")
                                            print("")
                                            print("¿Desea regresar a menú?")
                                            print("Si desea regresar a menú, coloque 1")
                                            print("Si desea salir definitivamente del programa, coloque 2")
                                            eleccion8=int(input("Coloque la opcion elegida: "))
                                            if eleccion8==1:
                                                continuar=True
                                            else: 
                                                continuar=False
                                        else:   
                                            if eleccion7==2:
                                                continuar=True
                                            else: 
                                                continuar=False    

                                else:
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
                        eleccion10=int(input("¿cuanto desea agregar? "))      
                        galones1=eleccion10/fdepositoR          
                        if galones1<0:
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
                             if galones1>=0:
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
                                eleccion12=input("¿Desea continuar con su compra? ")
                                if eleccion12==1:
                                    print("")
                                    targetanum2=int(input("Ingrese el número de su targeta para realizar el cobro: "))
                                    if targetanum2==targetanum2:
                                        print("¡Su compra fue realizada con exito!")
                                        print("¿Desea factura?")
                                        print("Si desea factura, coloque 1 ")
                                        print("Si no desea factura coloque 2")
                                        eleccion13=int(input("Coloque la opcion elegida: "))
                                        if eleccion13==1:
                                            print("---------------------------FACTURA--------------------------")
                                            print("--Datos del certificado--")
                                            print("NIT:7745452-0")
                                            print("Gasolineras Jaguar, S.A.")
                                            print("--Datos del cliente--")
                                            print("Nombre del cliente: ",nombrecliente2)
                                            print("NIT: ",nit2)
                                            print("Total a pagar: Q.",eleccion2)
                                            print("--Datos del cliente--")
                                            print("Se hecharon ",galones1, " galones de regular")
                                            print("----------------------------------------------------------------------------")
                                            print("¿Desea regresar a menú?")
                                            print("Si desea regresar a menú, coloque 1")
                                            print("Si desea salir definitivamente del programa, coloque 2")
                                            eleccion14=int(input("Coloque la opcion elegida: "))
                                            if eleccion14==1:
                                                continuar=True
                                            else: 
                                                continuar=False
                                else:
                                    if eleccion12==2:
                                        continuar=True
                                    else: 
                                        continuar=False
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
                            eleccion17=int(input("¿cuantos galones desea agregar? "))      
                            galones2=fdepositoS-eleccion17
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
                            if galones2>=0:
                                print("")
                                nombrecliente3=input("Ingrese su nombre completo: ")
                                nit3=input("Ingrese su número de NIT: ")
                                nobomba3=input("Ingrese el número de a utilizar (un número entre 1 y 4): ")
                                print("")
                                print("-------------------RESUMEN DE SU COMPRA-------------------")
                                print("Nombre del cliente: ",nombrecliente3)
                                print("NIT: ",nit3)
                                totalconsum3=galones*Pregular
                                print("Total a pagar: Q.",totalconsum3)
                                print("----------------------------------------------------------------------------")
                                print("")
                                print("Si desea continuar con su compra, coloque 1")
                                print("Si desea cancelar su compra, coloque 2")
                                eleccion19=input("¿Desea continuar con su compra?")
                                if eleccion19==1:
                                    print("")
                                    targetanum3=int(input("Ingrese el número de su targeta para realizar el cobro: "))
                                    if targetanum3==targetanum3:
                                        print("")
                                        print("¡Su compra fue realizada con exito!")
                                        print("¿Desea factura?")
                                        print("Si desea factura, coloque 1 ")
                                        print("Si no desea factura coloque 2")
                                        eleccion20=int(input("Coloque la opcion elegida: "))
                                        if eleccion20==1:
                                            print("")
                                            print("---------------------------FACTURA--------------------------")
                                            print("--Datos del certificado--")
                                            print("NIT:7745452-0")
                                            print("Gasolineras Jaguar, S.A.")
                                            print("--Datos del cliente--")
                                            print("Nombre del cliente: ",nombrecliente3)
                                            print("NIT: ",nit3)
                                            print("Total a pagar: Q.",totalconsum3)
                                            print("--Datos del cliente--")
                                            print("Se hecharon ",galones2, " galones de super")
                                            print("----------------------------------------------------------------------------")
                                            print("")
                                            print("¿Desea regresar a menú?")
                                            print("Si desea regresar a menú, coloque 1")
                                            print("Si desea salir definitivamente del programa, coloque 2")
                                            eleccion21=int(input("Coloque la opcion elegida: "))
                                            if eleccion21==1:
                                                continuar=True
                                            else: 
                                                continuar=False

                                    else:
                                        print("")
                                        print("¿Desea regresar a menú?")
                                        print("Si desea regresar a menú, coloque 1")
                                        print("Si desea salir definitivamente del programa, coloque 2")
                                        eleccion22=int(input("Coloque la opcion elegida: "))
                                        if eleccion22==1:
                                            continuar=True
                                        else: 
                                            continuar=False
                            else:
                                print("")
                                eleccion23=int(input("¿cuanto desea agregar? "))      
                                galones3=eleccion23/fdepositoS          
                                if galones3<0:
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
                                    if galones3>=0:
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
                                        eleccion24=input("¿Desea continuar con su compra?")
                                        if eleccion24==1:
                                            targetanum4=int(input("Ingrese el número de su targeta para realizar el cobro: "))
                                            if targetanum4==targetanum4:
                                                print("¡Su compra fue realizada con exito!")
                                                print("¿Desea factura?")
                                                print("Si desea factura, coloque 1 ")
                                                print("Si no desea factura coloque 2")
                                                eleccion25=int(input("Coloque la opcion elegida: "))
                                                if eleccion25==1:
                                                    print("")
                                                    print("---------------------------FACTURA--------------------------")
                                                    print("--Datos del certificado--")
                                                    print("NIT:7745452-0")
                                                    print("Gasolineras Jaguar, S.A.")
                                                    print("--Datos del cliente--")
                                                    print("Nombre del cliente: ",nombrecliente4)
                                                    print("NIT: ",nit4)
                                                    print("Total a pagar: Q.",eleccion4)
                                                    print("--Datos del cliente--")
                                                    print("Se hecharon ",galones3, " galones de super")
                                                    print("----------------------------------------------------------------------------")
                                                    print("")
                                                    print("¿Desea regresar a menú?")
                                                    print("Si desea regresar a menú, coloque 1")
                                                    print("Si desea salir definitivamente del programa, coloque 2")
                                                    eleccion26=int(input("Coloque la opcion elegida: "))
                                                    if eleccion26==1:
                                                        continuar=True
                                                    else: 
                                                        continuar=False
                                        else:
                                            if eleccion24==2:
                                                continuar=True
                                            else: 
                                                continuar=False
                
                #Si se escoge la opcion 3 se realizara lo siguiente:     
            else:
                if tipocombustible==3:    
                    if fdepositoD <=5:
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
                            galones4=fdepositoD-eleccion29               
                            if galones4<0:
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
                                if galones4>=0:
                                    print("")
                                    nombrecliente5=input("Ingrese su nombre completo:")
                                    nit5=input("Ingrese su número de NIT: ")
                                    nobomba5=input("Ingrese el número de a utilizar (un número entre 1 y 4): ")
                                    print("-------------------RESUMEN DE SU COMPRA-------------------")
                                    print("Nombre del cliente: ",nombrecliente5)
                                    print("NIT: ",nit5)
                                    totalconsum5=galones4*Pregular
                                    print("Total a pagar: Q.",totalconsum5)
                                    print("----------------------------------------------------------------------------")
                                    print("")
                                    print("Si desea continuar con su compra, coloque 1")
                                    print("Si desea cancelar su compra, coloque 2")
                                    eleccion30=input("¿Desea continuar con su compra?")
                                    if eleccion30==1:
                                        targetanum5=int(input("Ingrese el número de su targeta para realizar el cobro: "))
                                        if targetanum5==targetanum5:
                                            print("¡Su compra fue realizada con exito!")
                                            print("")
                                            print("¿Desea factura?")
                                            print("Si desea factura, coloque 1 ")
                                            print("Si no desea factura coloque 2")
                                            eleccion31=int(input("Coloque la opcion elegida: "))
                                            if eleccion31==1:
                                                print("")
                                                print("---------------------------FACTURA--------------------------")
                                                print("--Datos del certificado--")
                                                print("NIT:7745452-0")
                                                print("Gasolineras Jaguar, S.A.")
                                                print("--Datos del cliente--")
                                                print("Nombre del cliente: ",nombrecliente5)
                                                print("NIT: ",nit5)
                                                print("Total a pagar: Q.",totalconsum5)
                                                print("--Datos del cliente--")
                                                print("Se hecharon ",galones4, " galones de diesel")
                                                print("----------------------------------------------------------------------------")
                                                print("")
                                                print("¿Desea regresar a menú?")
                                                print("Si desea regresar a menú, coloque 1")
                                                print("Si desea salir definitivamente del programa, coloque 2")
                                                eleccion32=int(input("Coloque la opcion elegida: "))
                                                if eleccion32==1:
                                                    continuar=True
                                                else: 
                                                    continuar=False

                                    else:
                                        print("")
                                        print("¿Desea regresar a menú?")
                                        print("Si desea regresar a menú, coloque 1")
                                        print("Si desea salir definitivamente del programa, coloque 2")
                                        eleccion33=int(input("Coloque la opcion elegida: "))
                                        if eleccion33==1:
                                            continuar=True
                                        else: 
                                            continuar=False
                        else:
                            print("")
                            eleccion34=int(input("¿cuanto desea agregar? "))      
                            galones5=eleccion34/fdepositoD          
                            if galones5<0:
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
                                if galones5>=0:
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
                                    eleccion36=input("¿Desea continuar con su compra?")
                                    if eleccion36==1:
                                        print("")
                                        targetanum6=int(input("Ingrese el número de su targeta para realizar el cobro: "))
                                        if targetanum6==targetanum6:
                                            print("¡Su compra fue realizada con exito!")
                                            print("¿Desea factura?")
                                            print("Si desea factura, coloque 1 ")
                                            print("Si no desea factura coloque 2")
                                            eleccion37=int(input("Coloque la opcion elegida: "))
                                            if eleccion37==1:
                                                print("")
                                                print("---------------------------FACTURA--------------------------")
                                                print("--Datos del certificado--")
                                                print("NIT:7745452-0")
                                                print("Gasolineras Jaguar, S.A.")
                                                print("--Datos del cliente--")
                                                print("Nombre del cliente: ",nombrecliente6)
                                                print("NIT: ",nit6)
                                                print("Total a pagar: Q.",eleccion34)
                                                print("--Datos del cliente--")
                                                print("Se hecharon ",galones5, " galones de diesel")
                                                print("----------------------------------------------------------------------------")
                                                print("")
                                                print("¿Desea regresar a menú?")
                                                print("Si desea regresar a menú, coloque 1")
                                                print("Si desea salir definitivamente del programa, coloque 2")
                                                eleccion38=int(input("Coloque la opcion elegida: "))
                                                if eleccion38==1:
                                                    continuar=True
                                                else: 
                                                    continuar=False
