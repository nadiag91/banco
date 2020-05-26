from cuentabancaria import CuentaBancaria


def buscar_cuenta(apellido):
  posicion = -1 
  encontrado = False
  for cuenta in lista_cuentas_bancarias:
    if(apellido == cuenta.ver_apellido()):
      posicion = lista_cuentas_bancarias.index(cuenta)
      encontrado = True
  
  return posicion,encontrado
    

def validar_saldo(monto, posicion):
  saldo_mayor_a_monto = False
  if lista_cuentas_bancarias[posicionA].ver_saldo() >= monto:
    saldo_mayor_a_monto = True
  
  return saldo_mayor_a_monto

  
def transferencia(posicionA,posicionB,monto):
  transferencia_hecha = False
  if validar_saldo(monto_transferido, cuenta_origen) == True:
    lista_cuentas_bancarias[posicionA].extraer(monto_transferido)
    lista_cuentas_bancarias[posicionB].depositar(monto_transferido)
    transferencia_hecha = True
  
  return transferencia_hecha
  
      
lista_cuentas_bancarias = []
c1 = CuentaBancaria(1234,"asd","12312",100)
c2 = CuentaBancaria(1233,"qwe","12123",200)
c3 = CuentaBancaria(1235,"zxc","12123",300)
c4 = CuentaBancaria(1235,"fgh","12123",400)
lista_cuentas_bancarias.append(c1)
lista_cuentas_bancarias.append(c2)
lista_cuentas_bancarias.append(c3)
lista_cuentas_bancarias.append(c4)


Apellido = input('Ingrese apellido de la cuenta a extraer: ')

posicionA, existenciaA = buscar_cuenta(Apellido)
print(posicionA,existenciaA)

cuenta_origen = posicionA


if posicionA != -1:
  print("la encontré")
else:
  print("no la encontre")

if existenciaA == False:
  print("La cuenta no pudo ser encontrada")
else: 
  print("La posicion encontrada es: {}".format(cuenta_origen))

  print("El número de la cuenta encontrada es: {}".format(lista_cuentas_bancarias[cuenta_origen].vercuenta()))

  print("El saldo de la cuenta encontrada es: {}".format(lista_cuentas_bancarias[cuenta_origen].ver_saldo()))
  
  
  Apellido2 = input('Ingrese apellido de la cuenta a depositar: ')
  
  posicionB,existenciaB = buscar_cuenta(Apellido2)
  cuenta_destino = posicionB

  if (existenciaB == False):
    print("La cuenta no fue encontrada")
  else:
    print("La posicion encontrada es: {}".format(cuenta_destino))

    print("El número de la cuenta encontrada es: {}".format(lista_cuentas_bancarias[cuenta_destino].vercuenta()))

    print("El saldo de la cuenta encontrada es: {}".format(lista_cuentas_bancarias[cuenta_destino].ver_saldo()))
  

    valor = int(input("Ingrese el monto a transferir: "))
    monto = valor
    monto_transferido = monto
    verificar_monto = validar_saldo(monto_transferido, cuenta_origen)

    if verificar_monto == False:
      print("Saldo insuficiente")
    else:
      transferencia_hecha = transferencia(cuenta_origen, cuenta_destino, monto_transferido)
    
      if transferencia_hecha == True:
        print("Transferencia exitosa. El nuevo saldo en su cuenta destino es: {}".format(lista_cuentas_bancarias[cuenta_destino].ver_saldo()))
      
          


