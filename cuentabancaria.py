#Esta clase representa la clase cuenta bancaria que va a a recibir 4 atributos 
class CuentaBancaria:
    def __init__ (self, nroCuenta, saldo):
        self.nroCuenta = nroCuenta
        self.saldo = saldo

    #Este metodo devuelve el saldo de una cuenta bancaria 
    def ver_saldo(self):
        return self.saldo

    #Este metodo devuelve el numero de la cuenta bancaria
    def vercuenta(self):
        return self.nroCuenta

    #Este metodo permite realizar la extraccion de dinero de una cuenta, para luego si usa el metodo depositar (self,x), ser transferido a otra cuenta
    def extraer(self, x):
        tot = self.saldo
        total = tot - x 
        self.saldo = total

    #Este metodo recibe un valor a depositar (x) y lo descuenta del saldo total de la cuenta bancaria
    def depositar(self,x):
        tot = self.saldo
        nuevo = tot + x
        self.saldo = nuevo
