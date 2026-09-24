#extrato,saldo,deposito,saque
#BASEADO NAS FUNÇOES MAIN.PY
#REFATOREI o conta PARA SER UMA TUPLA
ListaContas = []
ListaVinculos = []
def exibir_conta(conta):
    resultado = (f"NÚMERO DA CONTA : '{conta[0]}'\n"
                f"CPF DO CLIENTE  : '{conta[1]}'\n"
                f"SALDO DA CONTA  : 'R$ {conta[2]:.2f}'")
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
    
def cadastrarConta(ListaContas,ListaClientes):
    quantidade = int(input('Quantas contas serão cadastrados? '))
    for item in range(quantidade):
        print(f'cadastro: {item + 1}')
        cpf = str(input('digite seu cpf'))
        clienteExiste = False
        for j in range(len(ListaClientes)):
            if ListaClientes[j][0] == cpf:
                clienteExiste = True
                break
        if not clienteExiste:
            print('cpf n esta cadastrado')
        else:
            saldo = float(input('digite seu saldo inicial'))
            numeroConta = int(input('digite seu numero da conta'))
            Conta = (numeroConta,cpf,saldo)
            ListaContas.append(Conta)
    
def listar_contas(Listacontas):
    if len(Listacontas) == 0:
        print('nenhuma conta encontrada')
        return
    print('LISTA DE CONTAS')
    for item in range(len(Listacontas)):
        Conta = Listacontas[item]
        print(f"Cliente {item + 1}:")
        print(f"  Número da Conta : {Conta[0]}")
        print(f"  CPF do Cliente  : {Conta[1]}")
        print(f"  Saldo da Conta  : R$ {Conta[2]:.2f}")

def consultar_saldo(ListaContas):
    cpf_busca = input("Digite o CPF do cliente para consultar: ")
    encontrado = False
    for item in range(len(ListaContas)):
        registro = ListaContas[item]
        if registro[1] == cpf_busca:  
            print(f"Número da Conta : {registro[0]}")
            print(f"CPF do Cliente  : {registro[1]}")
            print(f"Saldo Atual     : R$ {registro[2]:.2f}")
            encontrado = True
            break
            
    if not encontrado:
        print("\nConta não encontrada para o CPF informado.")

