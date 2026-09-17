import json

from cliente import criar_clientes, listar_clientes
from conta import criar_conta, depositar, sacar, transferir, saldoConta, listar_contas, consultar_saldo
from agencia import cadastrar_agencia, listar_agencias


def exibir_menu():
    print("\n" + "-" * 30)
    print("        FLASCO-BANK - MENU")
    print("-" * 30)
    print("1. Cadastrar cliente")
    print("2. Cadastrar conta")
    print("3. Cadastrar agência")
    print("4. Listar contas")
    print("5. Listar agências")
    print("6. Listar clientes")
    print("7. Sacar")
    print("8. Transferir")
    print("9. Depositar")
    print("10. Consultar saldo")
    print("11. Relatório do banco")
    print("12. Salvar dados")
    print("0. Sair")


def relatorio_banco(contas, agencias):
    montante_banco = 0

    for conta in contas:
        montante_banco += conta[2]

    print("\n--- RELATÓRIO DO BANCO ---")

    print("Montante total do banco:", montante_banco)

    for agencia in agencias:
        montante_agencia = 0

        for cpf in agencia[2]:
            for conta in contas:
                if conta[1] == cpf:
                    montante_agencia += conta[2]

        print("Agência:", agencia[0])
        print("Montante total da agência:", montante_agencia)


def salvar_dados(clientes, contas, agencias):
    dados = {
        "clientes": clientes,
        "contas": contas,
        "agencias": agencias
    }

    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

    print("Dados salvos com sucesso!")


def executar_menu(clientes, contas, agencias, proximo_numero_conta):

    exibir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Digite o nome: ")
        cpf = int(input("Digite o CPF: "))
        data_nascimento = input("Digite a data de nascimento: ")

        if cliente_existe(clientes, cpf):
            print("Este cliente já existe.")
        else:
            cliente = criar_clientes(nome, cpf, data_nascimento)
            clientes.append(cliente)

    elif opcao == "2":

        cpf = int(input("Digite o CPF do cliente: "))

        if cliente_existe(clientes, cpf):
            conta = criar_conta(proximo_numero_conta, cpf)
            contas.append(conta)
            proximo_numero_conta += 1
        else:
            print("Cliente não cadastrado.")

    elif opcao == "3":

        cadastrar_agencia(agencias)

    elif opcao == "4":

        listar_contas(contas)

    elif opcao == "5":

        listar_agencias(agencias)

    elif opcao == "6":

        listar_clientes(clientes)

    elif opcao == "7":
        sacar(saldoConta, valor_saque)
        
    elif opcao == "8":
        transferir(saldoConta, valor_tranferencia)
        
    elif opcao == "9":
        depositar(saldoConta, valor_deposito)

    elif opcao == "10":
        consultar_saldo(saldoConta)

    elif opcao == "11":

        relatorio_banco(contas, agencias)

    elif opcao == "12":

        salvar_dados(clientes, contas, agencias)

    elif opcao == "0":

        print("Saindo do sistema...")
        return

    else:

        print("Opção inválida. Tente novamente.")

    executar_menu(clientes, contas, agencias, proximo_numero_conta)
