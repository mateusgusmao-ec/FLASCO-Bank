def criar_agencia(numero_agencia, nome_agencia):
    clientes_agencia = []

    agencia = (numero_agencia, nome_agencia, clientes_agencia)

    return agencia


def cadastrar_agencia(agencias):
    numero_agencia = int(input("Digite o número da agência: "))
    if numero_agencia in agencias :
        print("Já existe uma agência com esse número") #verificando antes pois ele pedia o nome da agencia mesmo ja exxistindo
        return False
    
    nome_agencia = input("Digite o nome da agência: ")

    agencias[numero_agencia] = {
        "nome" : nome_agencia,
        "clientes" : []
    }
    print(f"Agência {nome_agencia} cadastrada com sucesso")
    return True
    
def procurar_agencia(agencias, numero_agencia):
    return agencias.get(str(numero_agencia), None)


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
    print("\n--- LISTA DE AGÊNCIAS ---")
    for numero , dados in agencias.item():
        print(f"Número : {numero} | Nome : {dados['nome']}")
        print(f"CPFs vinculados : {dados['clientes']}\n")