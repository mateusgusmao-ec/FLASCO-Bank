#extrato,saldo,deposito,saque
#BASEADO NAS FUNÇOES MAIN.PY
def exibir_conta(numeroDaConta,saldoConta):
    resultado = f"NÚMERO DA CONTA : '{numeroDaConta}'\nSALDO DA CONTA : '{saldoConta}'"
    return resultado

def depositar(saldoConta,valor_deposito):
    if valor_deposito > 0:
        novoSaldo = saldoConta + valor_deposito
        return True, novoSaldo
    else:
        return False,saldoConta
    
def sacar(saldoConta, valor_saque):
    if valor_saque > 0 and saldoConta >= valor_saque:
        novoSaldo = saldoConta - valor_saque
        return True, novoSaldo
    else:
        return False, saldoConta
