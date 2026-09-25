import json

from cliente import cadastrar_clienteS, listar_clientes, ordenar_clientes
from conta import cadastrar_contaS, depositar, sacar, transferir, saldoConta, listar_contas, consultar_saldo
from agencia import cadastrar_agencia, listar_agencias

#função para carregar os dados
def carregar_dados():
    try:
        with open("dados.json", "r") as arquivo :
            dados = json.load(arquivo)
            #usando listas os dados terão índice
        return dados[0], dados[1], dados[2]
    except FileNotFoundError:
        return [], [], [] #se o arquivo não existir

#função para salvar os dados(com listas)
def salvar_dados(clientes, contas, agencias):
    dados = [clientes, contas, agencias] #lista dos 3 dados
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

    print("Dados salvos com sucesso!")






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
    print("13 . Procurar clientes")
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
                if cpf in conta[1]: #mudou de == conta[1] porque agora tem uma lista de cpf's
                    montante_agencia += conta[2]

        
        print("Agência:", agencia[0])
        print("Montante total da agência:", montante_agencia)





def executar_menu(clientes, contas, agencias, proximo_numero_conta):

    exibir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_contaS(contas, clientes)

    elif opcao == "2":
        cadastrar_clienteS(clientes)

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

    elif opcao == "13":
        cpf_busca = int(input("Digite o CPF para busca : "))
        cliente_encontrado = procurar_cliente(clientes, cpf_busca)
        if cliente_encontrado:
            print(f"Cliente encontrado | Nome : {cliente_encontrado[0]} | CPF : {cliente_encontrado[1]}")#cliente_ecnontrado pois não faz parte das outras listas
        else :
            print("Cliente não encontrado")
    elif opcao == "0":
        print("Saindo do sistema...")
        return

    else:

        print("Opção inválida. Tente novamente.")

    executar_menu(clientes, contas, agencias, proximo_numero_conta)
