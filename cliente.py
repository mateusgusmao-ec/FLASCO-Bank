# Funções que diz respeito ao cadastro do cliente
# Login do cliente
# BASEADO NAS FUNÇOES MAIN.PY

def validar_cpf(cpf):
    cpf_texto = str(cpf)
    cpf_numeros = ""
    
    for letra in cpf_texto :
        if letra.isdigit() :
            cpf_numeros += letra
    
    if len(cpf_numeros) != 11 :
        return False
    
    todos_iguais = True
    for i in range(1, 11):
        if cpf_numeros[i] != cpf_numeros[0]:
            todos_iguais = False
            break
    if todos_iguais:
        return False
    
    soma = 0
    multiplicador = 10
    
    for i in range(9) :
        soma += int(cpf_numeros[i]) * multiplicador
        
    resto = (soma*10) % 11
    if resto >= 10:
        digito1=0
    else : 
        digito1 = resto
    
    if digito1 != int(cpf_numeros[9]):
        return False

def cadastrar_cliente(clientes, nome, cpf, data_nascimento):
    cpf_str = str(cpf)

    if not validar_cpf(cpf_str):
        print("CPF inválido!")
        return False

    if cpf_str in clientes :
        print(f"O cpf {cpf_str} já está cadastrado")
        return False    

    clientes[cpf_str] = { #dicionario com cpf como chave
        "nome": nome,
        "nascimento": data_nascimento
    }
    print("Cliente cadastrado com sucesso!")
    return True
    

def cadastrar_clienteS(clientes):
    quantidade = int(input('Quantos clientes serão cadastrados? '))
    for i in range(quantidade):
        nome = input()
        cpf = int(input())
        data_nascimento = int(input())

        cpf_existe = False
        for cliente in clientes :
            if cliente[1] == cpf:
                cpf_existe = True
                break #usando break para interromper o cadastro se o cpf ja existir
        if not cpf_existe :
            #criar tupla e adicionar o novo cliente
            novo_cliente = cadastrar_cliente(nome, cpf, data_nascimento)
            clientes.append(novo_cliente)
            print("Cliente cadastrado com sucesso!")
        else:
            print(f"O CPF {cpf} já existe. Cliente não encontrado")
def obter_nome_Cliente(cliente):
    return cliente[0]#retorna o nome puro

def ordenar_clientes(clientes):  # Usar .sort()
    #ordenação em ordem alfabética com base no nome (lista[0])
    clientes.sort(key= obter_nome_Cliente)
    print("Clientes ordenados!")
    
def procurar_cliente(clientes, cpf) :
    cpf_str = str(cpf)
    return clientes.get(cpf_str, None)
    


def listar_clientes(clientes):
    print("\n--- CLIENTES ---")
    for cpf, dados in clientes.items():
        print(f"Nome : {dados['nome']} | CPF : {cpf} | Nascimento : {dados['nascimento']}")