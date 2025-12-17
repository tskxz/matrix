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

#Soma&Subtracao
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
    return render_template('scalar.html')

#Multiplicacao
@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        try:
            print("[v0] Request content-type:", request.content_type)
            print("[v0] Request data:", request.data)
            
            data = request.get_json(force=True)
            print("[v0] Parsed JSON:", data)
            
            if not data or 'matrixA' not in data or 'matrixB' not in data:
                print("[v0] Missing matrixA or matrixB in request")
                return jsonify({'success': False, 'error': 'Dados de matriz inválidos'}), 400
            
            matrix_a_data = data['matrixA']
            matrix_b_data = data['matrixB']
            
            rows_a = len(matrix_a_data)
            cols_a = len(matrix_a_data[0]) if matrix_a_data else 0
            rows_b = len(matrix_b_data)
            cols_b = len(matrix_b_data[0]) if matrix_b_data else 0
            
            print(f"[v0] Matrix A: {rows_a}x{cols_a}, Matrix B: {rows_b}x{cols_b}")
            
            matrix_a = Matrix(rows_a, cols_a, matrix_a_data)
            matrix_b = Matrix(rows_b, cols_b, matrix_b_data)
            
            result = matrix_a.multiply(matrix_b)
            print("[v0] Multiplication successful")
            
            return jsonify({
                'success': True,
                'result': result['data'],
                'matrix_a': matrix_a.to_list(),
                'matrix_b': matrix_b.to_list(),
                'operation': 'Multiplicação',
                'dimensions_a': f"{rows_a}x{cols_a}",
                'dimensions_b': f"{rows_b}x{cols_b}",
                'dimensions_result': f"{result['rows']}x{result['cols']}"
            })
            
        except ValueError as e:
            print("[v0] ValueError:", str(e))
            return jsonify({'success': False, 'error': str(e)}), 400
        except Exception as e:
            print("[v0] Exception:", str(e))
            return jsonify({'success': False, 'error': str(e)}), 400
    
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