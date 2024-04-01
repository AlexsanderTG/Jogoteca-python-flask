class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def extrato(self):
        print("Saldo é {}".format(self.saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.depositar(valor)
    @property
    def saldo(self):
        return self.saldo
    @property
    def titular(self):
        return self.titular()

    @property
    def limite(self):
        return self.limite
    @limite.setter
    def limite(self,limite):
        self.limite = limite

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


if __name__ == '__main__':
    conta1 = Conta(123, "Henrique", 55.0, 1000.0)
    conta1.extrato()
    conta1.depositar(250)
    conta1.extrato()
    conta1.sacar(150)
    conta1.extrato()
