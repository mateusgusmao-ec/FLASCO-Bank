from cliente import criar_cliente, buscar_cliente
from conta import criar_conta, buscar_conta_por_cpf, depositar, sacar, transferir

def main():
    clientes = []
    contas = []
    proximo_numero_conta = 1

    while True:
        print("\n" + "="*30)
        print("      FLASCO-BANK - MENU      ")
        print("="*30)
        print("1. Criar cliente")
        print("2. Sacar")
        print("3. Transferir")
        print("4. Depositar")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cpf = input("Digite seu CPF: ").strip()
            if buscar_cliente(clientes, cpf):
                print("Cliente já cadastrado com este CPF!")
            else:
                nome = input("Digite seu nome: ").strip()
                nasc = input("Digite sua data de nascimento: ").strip()
                
            
                novo_cliente = criar_cliente(nome, cpf, nasc)
                clientes.append(novo_cliente)
                
                num_conta = f"{proximo_numero_conta:05d}-0"
                nova_conta = criar_conta(num_conta, cpf, saldo_inicial=0.0)
                contas.append(nova_conta)
                proximo_numero_conta += 1
                
                print(f"\nCliente cadastrado com sucesso!")
                print(f"Conta gerada automaticamente: {num_conta}")

        elif opcao == "2":
            cpf = input("Digite o CPF do titular da conta: ").strip()
            conta = buscar_conta_por_cpf(contas, cpf)
            
            if conta:
                val = float(input("Digite o valor para saque: "))
                if sacar(conta, val):
                    print(f"Saque realizado! Saldo atual: R$ {conta[2]:.2f}")
                else:
                    print("Falha no saque. Saldo insuficiente ou valor inválido.")
            else:
                print("Conta/Cliente não encontrado.")

        elif opcao == "3":
            cpf_origem = input("Digite o CPF do remetente: ").strip()
            c_origem = buscar_conta_por_cpf(contas, cpf_origem)
            
            if not c_origem:
                print("Conta de origem não encontrada.")
                continue

            cpf_destino = input("Digite o CPF do destinatário: ").strip()
            c_destino = buscar_conta_por_cpf(contas, cpf_destino)
            
            if not c_destino:
                print("Conta de destino não encontrada.")
                continue

            val = float(input("Digite o valor da transferência: "))
            if transferir(c_origem, c_destino, val):
                print(f"Transferência realizada! Saldo atual: R$ {c_origem[2]:.2f}")
            else:
                print("Falha na transferência. Saldo insuficiente ou valor inválido.")

        elif opcao == "4":
            cpf = input("Digite o CPF do titular da conta: ").strip()
            conta = buscar_conta_por_cpf(contas, cpf)
            
            if conta:
                val = float(input("Digite o valor do depósito: "))
                if depositar(conta, val):
                    print(f"Depósito realizado! Saldo atual: R$ {conta[2]:.2f}")
                else:
                    print("Falha no depósito. Valor inválido.")
            else:
                print("Conta/Cliente não encontrado.")

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()