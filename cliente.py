# Funções que diz respeito ao cadastro do cliente
# Login do cliente
# BASEADO NAS FUNÇOES MAIN.PY

def cadastrar_cliente(nome, cpf, data_nascimento):
    return (nome, cpf, data_nascimento)

def cadastrar_clienteS(clientes):
    quantidade = int(input('Quantos clientes serão cadastrados? '))
    for i in range(quantidade):
        nome = input()
        cpf = int(input())
        data_nascimento = int(input())

        cpf_existe = False
        for cliente in clientes :
            if cliente[1] == cpf:
                cpf_existe = True
                break #usando break para interromper o cadastro se o cpf ja existir
        if not cpf_existe :
            #criar tupla e adicionar o novo cliente
            novo_cliente = cadastrar_cliente(nome, cpf, data_nascimento)
            clientes.append(novo_cliente)
            print("Cliente cadastrado com sucesso!")
        else:
            print(f"O CPF {cpf} já existe. Cliente não encontrado")
def obter_nome_Cliente(cliente):
    return cliente[0]#retorna o nome puro

def ordenar_clientes(clientes):  # Usar .sort()
    #ordenação em ordem alfabética com base no nome (lista[0])
    clientes.sort(key= obter_nome_Cliente)
    print("Clientes ordenados!")
    
def procurar_cliente(clientes, cpf_procurado) :
    for cliente in clientes :
        #cliente[1] é o cpf
        if cliente[1] == cpf_procurado :
            return cliente
    return None


def listar_clientes(clientes):
    print("\n--- CLIENTES ---")
    for cliente in clientes:
        print(f"Nome : {cliente[0]} | CPF : {cliente[1]} | Nascimento : {cliente[2]}")
