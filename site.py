import random

from flask import Flask

app = Flask(__name__)
facts_list = ["Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, para que passemos o máximo de tempo possível visualizando conteúdo.",            
              "De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependencies de seus smartphones.", 
              "As redes sociais têm seus pontos positivos e negativos, e devemos estar conscientes de ambos ao utilizá-las.", 
              "O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna.",
              "Segundo um estudo de 2019, mais de 60% das pessoas respondem a mensagens de trabalho em seus smartphones dentro de 15 minutos após sair do trabalho"]
caraoucoroa = ["Cara",
               "Coroa"]

@app.route("/") 
def home(): 
    return """<h1>Página inicial</h1>
    <a href="/fatos">Veja um fato aleatório!</a>
    <ul>
    </ul>
    <a href="/dado">Role um dado de 6 lados!</a>
    <ul>
    </ul>
    <a href="/cara ou coroa">Cara ou Coroa</a>
    """

@app.route("/fatos")
def fatos():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/dado")
def dado():
    return f"<p>{random.randint(1, 6)}</p>"

@app.route("/cara ou coroa")
def cara():
    return f"<p>{random.choice(caraoucoroa)}</p>"

app.run(debug=True)
