from cliente import cadastrar_cliente, validar_cpf
from conta import cadastrar_conta, depositar, sacar, transferir, buscar_contas_por_cpf
def executar_testes():
    print("=== INICIANDO BATERIA DE TESTES (ETAPA 3) ===\n")
    clientes = {}
    contas = {}
    print("1. Teste de Validação de CPF:")
    print("   CPF Inválido (11111111111):", "Passou" if not validar_cpf("11111111111") else "Falhou")
    print("   CPF Inválido (Tamanho Errado):", "Passou" if not validar_cpf("123") else "Falhou")
    cpf_teste = "52998224725" 
    print("\n2. Teste de Cadastro de Cliente (Dicionário):")
    cadastrar_cliente(clientes, "Mateus", cpf_teste, "20070408")
    print("   Cliente armazenado:", clientes)
    print("\n3. Teste de Tipos de Contas Diferentes:")
    cadastrar_conta(contas, clientes, "1001", [cpf_teste], "corrente")
    cadastrar_conta(contas, clientes, "1002", [cpf_teste], "salario")
    cadastrar_conta(contas, clientes, "1003", [cpf_teste], "poupanca")
    # Tentativa de tipo inválido (deve falhar e exibir erro)
    cadastrar_conta(contas, clientes, "1004", [cpf_teste], "investimento")
    print("\n4. Teste de Transações em Dicionário:")
    # Simulando entadas
    contas["1001"]["saldo"] += 1000.0  # Deposito forçado
    contas["1001"]["saldo"] -= 200.0   # Saque forçado
    print(f"   Saldo final da conta 1001 (Esperado 800.0): R$ {contas['1001']['saldo']:.2f}")
    print("\n5. Teste de Busca por CPF:")
    contas_encontradas = buscar_contas_por_cpf(contas, cpf_teste)
    print(f"   Contas vinculadas ao CPF {cpf_teste}: {list(contas_encontradas.keys())}")
    print("\n=== TESTES CONCLUÍDOS ===")
if _name_ == "_main_":
    executar_testes()
