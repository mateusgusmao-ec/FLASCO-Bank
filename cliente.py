# Funções que diz respeito ao cadastro do cliente

def cadastro_cliente(nome, cpf, data_nascimento):
    cadastro = f'Cliente: {nome} | CPF: {cpf} | Data de Nascimento: {data_nascimento}'
    return cadastro


print(cadastro_cliente('Marcos Silva', '61209914506', '01011990'))