import json
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca


class Agencia:
    def __init__(self, numero="0001", nome="Agência Central FLASCO-Bank"):
        self.numero = str(numero)
        self.nome = nome
        self.clientes = []
        self.contas = []

    def buscar_cliente(self, cpf):
        cpf_limpo = Cliente.limpar_cpf(cpf)
        for cliente in self.clientes:
            if cliente.cpf == cpf_limpo:
                return cliente
        return None

    def cadastrar_cliente(self, nome, cpf, data_nascimento):
        if not Cliente.validar_cpf(cpf):
            return False, "CPF inválido!"

        if self.buscar_cliente(cpf) is not None:
            return False, "CPF já cadastrado!"

        novo_cliente = Cliente(nome, cpf, data_nascimento)
        self.clientes.append(novo_cliente)
        return True, f"Cliente {novo_cliente.nome} cadastrado com sucesso!"

    def buscar_conta(self, numero):
        num_str = str(numero)
        for conta in self.contas:
            if conta.numero == num_str:
                return conta
        return None

    def buscar_contas_por_cpf(self, cpf):
        cliente = self.buscar_cliente(cpf)
        if cliente:
            return cliente.contas
        return []

    def cadastrar_conta(self, numero, cpf_cliente, tipo, saldo_inicial=0.0):
        if self.buscar_conta(numero) is not None:
            return False, "Já existe uma conta com este número."

        cliente = self.buscar_cliente(cpf_cliente)
        if cliente is None:
            return False, "Cliente não encontrado para o CPF informado."

        tipo_normalizado = tipo.lower().strip()
        saldo_valido = max(0.0, float(saldo_inicial))

        if tipo_normalizado == "corrente":
            nova_conta = ContaCorrente(numero, cliente, saldo_valido)
        elif tipo_normalizado == "poupanca":
            nova_conta = ContaPoupanca(numero, cliente, saldo_valido)
        else:
            return False, "Tipo inválido! Escolha apenas Corrente ou Poupança."

        self.contas.append(nova_conta)
        cliente.adicionar_conta(nova_conta)
        return True, f"Conta {nova_conta.tipo} {nova_conta.numero} criada com sucesso!"

    def salvar_json(self, caminho="dados.json"):
        estrutura = {
            "agencia": {
                "numero": self.numero,
                "nome": self.nome
            },
            "clientes": [c.to_dict() for c in self.clientes],
            "contas": [ct.to_dict() for ct in self.contas]
        }
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(estrutura, arquivo, indent=4, ensure_ascii=False)

    @classmethod
    def carregar_json(cls, caminho="dados.json"):
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            info_agencia = dados.get("agencia", {})
            if not isinstance(info_agencia, dict):
                return cls()

            agencia = cls(
                numero=info_agencia.get("numero", "0001"),
                nome=info_agencia.get("nome", "Agência Central FLASCO-Bank")
            )

            lista_clientes = dados.get("clientes", [])
            if isinstance(lista_clientes, list):
                for c_dict in lista_clientes:
                    cliente = Cliente.from_dict(c_dict)
                    agencia.clientes.append(cliente)

            lista_contas = dados.get("contas", [])
            if isinstance(lista_contas, list):
                for ct_dict in lista_contas:
                    cliente = agencia.buscar_cliente(ct_dict["cpf_cliente"])
                    if cliente:
                        tipo = ct_dict["tipo"]
                        if tipo == "corrente":
                            conta = ContaCorrente(ct_dict["numero"], cliente, ct_dict["saldo"])
                        elif tipo == "poupanca":
                            conta = ContaPoupanca(ct_dict["numero"], cliente, ct_dict["saldo"])
                        else:
                            continue
                        agencia.contas.append(conta)
                        cliente.adicionar_conta(conta)

            return agencia
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return cls()