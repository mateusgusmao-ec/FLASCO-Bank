from functools import reduce

def obter_nomes(clientes):
    #compreensão de listas
    return [dados["nome"] for dados in clientes.values()]

def obter_nomes_agencias(agencias):
    return [dados["nome"] for dados in agencias.values()]

def conta_saldo_positivo(contas):
    contas_positivas = filter(lambda x : x[1]["saldo"] > 0, contas.items())
    #devolver em dicionário
    return {numero : dados for numero, dados in contas_positivas}

def calcular_saldo_total(contas):
    return reduce(lambda acc, conta: acc + conta["saldo"], contas.values(), 0.0)

def encontrar_maior_saldo(contas):
    if not contas:
        return 0.0
    conta_maior = max(contas.values(), key=lambda x : x["saldo"])
    return conta_maior["saldo"]

def encontrar_menor_saldo(conta):
    if not contas:
        return 0.0
    conta_menor = min(contas.values(), key=lambda x : x["saldo"])
    return conta_menor["saldo"]

def gerar_dashboard(clientes, contas):
    lista_saldos = [conta["saldo"] for conta in contas.values]

    numero_de_clientes = len(clientes)
    numero_de_contas = len(contas)

    if numero_de_contas == 0 :
        return {
            "numero_de_clientes" : numero_de_clientes,
            "numero_de_contas" : numero_de_contas,
            "saldo_total" : 0.0,
            "maior_saldo" : 0.0,
            "menor_saldo" : 0.0,
            "saldo_medio" : 0.0
        }

    saldo_total = sum(lista_saldos)
    maior_saldo = max(lista_saldos)
    menor_saldo = min(lista_saldos)
    saldo_medio = saldo_total / numero_de_contas

    return {
        "numero_clientes": numero_clientes,
        "numero_contas": numero_contas,
        "saldo_total": saldo_total,
        "maior_saldo": maior_saldo,
        "menor_saldo": menor_saldo,
        "saldo_medio": saldo_medio
    }