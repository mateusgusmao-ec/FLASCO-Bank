def cadastrar_agencia(agencias):
    numero = int(input("Digite o número da agência: "))
    nome = input("Digite o nome da agência: "))

    clientes_agencia = []

    agencia = (numero, nome, clientes_agencia)

    agencias.append(agencia)


def procurar_agencia(agencias, numero):
    for agencia in agencias:
        if agencia[0] == numero:
            return agencia

    return None


def cliente_existe_na_agencia(agencia, cpf):
    for cliente in agencia[2]:
        if cliente == cpf:
            return True

    return False
