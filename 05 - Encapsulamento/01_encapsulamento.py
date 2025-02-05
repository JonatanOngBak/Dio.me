class Conta:
    def __init__(self, nro.agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro.agencia

    def depositar(self, valor):
        #...
        self.saldo += valor

    def sacar(self, valor):
        # ... 
        self._saldo -= valor

    def mostra_saldo(self):
        return self._saldo

conta = Conta("0001", 100)
conta.depositar(100)

print(conta.mostra_saldo())