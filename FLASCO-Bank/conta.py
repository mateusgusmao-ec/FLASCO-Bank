#extrato,saldo,deposito,saque
#BASEADO NAS FUNÇOES MAIN.PY
def exibir_conta(numeroConta,saldoConta):
    resultado = f"NÚMERO DA CONTA : '{numeroConta}'\nSALDO DA CONTA : '{saldoConta}'"  # printa os dados da conta
    return resultado

def depositar(contas):
    numero = input("Digite o número da conta : ")
    if numero not in contas :
        print("Conta não encontrada")
        return

    valor = float(input("Digite o valor de depósito : "))
    if valor > 0 :
        contas[numero]['saldo'] += valor
        print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo : R$ {contas[numero]['saldo']:.2f}")
    else :
        print("Valor inválido")

    
def sacar(contas):
    numero = input("Digite o número da conta : ")
    if numero not in contas :
        print("Conta não encontrada")
        return
    
    valor = float(input("Digite o valor de saque : "))
    if valor > 0 and contas[numero]['saldo'] >= valor :
        contas[numero]['saldo'] -= valor
        print(f"Saque de R$ {valor:.2f} realizado. Novo saldo : R$ {contas[numero]['saldo']:.2f}")
    else :
        print("Valor inválido ou saldo inválido")
    

def transferir(contas):
    origem = input("Digite o número da sua conta (origem) : ")
    destino = input("Digite o número da conta de destino : ")


    if origem not in contas or destino not in contas :
        print("Conta de origem ou destino não encontrada")
        return

    valor = float(input("Digite o valor de transferência : "))

    if valor > 0 and contas[origem]['saldo'] >= valor :
        contas[origem]['saldo'] -= valor
        contas[destino]['saldo'] += valor
        print(f"Transferência no valor de R$ {valor:.2f} realizado, novo saldo : R$ {contas[numero]['saldo']:.2f}")
    else :
        print("Saldo insuficiente ou valor inválido")
# conta.py


def cadastrar_conta(contas, clientes, numero_conta, cpfs_titualres, tipo_conta):
    num_str = str(numero_conta)
    tipos_permitidos = ["corrente", "poupança", "salário"]#lista de tipos de conta

    if tipo_conta.lower() not in tipos_permitidos:
        print("Tipo de conta inválido. Use: corrente, salario ou poupanca.")# se for um tipo fora dos 3 não roda
        return False

    if num_str in contas:
        print("Já existe uma conta com esse número")
        return False

    cpfs_validos = []
    for cpf in cpfs_titualres:
        cpf_str = str(cpf)
        if cpf_str not in clientes:
            print(f"O cpf {cpf_str} não está na base de clientes")
            return False
        cpfs_validos.append(cpf_str) # verificar se ja existe o cpf na base de cadastro de clientes
# validando o cpf e conferindo se esta na base, adiciona o cpf pra conta

    contas[num_str] = {
        "titulares" : cpfs_validos,
        "tipo" : tipo_conta.lower(),
        "saldo" : 0.0
    }

    print(f"Conta {tipo_conta} número {num_str} criada com sucesso")
    return True

def cadastrar_contaS(contas, clientes):
    quant_contas=int(input("Quantas contas serão cadastradas?"))

    for _ in range(quant_contas):
        print("\n--- Novo Registo de Conta ---")
        numero_conta = input("Digite o número da conta: ")
        tipo_conta = input("Digite o tipo da conta (corrente, salario ou poupanca): ")

        quantidade_titulares=int(input("Quantos titulares essa conta terá?"))
        cpfs_titulares = []

        for _ in range(quantidade_titulares):
            cpf = input("Digite o CPF do titular :")
            cpfs_titulares.append(cpf)

    cadastrar_conta(contas, clientes, numero_conta, cpfs_titulares, tipo_conta)

def buscar_conta_cpf(contas, cpf) :
    cpf_str = str(cpf)
    encontradas = {}
    for num , dados in contas.item():
        if cpf_str in dados["titulares"]:
            encontradas[num] = dados
        return encontradas
#chave de busca dos titulares da conta

def listar_contas(contas):
  print("\n--- CONTAS ---")
  for numero , dados in contas.item():
      print(f"Conta : {numero} | Tipo : {dados['tipo']} | Titulares : {dados['titulares']} | Saldo : {dados['saldo']:.2f}")


def consultar_saldo(contas):
    numero = input("Digite o número da conta para consultar o saldo: ")
    if numero in contas:
        print(f"Saldo da conta {numero}: R$ {contas[numero]['saldo']:.2f}")
    else:
        print("Conta não encontrada.")

    if conta_encontrada != None :
       print(f"Numero da conta : {conta_encontrada[0]} | Saldo : R$ {conta_encontrada[2]:.2f}")
    else:
        print("Conta não encontrada para este CPF e número.")