# Funções que diz respeito ao cadastro do cliente

def cadastro_cliente(nome, cpf, senha):
    nome = input('Insira seu nome: ')
    cpf = int(input('Insira seu cpf: '))
    senha = input('Insira sua senha (somente letras):')

    return nome, cpf, senha

def Cliente(cadastro_cliente):
    cadastro_cliente(None, None, None)
