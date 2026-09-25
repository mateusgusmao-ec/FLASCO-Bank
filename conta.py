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

def cadastrar_contaS(numeroConta):
    contas = []

    quantidade = int(input('Quantas contas serão cadastrados? '))

    for _ in range(quantidade):
        print()
        numero_conta = int(input("Digite o numero da conta : "))
        cpf = int(input("Digite seu cpf"))

        #verificar se o cliente existe
        cliente_encontrado=False
        for cliente in clientes :
            if cliente[1] == cpf :
                cliente_encontrado = True
                break
        if not cliente_encontrado:
            print("Este  CPF não está cadastrado. Cadastre primeiro para criar a conta")

        else : #ver se o numero da conta ja exite
            conta_duplicada = False
            for conta in contas :
                if cont[0] == numero_conta:
                    conta_duplicada = True
                    break
            if conta_duplicada:
                print("Erro, já existe uma conta com esse número")
            else :
                saldo_inicial = 0.0
                #criar o dado da conta
                nova_conta = (numero_conta, cpf, saldo_inicial)
                contas.append(nova_conta)
                print(f"Conta {numero_conta} cadastrada com sucesso no cpf {cpf}")

def listar_contas(contas):
    print("\n--- CONTAS ---")

    for conta in contas:
        print("Número da conta:", contas[0])
        print("CPF do cliente:", contas[1])
        print("Saldo:", [contas2])
        print()

def consultar_saldo(cpf, numeroConta):
    cpf = int(input("Digite o CPF: "))
    conta = buscar_conta_por_cpf(contas, cpf)

    if conta != None:
        print(saldoConta(conta[0], conta[2]))
    else:
        print("Conta não encontrada.")
