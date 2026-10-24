import json
from flask import Flask, flash, redirect, render_template, request, url_for

from analise import gerar_dados_dashboard
from cliente import cadastrar_cliente, validar_cpf

app = Flask(__name__)
# A secret_key é necessária para exibir mensagens de aviso (flash) na tela
app.secret_key = "flasco_bank_chave_secreta"


def carregar_dados():
  try:
    with open("dados.json", "r", encoding="utf-8") as arquivo:
      dados = json.load(arquivo)
      return (
          dados.get("clientes", {}),
          dados.get("contas", {}),
          dados.get("agencias", {}),
      )
  except FileNotFoundError:
    return {}, {}, {}


def salvar_dados(clientes, contas, agencias):
  dados = {"clientes": clientes, "contas": contas, "agencias": agencias}
  with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)


@app.route("/")
def dashboard():
  clientes, contas, _ = carregar_dados()
  estatisticas = gerar_dados_dashboard(clientes, contas)
  return render_template("index.html", dados=estatisticas)


# ROTA QUE RECEBE OS DADOS DO FORMULÁRIO HTML
@app.route("/cadastrar_cliente", methods=["POST"])
def cadastrar_cliente_web():
  # 1. Pega os dados digitados nos campos 'name' do HTML
  nome = request.form.get("nome")
  cpf = request.form.get("cpf")
  nascimento = request.form.get("nascimento")

  # 2. Carrega a base atual do JSON
  clientes, contas, agencias = carregar_dados()

  # 3. Validações antes de salvar
  if not validar_cpf(cpf):
    flash("❌ CPF inválido!", "erro")
  elif str(cpf) in clientes:
    flash("❌ CPF já cadastrado!", "erro")
  else:
    # Cadastra no dicionário e salva no JSON
    cadastrar_cliente(clientes, nome, cpf, nascimento)
    salvar_dados(clientes, contas, agencias)
    flash(f"✅ Cliente {nome} cadastrado com sucesso!", "sucesso")

  # 4. Recarrega a página do dashboard
  return redirect(url_for("dashboard"))


if __name__ == "__main__":
  app.run(debug=True)