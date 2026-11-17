import atexit
from flask import Flask, render_template, request, redirect, url_for, flash
from agencia import Agencia
from analise import AnaliseFinanceira

app = Flask(__name__)
app.secret_key = "flasco_bank_etapa5_poo"

agencia = Agencia.carregar_json("dados.json")
analise = AnaliseFinanceira(agencia)


def salvar_ao_encerrar():
    agencia.salvar_json("dados.json")


atexit.register(salvar_ao_encerrar)


@app.route("/")
def dashboard():
    dados_dashboard = analise.gerar_dashboard()
    return render_template("index.html", dados=dados_dashboard)


@app.route("/cadastrar_cliente", methods=["POST"])
def cadastrar_cliente_web():
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    nascimento = request.form.get("nascimento")

    sucesso, mensagem = agencia.cadastrar_cliente(nome, cpf, nascimento)
    flash(mensagem, "sucesso" if sucesso else "erro")
    return redirect(url_for("dashboard"))


@app.route("/cadastrar_conta", methods=["POST"])
def cadastrar_conta_web():
    numero = request.form.get("numero")
    cpf = request.form.get("cpf")
    tipo = request.form.get("tipo")
    saldo_str = request.form.get("saldo", "0")

    try:
        saldo_inicial = float(saldo_str)
    except ValueError:
        saldo_inicial = 0.0

    sucesso, mensagem = agencia.cadastrar_conta(numero, cpf, tipo, saldo_inicial)
    flash(mensagem, "sucesso" if sucesso else "erro")
    return redirect(url_for("dashboard"))


@app.route("/transacao", methods=["POST"])
def realizar_transacao_web():
    operacao = request.form.get("operacao")
    numero_origem = request.form.get("numero_origem")
    numero_destino = request.form.get("numero_destino")
    valor_str = request.form.get("valor", "0")

    try:
        valor = float(valor_str)
    except ValueError:
        valor = 0.0

    conta_origem = agencia.buscar_conta(numero_origem)
    if conta_origem is None:
        flash("Conta não encontrada.", "erro")
        return redirect(url_for("dashboard"))

    if operacao == "depositar":
        if conta_origem.depositar(valor):
            flash(f"Depósito de R$ {valor:.2f} realizado na conta {conta_origem.numero}.", "sucesso")
        else:
            flash("Valor de depósito inválido.", "erro")

    elif operacao == "sacar":
        if conta_origem.sacar(valor):
            flash(f"Saque de R$ {valor:.2f} realizado na conta {conta_origem.numero}.", "sucesso")
        else:
            flash("Saldo insuficiente ou valor inválido.", "erro")

    elif operacao == "transferir":
        conta_destino = agencia.buscar_conta(numero_destino)
        if conta_destino is None:
            flash("Conta de destino não encontrada.", "erro")
        elif conta_origem.numero == conta_destino.numero:
            flash("A conta de destino deve ser diferente da origem.", "erro")
        elif conta_origem.transferir(conta_destino, valor):
            flash(f"Transferência de R$ {valor:.2f} realizada com sucesso.", "sucesso")
        else:
            flash("Saldo insuficiente para transferência.", "erro")

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)