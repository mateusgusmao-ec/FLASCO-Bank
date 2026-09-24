# Funções que diz respeito ao cadastro do cliente
# Login do cliente
# BASEADO NAS FUNÇOES MAIN.PY
ListaClientes = []
def exibirCliente(nome, cpf, data_nascimento):
    cadastro = f'Cliente: {nome} | CPF: {cpf} | Data de Nascimento: {data_nascimento}'
    return cadastro

def cadastrarClientes(ListaClientes):
    quantidade = int(input('Quantos clientes serão cadastrados? '))
    for item in range(quantidade):
        cpf = str(input('digite seu cpf para cadastro'))
        cpfExiste = False
        for j in range(len(ListaClientes)):
            if ListaClientes[j][0] == cpf:
                cpfExiste = True
                break
        if cpfExiste:
             print('cliente ja cadastrado')
        else:
            nome = str(input('digite seu nome'))
            data_nascimento = str(input('digite sua data de nascimento'))
            cliente = (cpf,nome,data_nascimento)
            ListaClientes.append(cliente)
            print('cliente cadasteado')

def listar_clientes(ListaClientes):
    if len(ListaClientes) == 0:
        print('Nenhum cliente encontrado.')
        return
    print('LISTA DE CLIENTES')
    for item in range(len(ListaClientes)):
        cliente = ListaClientes[item]
        print(f"Cliente {item + 1}:")
        print(f"  CPF                : {cliente[0]}")
        print(f"  Nome               : {cliente[1]}")
        print(f"  Data de Nascimento : {cliente[2]}")
