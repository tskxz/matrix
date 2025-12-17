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
        try:
            if not request.data:
                return jsonify({'error': 'No data received'}), 400
                
            data = request.get_json(force=True)
            
            if not data:
                return jsonify({'error': 'Invalid JSON'}), 400
            
            matrix_a = Matrix(data['rows'], data['cols'], data['matrix_a'])
            matrix_b = Matrix(data['rows'], data['cols'], data['matrix_b'])
            
            result = matrix_a.add(matrix_b) if data['operation'] == 'sum' else matrix_a.subtract(matrix_b)
            op_name = 'Soma' if data['operation'] == 'sum' else 'Subtração'
            
            return jsonify({
                'matrix_a': matrix_a.to_list(),
                'matrix_b': matrix_b.to_list(),
                'result': result['data'],
                'operation': op_name,
                'dimensions': f"{data['rows']}x{data['cols']}"
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    return render_template('sum_sub.html')

@app.route('/scalar', methods=['GET', 'POST'])
def scalar():
    """
    Multiplicação de matriz por escalar.
    """
    if request.method == "POST":
        try:
            if not request.data:
                return jsonify({'error': 'No data received'}), 400
            data = request.get_json(force=True)
            print(data)
            if not data:
                return jsonify({'error': 'Invalid JSON'}), 400
            matrix_a = Matrix(data['rows'], data['cols'], data['matrix_a'])
            result = matrix_a.scalar_multiply(data['scalar'])

            return jsonify({
                'matrix_a': matrix_a.to_list(),
                'result': result['data'],
                'dimensions': f"{data['rows']}x{data['cols']}"
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return render_template('scalar.html')

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    """
    Multiplicação de matrizes.
    """
    return render_template('multiply.html')

@app.route('/determinant', methods=['GET', 'POST'])
def determinant():
    """
    Cálculo do Determinante.
    """
    return render_template('determinant.html')

@app.route('/inverse', methods=['GET', 'POST'])
def inverse():
    """
    Matriz Inversa.
    """
    return render_template('inverse.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    """
    Criptografia (provavelmente usando a matriz como chave ou método Hill).
    """
    return render_template('encrypt.html')

# --- Execução do Servidor ---

if __name__ == '__main__':
    # Em ambiente de desenvolvimento, usar debug=True
    app.run(debug=True)