'''
#Esta funcion recibe como parametro un apellido a buscar. Recorre la lista de cuentas bancarias guardadas y devuelve la posición de ese objeto
#Se considera posicion=-1 para que en caso que no sea true, devuelva la posicion del objeto en la lista_cuentas_bancarias
def buscar_cuenta(apellido):
  posicion = -1
  for cuenta in lista_cuentas_bancarias:
    if(apellido == cuenta.ver_apellido()):
      posicion = lista_cuentas_bancarias.index(cuenta)
  return posicion





#Se cargan 2 objetos, c1 y c2, a la lista, lista_cuentas_bancarias = [], para poder probar la función buscar_cuenta y los metodos de clase
lista_cuentas_bancarias = []
c1 = CuentaBancaria(1234,"garcia","12312",100)
c2 = CuentaBancaria(1233,"gomez","12123",200)
lista_cuentas_bancarias.append(c1)
lista_cuentas_bancarias.append(c2)


pregunta = int(input("Bienvenido! Elija la opción deseada\n1: Buscar cuenta\n2: Depósito\n3: Transferencias\n4:Salir\n"))

while(True):
  if (pregunta == 1):
    Apellido = input('Ingrese apellido de la cuenta: ')
    buscar_cuenta(Apellido)
    busqueda = buscar_cuenta(Apellido)

    if (busqueda == -1):
      print("La cuenta no fue encontrada")
    else:
      print("La posicion encontrada es: {}".format(busqueda))

      print("El número de la cuenta encontrada es: {}".format(lista_cuentas_bancarias[busqueda].vercuenta()))

      print("El saldo de la cuenta encontrada es: {}".format(lista_cuentas_bancarias[busqueda].ver_saldo()))
      break

  if (pregunta == 2):
    #En Depositar, primero se realiza la busqueda de la cuenta a que se quiere depositar a traves de la funcion buscar_cuenta(apellido)
    Apellido = input('Ingrese apellido de la cuenta de donde desea extraer el dinero: ')
    buscar_cuenta(Apellido)
    busqueda1 = buscar_cuenta(Apellido)
    if (busqueda1 == -1):
      print("La cuenta no fue encontrada")
    else:
      print("El número de la cuenta encontrada es: {}".format(lista_cuentas_bancarias[busqueda1].vercuenta()))

      print("El saldo de la cuenta encontrada es: {}".format(lista_cuentas_bancarias[busqueda1].ver_saldo()))

      #Se determina el valor a depositar que sera usado en el metodo depositar()
      valor_a_depositar = int(input("Ingrese el monto que desea depositar: "))
      lista_cuentas_bancarias[busqueda].depositar(valor_a_depositar)
      print("El nuevo saldo de su cuenta es {}".format(lista_cuentas_bancarias[busqueda].ver_saldo()))
      break

  if (pregunta == 3):
    #Se buscan dos cuentas, buscar_cuenta(Apellido_cuenta1) devuelve la cuenta desde donde se extraera el dinero
    Apellido_cuenta1 = input('Ingrese el apellido de la cuenta de donde se extraerá el dinero: ')
    buscar_cuenta(Apellido_cuenta1)
    busqueda2 = buscar_cuenta(Apellido_cuenta1)
    if (busqueda2 == -1):
      print("La cuenta no fue encontrada")
    else:
      print("El numero de la cuenta registrada es: {}".format(lista_cuentas_bancarias[busqueda2].vercuenta()))

      print("El saldo de la cuenta es: {}".format(lista_cuentas_bancarias[busqueda2].ver_saldo()))

      valor_a_transferir = int(input("Ingrese el valor a extraer "))
      #Con la funcion buscar_cuenta(Apellido_cuenta2), se encuentra la cuenta a la que se transferira el dinero especificado en valor_a_transferir
      Apellido_cuenta2 = input('Ingrese el apellido de la cuenta a la que se transferirá el dinero: ')
      buscar_cuenta(Apellido_cuenta2)
      busqueda3 = buscar_cuenta(Apellido_cuenta2)
      lista_cuentas_bancarias[busqueda2].extraer(valor_a_transferir)
      lista_cuentas_bancarias[busqueda3].depositar(valor_a_transferir)
      print("Transferencia exitosa. El nuevo saldo de su cuenta es {} ".format(lista_cuentas_bancarias[busqueda3].ver_saldo()))
      break
  if (pregunta == 4):
    print ("Operación finalizada")
    break




#OPCION 1
lista_cuentas_bancarias = []
def crear_cuentas():
    n = int(input("cuantas cuentas desea crear?: "))
    for x in range(n):
        num_cuenta = input('Ingrese el numero de cuenta')
        apellido = input('Ingrese el apellido del cliente')
        num_dni = input('Ingrese el numero de dni')
        saldo = int(input('Ingrese el saldo inicial'))
        nueva_cuenta = CuentaBancaria(num_cuenta,apellido,num_dni,saldo)
        lista_cuentas_bancarias.append(nueva_cuenta)
        print ("La cuenta ha sido creada correctamente")        


#OPCION 2
def transferir():
    cuenta_a_extraer = input("Ingrese el número de cuenta de la que se extrae el dinero: ")
    cuenta_a_depositar = input("Ingrese el número de cuenta a la que se transfiere el dinero: ")
    for cuenta in lista_cuentas_bancarias:
        if (cuenta.vercuenta() == cuenta_a_extraer): 
            print("El saldo de la cuent a extraer es: {}".format(cuenta.ver_saldo()))
            valor_de_extraccion = int(input("Ingrese el valor a extraer "))
            cuenta.extraer(valor_de_extraccion)
            for cuenta2 in lista_cuentas_bancarias:
                if (cuenta2.vercuenta() == cuenta_a_depositar):
                    cuenta2.depositar(valor_de_extraccion)
                    print("El nuevo saldo de su cuenta es {} ".format(cuenta2.ver_saldo()))
                    break

    
    if (cuenta.vercuenta() != cuenta_a_buscar) or (cuenta2.vercuenta() != cuenta_a_depositar):
      error = int(input("Número de cuenta no encontrado. Intentelo de nuevo. Ingrese 0 para repetir, 3 para salir"))
    if (error == 0):
      transferir()
    if (error == 3):
      salir()
      




while(True):
    opciones = input("Ingrese 1 para crear cuentas, 2 para transferir, 3 para salir ")

    if (opciones == "1"):
        crear_cuentas()
        transferir()
    if (opciones == "2"):
        transferir()
    if (opciones == "3"):
        print("Operación finalizada")
        break
    

 '''


