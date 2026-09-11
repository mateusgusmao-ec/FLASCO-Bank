from cliente import criar_clienteS
from conta import criar_contaS

print('BEM VINDO AO FLASCO-BANK')
print('1 - Cadastro cliente')
print('2 - Criar conta')
print('5 - Sair da conta')

operacao = int(input('Insira o código de operação: '))

while operacao != 5:
        if operacao == 1:
            criar_clienteS(nome, cpf, data_nascimento)

        elif operacao == 2:
            criar_contaS(saldoConta, )
        
        
        elif operacao > 5:
            print('Não existe esse codigo de operação, insira novamente')
        
        operacao = int(input('Insira o código de operação: '))
                  


