from flask import Flask, render_template, request, jsonify
from core.matrix import Matrix

app = Flask(__name__)

def parse_matrix_from_form(form_data, prefix, rows, cols):
    """Parse matrix from form data."""
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            key = f"{prefix}_{i}_{j}"
            value = form_data.get(key)
            if value is None:
                raise ValueError(f"Missing value at [{i+1}][{j+1}]")
            row.append(float(value))
        matrix.append(row)
    return matrix

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
        try:
            data = request.form
            rows = int(data.get('rows'))
            cols = int(data.get('cols'))
            operation = data.get('operation')
            
            matrix_a = Matrix(rows, cols, parse_matrix_from_form(data, 'matrix_a', rows, cols))
            matrix_b = Matrix(rows, cols, parse_matrix_from_form(data, 'matrix_b', rows, cols))
            
            result = matrix_a.add(matrix_b) if operation == 'sum' else matrix_a.subtract(matrix_b)
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return render_template('sum_sub.html')

@app.route('/scalar', methods=['GET', 'POST'])
def scalar():
    """
    Multiplicação de matriz por escalar.
    """
    if request.method == 'POST':
        # Lógica para Multiplicação por escalar
        return jsonify({'result': 'Cálculo de Multiplicação por Escalar (a implementar)'})
    return render_template('scalar.html')

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    """
    Multiplicação de matrizes.
    """
    if request.method == 'POST':
        # Lógica para Multiplicação de matrizes
        return jsonify({'result': 'Cálculo de Multiplicação de Matrizes (a implementar)'})
    return render_template('multiply.html')

@app.route('/determinant', methods=['GET', 'POST'])
def determinant():
    """
    Cálculo do Determinante.
    """
    if request.method == 'POST':
        # Lógica para Determinante
        return jsonify({'result': 'Cálculo de Determinante (a implementar)'})
    return render_template('determinant.html')

@app.route('/inverse', methods=['GET', 'POST'])
def inverse():
    """
    Matriz Inversa.
    """
    if request.method == 'POST':
        # Lógica para Matriz Inversa
        return jsonify({'result': 'Cálculo de Matriz Inversa (a implementar)'})
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