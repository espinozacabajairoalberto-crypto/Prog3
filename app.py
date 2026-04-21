from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lista = ["la guitarra", "para no verte mas" , "balada para un gordo"]
    return render_template('lista.html', titulo='canciones top de la semana', musicas = lista)

if __name__ == '__main__':
    app.run(debug=True)
