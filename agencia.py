def cadastrar_agencia(agencias):
    numero = int(input("Digite o número da agência: "))
    nome = input("Digite o nome da agência: ")

    clientes = []

    agencia = (numero, nome, clientes)

    agencias.append(agencia)


def listar_agencias(agencias):
    print("\n--- AGÊNCIAS ---")

    for agencia in agencias:
        print("Número:", agencia[0])
        print("Nome:", agencia[1])
        print("Clientes:", len(agencia[2]))

def procurar_agencia(agencias, numero):
    for agencia in agencias:
        if agencia[0] == numero:
            return agencia

    return None


def cliente_existe_na_agencia(agencia, cpf):
    for cliente in agencia[2]:
        if cliente[0] == cpf:
            return True

    return False
