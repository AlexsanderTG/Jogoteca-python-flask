

def criar_conta(numero, titular, saldo, limite, conta=None):
    conta = {"Numero": numero, "Titular": titular, "Saldo": saldo, "Limite": limite}
    return conta

def deposita(conta, valor):
    conta["Saldo"] += valor


def saca(conta, valor):
   conta["Saldo"]-= valor

def extrato(conta):
    print("Saldo é {}".format(conta["Saldo"]))

