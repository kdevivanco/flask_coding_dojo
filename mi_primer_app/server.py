from flask import Flask
app = Flask (__name__)

@app.route('/')
def home():
    return('<h3>Hola mundo</h3>')

@app.route('/dojo')
def ejemplo_1_dojo():
    return '<h3>Dojo!</h3>'

@app.route('/say/<nombre>')
def ejemplo_2(nombre):
    return f'<h3>{str(nombre)}</h3>'


@app.route('/repeat/<some_int>/<word>')
def ejemplo_3(some_int,word):
    texto = [f'<h3>{str(word)}</h3>']*int(some_int)
    texto = ' '.join(texto)
    return texto


@app.errorhandler(404)
def error(e):
    return('<h3>Esta ruta no existe</h3>')


if __name__ == '__main__':
    app.run(debug=True)