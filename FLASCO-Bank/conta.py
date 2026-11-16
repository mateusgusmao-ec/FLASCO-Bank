#extrato,saldo,deposito,saque
#BASEADO NAS FUNÇOES MAIN.PY
from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, numero, cliente, saldo=0.0):
        self.numero = str(numero)
        self.cliente = cliente
        self.saldo = float(saldo)

    @property
    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def sacar(self, valor):
        if valor > 0 :
            self.saldo += float(valor)
            return True
        return False

    def to_dict(self):
        return {
            "numero" : self.numero,
            "cpf_cliente" : self.cliente.cpf,
            "tipo" : self.tipo,
            "saldo" : self.saldo
        }

class ContaCorrente(Conta):
    @property
    def tipo(self):
        return "corrente"

    def sacar(self, valor):
        valor = float(valor)
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

class ContaPoupança(Conta):
    @property
    def tipo(self):
        return "poupança"
    def sacar(self, valor):
        valor = float(valor)
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def render_juros(self, taxa=0.005):
        if self.saldo > 0:
            self.saldo += self.saldo * taxa