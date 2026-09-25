#extrato,saldo,deposito,saque
#BASEADO NAS FUNÇOES MAIN.PY
def exibir_conta(numeroConta,saldoConta):
    resultado = f"NÚMERO DA CONTA : '{numeroConta}'\nSALDO DA CONTA : '{saldoConta}'"  # printa os dados da conta
    return resultado

def depositar(saldoConta,valor_deposito):
    if valor_deposito > 0:
        novoSaldo = saldoConta + valor_deposito   # sistema de entrada de um valor na conta
        return True, novoSaldo
    else:
        return False,saldoConta
    
def sacar(saldoConta, valor_saque):
    if valor_saque > 0 and saldoConta >= valor_saque:
        novoSaldo = saldoConta - valor_saque  # sistema de saída de um valor da conta
        return True, novoSaldo
    else:
        return False, saldoConta

def transferir(saldoConta, valor_deposito):
    if valor_deposito > 0 and saldoConta >= valor_deposito:
        novoSaldo = saldoConta - valor_deposito
        return True, novoSaldo
    else:
        return False, saldoConta
# conta.py


def cadastrar_contaS(contas, clientes):
  quantidade_contas = int(input("Quantas contas serão cadastradas? "))

  for _ in range(quantidade_contas):
    print()
    numero_conta = int(input("Digite o número da conta: "))

    #verifica se ja tem a conta
    conta_duplicada = False
    for conta in contas:
      if conta[0] == numero_conta:
        conta_duplicada = True
        break

    if conta_duplicada:
      print("Já existe uma conta cadastrada com este número.")
    else:
      # perguntar o numero de titulares
      qtd_titulares = int(
          input("Quantos titulares esta conta terá? (Ex: 1 ou mais): ")
      )
      cpfs_titulares = []
      conta_valida = True

      # coletar os cpf's
      for _ in range(qtd_titulares):
        cpf = int(input("Digite o CPF do titular: "))

        # ver se o cliente existe na lista_clientes
        cliente_encontrado = False
        for cliente in clientes:
          # cliente[1] é o cpf
          if cliente[1] == cpf:
            cliente_encontrado = True
            break

        if not cliente_encontrado:
          print(f" O CPF {cpf} não está cadastrado! Cadastre o cliente primeiro.")
          conta_valida = False
          break
        else:
          # para não repetir o cpf
          if cpf not in cpfs_titulares:
            cpfs_titulares.append(cpf)
          else:
            print(f"O CPF {cpf} já foi adicionado a esta conta.")

      # se for válido cria a conta com mais de 1 titular
      if conta_valida and len(cpfs_titulares) > 0:
        saldo_inicial = 0.0
        # guarda uma lista de cpfs na cliente[1]
        nova_conta = (numero_conta, cpfs_titulares, saldo_inicial)
        contas.append(nova_conta)
        print(f"Conta conjunta {numero_conta} cadastrada com sucesso para os CPFs: {cpfs_titulares}!")


def listar_contas(contas):
  print("\n--- CONTAS ---")
  for conta in contas:
    print(f"Número da conta: {conta[0]}")
    print(f"Titulares (CPFs): {conta[1]}")  # mostra todos os cpf's da lista
    print(f"Saldo: {conta[2]}")
    print()


def consultar_saldo(cpf, numeroConta):
    cpf = int(input("Digite o CPF: "))
    conta = buscar_conta_por_cpf(contas, cpf)

    if conta != None:
        print(saldoConta(conta[0], conta[2]))
    else:
        print("Conta não encontrada.")
