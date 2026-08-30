from cliente import criar_cliente
from conta import depositar, sacar, exibir_conta
#chama as funções dos outros arquivos para main



print("-"*27)
print("-"*3, "CADASTRO DO CLIENTE", "-"*3)
nome_usuario=input("DIGITE SEU NOME : ")
cpf_usuario=input("DIGITE SEU CPF :" )
nascimento_usuario=input("DIGITE SEU NASCIMENTO : ")

dados_clientes = criar_cliente(nome_usuario, cpf_usuario, nascimento_usuario)

numeroDaConta='12355-0'
saldoConta=0.00

print("\n--- RESUMO DO CADASTRO BANCARIO ---")
print(dados_clientes)
print(exibir_conta(numeroDaConta, saldoConta))

print("\n--- SIMULANDO DEPÓSITO ---")
valor_deposito=float(input("Digite o valor do depósito : "))

sucesso_deposito, saldoConta = depositar(saldoConta, valor_deposito)

if sucesso_deposito: 
    print("✅ Depósito realizado com sucesso!")
else:
    print("❌ Falha no depósito. Valor inválido.")


print(exibir_conta(numeroDaConta, saldoConta))

print("\n--- SIMULANDO SAQUE ---")
valor_saque=float(input("Digite um valor para saque : "))

sucesso_saque, saldoConta = sacar(saldoConta, valor_saque)

if sucesso_saque:
    print("✅ Saque realizado com sucesso!")
else :
    print("❌ Falha no saque. Valor inválido.")

print("\n--- RESULTADO FINAL DO SISTEMA ---")
print(dados_clientes)
print(exibir_conta(numeroDaConta, saldoConta))