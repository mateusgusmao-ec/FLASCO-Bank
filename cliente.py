# Funções que diz respeito ao cadastro do cliente
# Login do cliente
# BASEADO NAS FUNÇOES MAIN.PY

def cadastrar_cliente(nome, cpf, data_nascimento):
    cadastro = f'Cliente: {nome} | CPF: {cpf} | Data de Nascimento: {data_nascimento}'
    return cadastro

def cadastrar_clienteS(nome, cpf, data_nascimento):
    clientes = []

    quantidade = int(input('Quantos clientes serão cadastrados? '))
    
    if cpf not in clientes: 
        for _ in range(quantidade):
            nome = input()
            cpf = int(input())
            data_nascimento = int(input())
            clientes.append(nome)
            clientes.append(cpf)
            clientes.append(data_nascimento)
    else:
        print('Este cliente já existe.')


def listar_clientes(clientes):
    print("\n--- CLIENTES ---")

    for cpf in clientes:
        print("CPF:", cpf)
