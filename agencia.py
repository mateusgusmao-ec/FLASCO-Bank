def criar_agencia(numero_agencia, nome_agencia):
    clientes_agencia = []

    agencia = (numero_agencia, nome_agencia, clientes_agencia)

    return agencia


def cadastrar_agencia(agencias):
    numero_agencia = int(input("Digite o número da agência: "))
    nome_agencia = input("Digite o nome da agência: ")

    agencia = criar_agencia(numero_agencia, nome_agencia)

    agencias.append(agencia)


def procurar_agencia(agencias, numero_agencia):
    for agencia in agencias:
        if agencia[0] == numero_agencia:
            return agencia

    return None


def cliente_existe_na_agencia(agencia, cpf):
    for cpf_cliente in agencia[2]:
        if cpf_cliente == cpf:
            return True

    return False


def adicionar_cliente_agencia(agencias, clientes, numero_agencia, cpf):
    agencia = procurar_agencia(agencias, numero_agencia)

    if agencia == None:
        return False

    if cpf not in clientes:
        return False

    if cliente_existe_na_agencia(agencia, cpf):
        return False

    agencia[2].append(cpf)

    return True


def listar_agencias(agencias):
    for agencia in agencias:
        print("Número da agência:", agencia[0])
        print("Nome da agência:", agencia[1])

        print("Clientes da agência:")

        for cpf in agencia[2]:
            print(cpf)

        print()
