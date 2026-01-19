from flask import Flask, render_template, request, jsonify
from core.matrix import Matrix

app = Flask(__name__)

@app.route('/')
def index():
    """Página inicial/menu."""
    pass

@app.route('/sum', methods=['GET', 'POST'])
def sum_sub():
    """Soma/Subtração de matrizes."""
    pass

@app.route('/scalar', methods=['GET', 'POST'])
def scalar():
    """Multiplicação de matriz por escalar."""
    pass

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    """Multiplicação de matrizes."""
    pass

@app.route('/determinant', methods=['GET', 'POST'])
def determinant():
    """Cálculo de determinante."""
    pass

@app.route('/inverse', methods=['GET', 'POST'])
def inverse():
    """Cálculo de matriz inversa."""
    pass

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    """Criptografia de mensagens usando multiplicação matricial."""
    pass

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    """Descriptografia de mensagens usando multiplicação matricial."""
    pass

@app.route('/check_matrix', methods=['POST'])
def check_matrix():
    """Endpoint para verificar se uma matriz é válida para criptografia."""
    pass

if __name__ == '__main__':
    app.run(debug=True)