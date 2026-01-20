from flask import Flask, render_template, request, jsonify
from core.matrix import Matrix

app = Flask(__name__)

# Reader Function

def handle_matrix_operation(operation_func, *args, **spargs):
    """
    Generic handler for matrix operations.
    Catches errors and returns proper JSON response.
    """
    try:
        result = operation_func(*args, **spargs)
        
        # If result is a Matrix object, convert to list
        if isinstance(result, Matrix):
            return jsonify({'result': result.to_list()})
        # if result is already a dict, return it as is
        elif isinstance(result, dict):
            return jsonify(result)
        # else return normal result
        else:
            return jsonify({'result': result})
            
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Erro: {str(e)}'}), 500

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
    
    data = request.get_json()
    matrix_a = Matrix(data['rows'], 
                      data['cols'], 
                      data['matrix_a'])
    
    matrix_b = Matrix(data['rows'], 
                      data['cols'], 
                      data['matrix_b'])
    
    if data['operation'] == 'add':
        return handle_matrix_operation(matrix_a.add, matrix_b)
    elif data['operation'] == 'subtract':
        return handle_matrix_operation(matrix_a.subtract, matrix_b)
    else:
        return jsonify({'error': 'Operação inválida'}), 400

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    """Multiplicação de matrizes."""
    if request.method == 'GET':
        return render_template('multiply.html')
    
    data = request.get_json()
    matrix_a = Matrix(data['rows_a'], 
                      data['cols_a'], 
                      data['matrix_a'])
    
    matrix_b = Matrix(data['rows_b'], 
                      data['cols_b'], 
                      data['matrix_b'])
    
    return handle_matrix_operation(matrix_a.multiply, matrix_b)

@app.route('/transpose', methods=['GET', 'POST'])
def transpose():
    """Transpor uma Matriz"""
    if request.method == 'GET':
        return render_template('transpose.html')
    
    data = request.get_json()
    matrix = Matrix(data['rows'],
                    data['cols'],
                    data['matrix'])
    
    return handle_matrix_operation(matrix.transpose)

@app.route('/scalar', methods=['GET', 'POST'])
def scalar():
    """Multiplicação de matriz por escalar."""
    if request.method == 'GET':
        return render_template('scalar.html')
    
    data = request.get_json()
    matrix = Matrix(data['rows'], 
                    data['cols'], 
                    data['matrix'])
    
    return handle_matrix_operation(matrix.scalar_multiply, data['scalar'])

@app.route('/determinant', methods=['GET', 'POST'])
def determinant():
    """Cálculo de determinante."""
    if request.method == 'GET':
        return render_template('determinant.html')
    
    data = request.get_json()
    matrix = Matrix(data['size'], 
                    data['size'], 
                    data['matrix'])
    
    return handle_matrix_operation(matrix.determinant)

@app.route('/inverse', methods=['GET', 'POST'])
def inverse():
    """Cálculo de matriz inversa."""
    if request.method == 'GET':
        return render_template('inverse.html')
    
    data = request.get_json()
    matrix = Matrix(data['size'], 
                    data['size'], 
                    data['matrix'])
    
    return handle_matrix_operation(matrix.inverse)

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    """Criptografia de mensagens usando multiplicação matricial."""
    if request.method == 'GET':
        return render_template('encrypt.html')
    
    data = request.get_json()
    encoding_matrix = Matrix(data['size'], 
                             data['size'], 
                             data['encoding_matrix'])
    
    result = encoding_matrix.encrypt_message(data['message'])
    
    return jsonify({
        'encrypted_matrix': result['encrypted_matrix'].to_list(),
        'numeric_sequence': result['numeric_sequence']
    })

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    """Descriptografia de mensagens usando multiplicação matricial."""
    if request.method == 'GET':
        return render_template('decrypt.html')
    
    data = request.get_json()
    encoding_matrix = Matrix(data['size'], 
                             data['size'], 
                             data['encoding_matrix'])
    
    encrypted_matrix = Matrix(data['size'], 
                              data['encrypted_cols'], 
                              data['encrypted_matrix'])
    
    return handle_matrix_operation(encoding_matrix.decrypt_message, encrypted_matrix)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)