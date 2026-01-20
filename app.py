from flask import Flask, render_template, request, jsonify
from core.matrix import Matrix

app = Flask(__name__)

# App Routes

@app.route('/')
def index():
    """Página inicial/menu."""
    return render_template('index.html')

@app.route('/sum-sub', methods=['GET', 'POST'])
def sum_sub():
    """Soma/Subtração de matrizes."""
    if request.method == 'GET':
        return render_template('sum_sub.html')

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    """Multiplicação de matrizes."""
    if request.method == 'GET':
        return render_template('multiply.html')

@app.route('/transpose', methods=['GET', 'POST'])
def transpose():
    """Transpor uma Matriz"""
    if request.method == 'GET':
        return render_template('transpose.html')

@app.route('/scalar', methods=['GET', 'POST'])
def scalar():
    """Multiplicação de matriz por escalar."""
    if request.method == 'GET':
        return render_template('scalar.html')

@app.route('/determinant', methods=['GET', 'POST'])
def determinant():
    """Cálculo de determinante."""
    if request.method == 'GET':
        return render_template('determinant.html')

@app.route('/inverse', methods=['GET', 'POST'])
def inverse():
    """Cálculo de matriz inversa."""
    if request.method == 'GET':
        return render_template('inverse.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    """Criptografia de mensagens usando multiplicação matricial."""
    if request.method == 'GET':
        return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    """Descriptografia de mensagens usando multiplicação matricial."""
    if request.method == 'GET':
        return render_template('decrypt.html')

# Api Routes


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)