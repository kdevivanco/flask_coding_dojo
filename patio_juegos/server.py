from flask import Flask,render_template
app = Flask (__name__)

@app.route('/')
def home():
    return('<h3>Hola mundo</h3>')

@app.route('/play')
pass


if __name__ == '__main__':
    app.run(debug=True)