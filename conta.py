#extrato,saldo,deposito,saque
#BASEADO NAS FUNÇOES MAIN.PY
def exibir_conta(numeroConta,saldoConta):
    resultado = f"NÚMERO DA CONTA : '{numeroConta}'\nSALDO DA CONTA : '{saldoConta}'"
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

def transferir(saldoConta, valor_deposito):

def criar_contaS(numeroConta):
    contas = []
    

def listar_contas(contas):
    print("\n--- CONTAS ---")

    for conta in contas:
        print("Número da conta:", conta[0])
        print("CPF do cliente:", conta[1])
        print("Saldo:", conta[2])
        print()

def consultar_saldo(cpf, numeroConta):
    cpf = int(input("Digite o CPF: "))
    conta = buscar_conta_por_cpf(contas, cpf)

    if conta != None:
        print(saldoConta(conta[0], conta[2]))
    else:
        print("Conta não encontrada.")
