from functools import reduce

# 1. Listar clientes e agências
def obter_nomes_clientes(clientes):
    # Compreensão de lista para extrair apenas os nomes
    return [dados["nome"] for dados in clientes.values()]

def encontrar_maior_saldo(contas):
    # Encontra o maior saldo usando a função de alta ordem max() com lambda
    if not contas:
        return 0.0
    # max() é uma função de alta ordem que aceita uma função (key) como argumento
    conta_maior = max(contas, key=lambda conta: conta["saldo"])
    return conta_maior["saldo"]

def encontrar_menor_saldo(contas):
    # Encontra o menor saldo usando a função de alta ordem min() com lambda
    if not contas:
        return 0.0
    # min() é uma função de alta ordem que aceita uma função (key) como argumento
    conta_menor = min(contas, key=lambda conta: conta["saldo"])
    return conta_menor["saldo"]

def gerar_dados_dashboard(clientes, contas):
    # Gera o resumo para o dashboard combinando list comprehensions e funções de alta ordem (reduce, map)
    if not contas:
        return {
            "num_clientes": len(clientes),
            "num_contas": 0,
            "saldo_total": 0.0,
            "maior_saldo": 0.0,
            "menor_saldo": 0.0,
            "saldo_medio": 0.0
        }

    # 1. Compreenssão de listas para extrair apenas os saldos de todas as contas
    saldos = [conta["saldo"] for conta in contas]

    # 2. Função de Alta Ordem (reduce) para somar os saldos
    saldo_total = reduce(lambda acc, saldo: acc + saldo, saldos, 0.0)

    # 3. Métricas finais
    qtd_contas = len(saldos)
    saldo_medio = saldo_total / qtd_contas if qtd_contas > 0 else 0.0

    return {
        "num_clientes": len(clientes),
        "num_contas": qtd_contas,
        "saldo_total": saldo_total,
        "maior_saldo": encontrar_maior_saldo(contas),
        "menor_saldo": encontrar_menor_saldo(contas),
        "saldo_medio": saldo_medio,
        "saldo_total_formatado": f"R$ {saldo_total:.2f}",
        "saldo_medio_formatado": f"R$ {saldo_medio:.2f}",
    }

def obter_nomes_agencias(agencias):
    return [dados["nome"] for dados in agencias.values()]

# 2. Listar contas com saldo positivo
def contas_saldo_positivo(contas):
    # Usando filter e lambda (Função de Alta Ordem)
    # Retorna uma lista de tuplas (numero_conta, dados_da_conta)
    contas_positivas = filter(lambda item: item[1]["saldo"] > 0, contas.items())
    
    # Convertendo de volta para dicionário usando compreensão de dicionário
    return {numero: dados for numero, dados in contas_positivas}

# 3. Calcular saldo total do banco
def calcular_saldo_total(contas):
    # Usando reduce e lambda para somar (Função de Alta Ordem)
    # O 0.0 no final é o valor inicial do acumulador
    return reduce(lambda acumulador, conta: acumulador + conta["saldo"], contas.values(), 0.0)

# 4. Encontrar maior saldo
def encontrar_maior_saldo(contas):
    if not contas:
        return 0.0
    # Usando max com uma função lambda para buscar a conta com maior saldo
    conta_maior = max(contas.values(), key=lambda c: c["saldo"])
    return conta_maior["saldo"]

# 5. Encontrar menor saldo
def encontrar_menor_saldo(contas):
    if not contas:
        return 0.0
    # Usando min com uma função lambda
    conta_menor = min(contas.values(), key=lambda c: c["saldo"])
    return conta_menor["saldo"]

# 6. Dashboard para análise financeira
def gerar_dados_dashboard(clientes, contas):
    # Usando compreensão de lista para extrair todos os saldos rapidamente
    lista_saldos = [conta["saldo"] for conta in contas.values()]
    
    numero_clientes = len(clientes)
    numero_contas = len(contas)
    
    # Se não houver contas, evita divisão por zero
    if numero_contas == 0:
        return {
            "numero_clientes": numero_clientes,
            "numero_contas": 0,
            "saldo_total": 0.0,
            "maior_saldo": 0.0,
            "menor_saldo": 0.0,
            "saldo_medio": 0.0
        }

    saldo_total = sum(lista_saldos)
    maior_saldo = max(lista_saldos)
    menor_saldo = min(lista_saldos)
    saldo_medio = saldo_total / numero_contas

    return {
        "numero_clientes": numero_clientes,
        "numero_contas": numero_contas,
        "saldo_total": saldo_total,
        "maior_saldo": maior_saldo,
        "menor_saldo": menor_saldo,
        "saldo_medio": saldo_medio
    }