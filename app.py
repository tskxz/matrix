from flask import Flask, render_template, request, jsonify
from core.matrix import Matrix

app = Flask(__name__)

@app.route('/')
def index():
    """
    Página inicial/menu.
    Irá renderizar o template 'index.html'.
    """
    return render_template('index.html')

@app.route('/sum', methods=['GET', 'POST'])
def sum_sub():
    """
    Soma/Subtração de matrizes.
    No POST, processa o cálculo. No GET, mostra o formulário.
    """
    if request.method == 'POST':
       """
       Referencia para o futuro de como usar a classe Matrix para soma:
       # matriz_a = Matrix(2, 2, [[1, 2], [3, 4]])
       # matriz_b = Matrix(2, 2, [[5, 6], [7, 8]])
       # matriz_a.add(matriz_b)
       """
       matriz_a = Matrix(2, 2) # matriz 2 por 2 nula para testar
       return matriz_a.add()
    return render_template('sum_sub.html')

@app.route('/scalar', methods=['GET', 'POST'])
def scalar():
    """
    Multiplicação de matriz por escalar.
    """
    if request.method == 'POST':
        # Lógica para Multiplicação por escalar
        matriz_a = Matrix(2, 2) # matriz 2 por 2 nula para testar
        return matriz_a.scalar_multiply(2)
    return render_template('scalar.html')

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    """
    Multiplicação de matrizes.
    """
    if request.method == 'POST':
        # Lógica para Multiplicação de matrizes
        matriz_a = Matrix(2, 2)
        matriz_b = Matrix(2, 2) 
        return matriz_a.multiply(matriz_b)
    return render_template('multiply.html')

@app.route('/determinant', methods=['GET', 'POST'])
def determinant():
    """
    Cálculo do Determinante.
    """
    if request.method == 'POST':
        # Lógica para Determinante
        matriz_a = Matrix(2, 2) # matriz 2 por 2 nula para testar
        return matriz_a.determinant()
    return render_template('determinant.html')

@app.route('/inverse', methods=['GET', 'POST'])
def inverse():
    """
    Matriz Inversa.
    """
    if request.method == 'POST':
        # Lógica para Matriz Inversa
        matriz_a = Matrix(2, 2) # matriz 2 por 2 nula para testar
        return matriz_a.inverse()
    return render_template('inverse.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    """
    Criptografia (provavelmente usando a matriz como chave ou método Hill).
    """
    if request.method == 'POST':
        # Lógica para Criptografia
        return jsonify({'result': 'Funcionalidade de Criptografia (a implementar)'})
    return render_template('encrypt.html')

# --- Execução do Servidor ---

if __name__ == '__main__':
    # Em ambiente de desenvolvimento, usar debug=True
    app.run(debug=True)