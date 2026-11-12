# Funções que diz respeito ao cadastro do cliente
# Login do cliente
# BASEADO NAS FUNÇOES MAIN.PY

class Cliente:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = str(self.data_nascimento)
        self.contas = []

    def adcicionar_conta(self, conta):
        if conta not in self.contas :
            self.contas.append(conta)

    def to_dict(self):
        return{
            "nome" : self.nome,
            "cpf" : self.nome,
            "data_nascimento" : self.data_nascimento
            }
    @classmethod
    def from_dicts(cls, dados):
        return cls(
            nome = dados["nome"],
            cpf = dados["cpf"],
            data_nascimento = dados["data_nacimento"]
        )
    @staticmethod
    def limpar_cpf(cpf):
        cpf_texto = str(cpf).strip()
        cpf_numeros = "" 
        for letra in cpf_texto:
            if letra.isdigit():
                cpf_numeros += letra
            if len(cpf_numeros) == 10:
                cpf_numeros = "0" + cpf_numeros
            return cpf_numeros
