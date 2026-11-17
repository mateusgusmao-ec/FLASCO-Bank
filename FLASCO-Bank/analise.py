from functools import reduce
class AnaliseFinanceira:
    def __init__(self, agencia):
        self.agencia = agencia

    def obter_contas_saldo_positivo(self):
        return list(filter(lambda c: c.saldo > 0, self.agencia.contas))

    def calcular_saldo_total(self):
        return reduce(lambda acum, c: acum + c.saldo, self.agencia.contas, 0.0)

    def encontrar_maior_saldo(self):
        if not self.agencia.contas:
            return 0.0
        return max(self.agencia.contas, key=lambda c: c.saldo).saldo

    def encontrar_menor_saldo(self):
        if not self.agencia.contas:
            return 0.0
        return min(self.agencia.contas, key=lambda c: c.saldo).saldo

    def gerar_dashboard(self):
        qtd_contas = len(self.agencia.contas)
        saldo_total = self.calcular_saldo_total()
        maior_saldo = self.encontrar_maior_saldo()
        menor_saldo = self.encontrar_menor_saldo()
        saldo_medio = (saldo_total / qtd_contas) if qtd_contas > 0 else 0.0

        return {
            "agencia": self.agencia,
            "numero_clientes": len(self.agencia.clientes),
            "numero_contas": qtd_contas,
            "saldo_total": round(saldo_total, 2),
            "maior_saldo": round(maior_saldo, 2),
            "menor_saldo": round(menor_saldo, 2),
            "saldo_medio": round(saldo_medio, 2),
            "clientes": self.agencia.clientes,
            "contas": self.agencia.contas,
            "contas_positivas": self.obter_contas_saldo_positivo()
        }