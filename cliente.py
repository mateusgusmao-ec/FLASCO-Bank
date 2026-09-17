# Funções que diz respeito ao cadastro do cliente
# Login do cliente
# BASEADO NAS FUNÇOES MAIN.PY

def criar_cliente(nome, cpf, data_nascimento):
    cadastro = f'Cliente: {nome} | CPF: {cpf} | Data de Nascimento: {data_nascimento}'
    return cadastro

def criar_clienteS(nome, cpf, data_nascimento):
    cliente = []

    quantidade = int('Quantos clientes serão cadastrados? ')

    if cpf not in clientes: 
        for _ in range(quantidade):
            nome = input()
            cpf = int(input())
            data_nascimento = int(input())
            cliente.append(cpf)
    else:
        print('Este cliente já existe.')
