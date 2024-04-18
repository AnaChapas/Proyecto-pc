#VARIABLES GENERALES
#Cantidad inicial en cada deposito
depositoR=40
depositoS=40
depositoD=40
#Costos de gestion de inventario 
costoregular = 7.00
costosuper = 8.00
costodiesel = 6.00
#Precios de gasolina
Pregular=29.00
Psuper=30.00
Pdiesel=26.50
#Capacidad maxima de galones:
capacidad_maxima = 80
#Variables de gestion de turnos
tradiurna=1
travespe=1
tranoc=1
saldi=14.00
salves=14.50
salnoc=15.50
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
    if eleccion==1:
        print("Menú:")
        print("1. Gestionar inventario")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("Nivel de los depósitos:")
            print(f"Regular: {depositoR} galones")
            print(f"Súper: {depositoS} galones")
            print(f"Diésel: {depositoD} galones")

            agregar_combustible = input("¿Desea agregar combustible? (s/n): ")

            if agregar_combustible.lower() == 's':
                cantregular = float(input("Ingrese la cantidad de galones de gasolina regular: "))
                fdepositoR=depositoR++cantregular
                if fdepositoR <= capacidad_maxima:
                    fcostoR = (cantregular * costoregular)
                else:
                    fdepositoR=depositoR
                    print("Operación inválida. La cantidad excede la capacidad del depósito de gasolina regular.")
                    fcostoR = 0
                
                cantsuper = float(input("Ingrese la cantidad de galones de gasolina súper: "))
                fdepositoS=depositoS++cantsuper
                if fdepositoS <= capacidad_maxima:
                    fcostoS = (cantsuper * costosuper)
                else:
                    fdepositoS=depositoS
                    print("Operación inválida. La cantidad excede la capacidad del depósito de gasolina súper.")
                    fcostoS = 0
            
                cantdiesel = float(input("Ingrese la cantidad de galones de diésel: "))
                fdepositoD=depositoD++cantdiesel
                if fdepositoD <= capacidad_maxima:
                    fcostoD = (cantdiesel * costodiesel)                  
                else:
                    fdepositoD=depositoD
                    print("Operación inválida. La cantidad excede la capacidad del depósito de diésel.")
                    fcostoD = 0
                         
                print(f"Se agregó combustible:")
                print(f"Costo de almacenamiento de gasolina regular: Q{fcostoR:.2f}")
                print(f"Costo de almacenamiento de gasolina súper: Q{fcostoS:.2f}")
                print(f"Costo de almacenamiento de diésel: Q{fcostoD:.2f}")

        elif opcion == '2':
            print("Gracias por utilizar nuestros servicios, vuelva pronto")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

#Codigo de venta de combustible
    elif eleccion == 2:
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
                                    fdepositoR=fdepositoR++eleccion4
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
                        galones1=eleccion10/Pregular  
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
                                    fdepositoR=fdepositoR++galones1
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
                                        fdepositoS=fdepositoS++eleccion17
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
                            galones3=eleccion23/Psuper 
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
                                        fdepositoS=fdepositoS++galones3
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
                                    fdepositoD=fdepositoD++eleccion29
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
                        galones5=eleccion34/Pdiesel   
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
                                    fdepositoD=fdepositoD++galones5
                                    print("")
                                    print("¿Desea regresar a menú?")
                                    print("Si desea regresar a menú, coloque 1")
                                    print("Si desea salir definitivamente del programa, coloque 2")
                                    eleccion59 = int(input("Coloque la opción elegida: "))
                                    if eleccion59 == 1:
                                        continuar = True
                                    else:
                                        continuar = False
#Codigo de gestión de turnos
    elif eleccion==3:
        print("")
        print("--------------------------Gestión de turnos-------------------------------")
        print("--------Tipo de jornada------------------------Total de trabajadores------")
        print("----------- Diurna -------------------------------- ",tradiurna," --------")
        print("--------- Vespertina ------------------------------ ",travespe," ---------")
        print("---------- Nocturna ------------------------------- ",tranoc," -----------")
        print("--------------------------------------------------------------------------")
        print("")
        print("¿Desea agregar o retirar personal a alguna jornada?")
        print("Si desea agregar personal, coloque 1")
        print("Si desea retirar personal, coloque 2")
        per= int(input(" Coloque la opcion elegida: "))
        if per==1:
            print("")
            per1=int(input("¿Cuantas personas desea agregar a la jornada diurna?: "))
            tradiurna=per1++tradiurna
            per2=int(input("¿Cuantas personas desea agregar a la jornada vespertina?: "))
            travespe=travespe++per2
            per3=int(input("¿Cuantas personas desea agregar a la jornada nocturna?:"))
            tranoc=per3++tranoc
            print("")
            print("----------------------------Costos de los trabajadores-----------------------------")
            print("-----------Horarios------------Tipo de jornada------------Salario por jornada------")
            print("------ 12:00 AM - 8:00 AM --------- Diurna ------------------- ",saldi," ----------")
            print("------ 8:00 AM - 4:00 PM --------- Vespertina --------------- ",salves," ----------")
            print("------ 4:00 PM - 12:00 AM --------- Nocturna ---------------- ",salnoc," ----------")
            print("-----------------------------------------------------------------------------------")
            print("¿Desea regresar a menú?")
            print("Si desea regresar a menú, coloque 1")
            print("Si desea salir definitivamente del programa, coloque 2")
            print("Si desea salir definitivamente del programa, coloque 2")
            eleccion60=int(input("Coloque la opcion elegida: "))
            if eleccion60==1:
                continuar=True
            else:
                continuar=False
 
        else:
            print("")
            per4=int(input("¿Cuantas personas desea retirar de la jornada diurna?: "))
            tradiurna=tradiurna-per4
            if tradiurna<=0:
                tradiurna=tradiurna++per4
                print("La cantidad de empleados que desea retirar no es permitida")
            else:
                tradiurna
            
            per6=int(input("¿Cuantas personas desea retirar de la jornada vespertina?: "))
            travespe=travespe-per6
            if travespe<=0:
                travespe=travespe++per6
                print("La cantidad de empleados que desea retirar no es permitida")
            else:
                travespe

            per8=int(input("¿Cuantas personas desea retirar de la jornada Nocturna?: "))
            tranoc=tranoc-per8
            if tranoc<=0:
                tranoc=tranoc++per8
                print("La cantidad de empleados que desea retirar no es permitida")
            else:
                tranoc
                
            print("")
            print("----------------------------Costos de los trabajadores-----------------------------")
            print("-----------Horarios------------Tipo de jornada------------Salario por jornada------")
            print("------ 12:00 AM - 8:00 AM --------- Diurna ------------------- ",saldi," ----------")
            print("------ 8:00 AM - 4:00 PM --------- Vespertina --------------- ",salves," ----------")
            print("------ 4:00 PM - 12:00 AM --------- Nocturna ---------------- ",salnoc," ----------")
            print("-----------------------------------------------------------------------------------")
            print("")
            print("¿Desea regresar a menú?")
            print("Si desea regresar a menú, coloque 1")
            print("Si desea salir definitivamente del programa, coloque 2")
            eleccion70=int(input("Coloque la opcion elegida: "))
            if eleccion70==1:
                continuar=True
            else:
                continuar=False
#Codigo de reporte de rentabilidad
    else:
        print("")