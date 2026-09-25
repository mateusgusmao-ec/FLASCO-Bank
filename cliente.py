# Funções que diz respeito ao cadastro do cliente
# Login do cliente
# BASEADO NAS FUNÇOES MAIN.PY

def cadastrar_cliente(nome, cpf, data_nascimento):
    return f'Cliente: {nome} | CPF: {cpf} | Data de Nascimento: {data_nascimento}'#retorna os dados numa tupla

def cadastrar_clienteS(nome, cpf, data_nascimento):
    clientes = []

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

def ordenar_clientes(clientes)  # Usar .sort() 
    #ordenação em ordem alfabética com base no nome (lista[0])
    clientes.sort(key= obter_nome_Cliente)
    print("Clientes ordenados!")
    


def listar_clientes(clientes):
    print("\n--- CLIENTES ---")
    for cliente in clientes:
        print(f"Nome : {cliente[0]} | CPF : {cliente[1]} | Nascimento : {cliente[2]}")
