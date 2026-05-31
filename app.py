from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/administrador')
def administrador():
    return render_template('administrador.html')


@app.route('/candidato')
def candidato():
    return render_template('candidato.html')

if __name__ == '__main__':
    app.run(debug=True)