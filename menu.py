from cliente import criar_clienteS
from conta import criar_conta, depositar, sacar, transferir, saldoConta

def exibir_menu():
    print("\n" + "="*30)
    print("      FLASCO-BANK - MENU      ")
    print("="*30)
    print("1. Criar cliente")
    print("2. Sacar")
    print("3. Transferir")
    print("4. Depositar")
    print("5. Consultar Saldo")
    print("0. Sair")

def cliente_existe(clientes, cpf):
    for c in clientes:
        if f"CPF: {cpf}" in c:
            return True
    return False

def buscar_conta_por_cpf(contas, cpf):
    for c in contas:
        if c[1] == str(cpf):
            return c
    return None

def executar_menu(clientes, contas, proximo_numero_conta):
    exibir_menu()
    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        criar_clienteS(nome, cpf, data_nascimento)

    elif opcao == "2":
        sacar(saldoConta, valor_saque)

    elif opcao == "3":
        transferir(saldoConta, valor_transferencia)

    elif opcao == "4":
        depositar(saldoConta, valor_deposito)

    elif opcao == "5":
        print(saldo_Conta)

    elif opcao == "0":
        print("Saindo do sistema...")
        return

    else:
        print("Opção inválida! Tente novamente.")

    executar_menu(clientes, contas, proximo_numero_conta)

def main():
    clientes = []
    contas = []
    proximo_numero_conta = 1
    executar_menu(clientes, contas, proximo_numero_conta)

if __name__ == "__main__":
    main()
