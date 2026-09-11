# Funções que diz respeito ao cadastro do cliente
# Login do cliente
# BASEADO NAS FUNÇOES MAIN.PY

def criar_cliente(nome, cpf, data_nascimento):
    cadastro = f'Cliente: {nome} | CPF: {cpf} | Data de Nascimento: {data_nascimento}'
    return cadastro

def criar_clienteS(nome, cpf, data_nascimento):
    clientes = []
    
    quantidade_clientes = int(input('Quantos clientes serão cadastrados? '))

    for _ in range(quantidade_clientes):
        nome = input('Insira seu nome: ')
        cpf = int(input('Insira seu cpf: '))
        data_nascimento = int(input('Insira a sua data de nascimento: '))
        clientes.append(nome)
