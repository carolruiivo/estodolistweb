from flask import Flask, render_template, request, session, redirect
from database import consultar_tarefas

app = Flask(__name__)
app.secret_key = "senai"

# dados de acesso do adm
ADMIN_EMAIL = "carolruivo@gmail.com"
ADMIN_SENHA = "123456"

@app.route("/") #HomePage - página inicial
def home():
    if "login" not  in session:
        return redirect("/login")
    
    #usuário logado
    tarefas = consultar_tarefas()
    return render_template("index.html",tarefas=tarefas)

# -----------------------------------------
# rota login
@app.route("/login", methods=["GET","POST"])
def login():
    if "login" in session:
        return redirect("/")
    
    if request.method == "GET":
        return render_template("login.html")

    # post
    email = request.form.get("email") # pegando o email que estava no form html
    senha = request.form.get("senha") # essa informação está no atributo name

    if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
        session["login"] = True # cria a sessão lista 
        return redirect("/") # redireciona para a página/rota inicial
    else:
        return render_template("login.html", msgerro = "E-mail ou senha estão incorretos")

# ------------------------------
# rota logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ----------------------------------
# tratamento de erro - código 404 
@app.errorhandler(404)
def not_found(erro):
    return render_template("erro404.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000) #debug ajuda a encontrar erros, caso esteja desligado, ele mascara os erros mas não significa que o sistema funcione perfeitamente; port é a "porta" usada no computador
    #host='0.0.0.0' Habilita o IP público

