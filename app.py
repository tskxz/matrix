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
            
            if 'rows' not in data or 'cols' not in data:
                return jsonify({'error': 'Dimensões não fornecidas'}), 400
            
            if 'matrix_a' not in data or 'matrix_b' not in data:
                return jsonify({'error': 'Matrizes não fornecidas'}), 400
            
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
            
            if 'rows' not in data or 'cols' not in data:
                return jsonify({'error': 'Dimensões não fornecidas'}), 400
            
            if 'matrix_a' not in data:
                return jsonify({'error': 'Matriz não fornecida'}), 400
            
            if 'scalar' not in data:
                return jsonify({'error': 'Escalar não fornecido'}), 400
            
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

#Multiplicacao
@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        try:
            
            data = request.get_json(force=True)
            
            if not data:
                return jsonify({'error': 'Invalid JSON'}), 400
            
            if 'matrix_a' not in data or 'matrix_b' not in data:
                return jsonify({'error': 'Matrizes não fornecidas'}), 400
            
            matrix_a_data = data['matrix_a']
            matrix_b_data = data['matrix_b']
            
            rows_a = len(matrix_a_data)
            cols_a = len(matrix_a_data[0]) if matrix_a_data else 0
            rows_b = len(matrix_b_data)
            cols_b = len(matrix_b_data[0]) if matrix_b_data else 0
            if cols_a != rows_b:
                return jsonify({
                    'error': f'Matrizes incompatíveis: A.cols({cols_a}) ≠ B.rows({rows_b})'
                }), 400
            
            matrix_a = Matrix(rows_a, cols_a, matrix_a_data)
            matrix_b = Matrix(rows_b, cols_b, matrix_b_data)
            
            result = matrix_a.multiply(matrix_b)
            
            return jsonify({
                'matrix_a': matrix_a.to_list(),
                'matrix_b': matrix_b.to_list(),
                'result': result.to_list(),
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    return render_template('multiply.html')

@app.route('/determinant', methods=['GET', 'POST'])     

def determinant():
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            
            if not data:
                return jsonify({'error': 'Invalid JSON'}), 400
            
            if 'size' not in data or 'matrix' not in data:
                return jsonify({'error': 'Tamanho ou matriz não fornecidos'}), 400
            
            size = data['size']
            matrix_data = data['matrix']
            method = data.get('method', 'auto')
            
            # Validar se é matriz quadrada
            if len(matrix_data) != size or any(len(row) != size for row in matrix_data):
                return jsonify({'error': 'A matriz deve ser quadrada'}), 400
            
            # Criar objeto Matrix
            matrix = Matrix(size, size, matrix_data)
            
            if not matrix.is_square():
                return jsonify({'error': 'Determinante só existe para matrizes quadradas'}), 400
            
            # Calcular determinante
            try:
                determinant_value = matrix.determinant()
                
                # Arredondar para evitar -0.0000000000001
                if abs(determinant_value) < 1e-10:
                    determinant_value = 0.0
                
                result = {
                    'matrix': matrix.to_list(),
                    'determinant': determinant_value,
                    'size': size,
                    'method': method,
                    'is_singular': determinant_value == 0
                }
                
                # Adicionar detalhes do método se for pequena
                if size <= 3:
                    if size == 2:
                        a, b = matrix_data[0][0], matrix_data[0][1]
                        c, d = matrix_data[1][0], matrix_data[1][1]
                        result['method_details'] = f"2×2: det = ad - bc = ({a}×{d}) - ({b}×{c}) = {a*d} - {b*c} = {determinant_value}"
                    elif size == 3:
                        a, b, c = matrix_data[0][0], matrix_data[0][1], matrix_data[0][2]
                        d, e, f = matrix_data[1][0], matrix_data[1][1], matrix_data[1][2]
                        g, h, i = matrix_data[2][0], matrix_data[2][1], matrix_data[2][2]
                        result['method_details'] = f"3×3 (Sarrus):\n"
                        result['method_details'] += f"  (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)\n"
                        result['method_details'] += f"  = ({a}×{e}×{i} + {b}×{f}×{g} + {c}×{d}×{h}) - ({c}×{e}×{g} + {b}×{d}×{i} + {a}×{f}×{h})\n"
                        result['method_details'] += f"  = ({a*e*i} + {b*f*g} + {c*d*h}) - ({c*e*g} + {b*d*i} + {a*f*h})\n"
                        result['method_details'] += f"  = {determinant_value}"
                
                return jsonify(result)
                
            except Exception as e:
                return jsonify({'error': f'Erro ao calcular determinante: {str(e)}'}), 400
            
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    return render_template('determinant.html')

@app.route('/inverse', methods=['GET', 'POST'])
def inverse():
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            
            if not data:
                return jsonify({'error': 'Invalid JSON'}), 400
            
            if 'size' not in data or 'matrix' not in data:
                return jsonify({'error': 'Tamanho ou matriz não fornecidos'}), 400
            
            size = data['size']
            matrix_data = data['matrix']
            method = data.get('method', 'adjugate')  # 'adjugate' ou 'gauss-jordan'
            
            # Validar se é matriz quadrada
            if len(matrix_data) != size or any(len(row) != size for row in matrix_data):
                return jsonify({'error': 'A matriz deve ser quadrada'}), 400
            
            # Criar objeto Matrix
            matrix = Matrix(size, size, matrix_data)
            
            # Verificar se é quadrada
            if not matrix.is_square():
                return jsonify({'error': 'Matriz inversa só existe para matrizes quadradas'}), 400
            
            # Calcular determinante primeiro
            determinant_value = matrix.determinant()
            
            # Verificar se é singular
            if abs(determinant_value) < 1e-10:
                result = {
                    'matrix': matrix.to_list(),
                    'determinant': 0.0,
                    'is_singular': True,
                    'error': 'Matriz singular (determinante = 0). Não tem inversa.',
                    'size': size
                }
                return jsonify(result)
            
            # Calcular inversa com método escolhido
            if method == 'gauss-jordan':
                inverse_matrix = matrix.gauss_jordan_inverse()
            else:
                inverse_matrix = matrix.inverse()
            
            # Verificar o resultado
            verification = matrix.verify_inverse(inverse_matrix)
            
            # Preparar resposta
            result = {
                'matrix': matrix.to_list(),
                'inverse': inverse_matrix.to_list(),
                'determinant': determinant_value,
                'is_singular': False,
                'size': size,
                'method': method,
                'verification': verification,
                'verification_ok': verification['is_correct']
            }
            
            # Adicionar detalhes para matrizes 2x2
            if size == 2:
                a, b = matrix_data[0][0], matrix_data[0][1]
                c, d = matrix_data[1][0], matrix_data[1][1]
                det = determinant_value
                result['formula_details'] = f"Inversa 2×2: (1/det) × [[d, -b], [-c, a]] = (1/{det}) × [[{d}, -{b}], [-{c}, {a}]]"
            
            return jsonify(result)
            
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': f'Erro ao calcular inversa: {str(e)}'}), 500
    
    return render_template('inverse.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    """
    Criptografia de mensagens usando multiplicação matricial.
    """
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            
            if not data:
                return jsonify({'error': 'Invalid JSON'}), 400
            
            message = data.get('message', '')
            matrix_data = data.get('encoding_matrix', [])
            operation = data.get('operation', 'encrypt')
            
            if not message:
                return jsonify({'error': 'Mensagem não pode estar vazia'}), 400
            
            if not matrix_data:
                return jsonify({'error': 'Matriz codificadora não fornecida'}), 400
            
            size = len(matrix_data)
            
            # Validar matriz quadrada
            if any(len(row) != size for row in matrix_data):
                return jsonify({'error': 'A matriz deve ser quadrada'}), 400
            
            # Criar matriz codificadora
            encoding_matrix = Matrix(size, size, matrix_data)
            
            # Verificar se a matriz é invertível
            det = encoding_matrix.determinant()
            if abs(det) < 1e-10:
                return jsonify({
                    'error': 'Matriz singular (det=0). Escolha uma matriz invertível para criptografia.'
                }), 400
            
            if operation == 'encrypt':
                # Criptografar
                result = encoding_matrix.encrypt_message(message, encoding_matrix)
                
                return jsonify({
                    'operation': 'encrypt',
                    'original_message': message,
                    'encoding_matrix': encoding_matrix.to_list(),
                    'message_matrix': result['message_matrix'].to_list(),
                    'encrypted_matrix': result['encrypted_matrix'].to_list(),
                    'numeric_sequence': result['numeric_sequence'],
                    'determinant': det
                })
            
            elif operation == 'decrypt':
                # Para descriptografar, precisamos da matriz criptografada
                encrypted_data = data.get('encrypted_matrix', [])
                
                if not encrypted_data:
                    return jsonify({'error': 'Matriz criptografada não fornecida'}), 400
                
                # Criar matriz criptografada
                encrypted_rows = len(encrypted_data)
                encrypted_cols = len(encrypted_data[0]) if encrypted_data else 0
                encrypted_matrix = Matrix(encrypted_rows, encrypted_cols, encrypted_data)
                
                # Calcular matriz decodificadora (inversa)
                decoding_matrix = encoding_matrix.inverse()
                
                # Descriptografar
                result = encoding_matrix.decrypt_message(encrypted_matrix, decoding_matrix)
                
                return jsonify({
                    'operation': 'decrypt',
                    'encrypted_matrix': encrypted_matrix.to_list(),
                    'decoding_matrix': decoding_matrix.to_list(),
                    'message_matrix': result['message_matrix'].to_list(),
                    'decrypted_message': result['decrypted_message'],
                    'numeric_sequence': result['numeric_sequence']
                })
            
            else:
                return jsonify({'error': 'Operação inválida. Use "encrypt" ou "decrypt"'}), 400
                
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': f'Erro: {str(e)}'}), 500
    
    return render_template('encrypt.html')

@app.route('/check_matrix', methods=['POST'])
def check_matrix():
    """Endpoint para verificar se uma matriz é válida para criptografia."""
    try:
        data = request.get_json(force=True)
        
        matrix_data = data['matrix']
        size = data['size']
        
        # Validar tamanho
        if len(matrix_data) != size or any(len(row) != size for row in matrix_data):
            return jsonify({'valid': False, 'error': 'Matriz não é quadrada'})
        
        # Criar objeto Matrix
        matrix = Matrix(size, size, matrix_data)
        
        # Verificar se é quadrada
        if not matrix.is_square():
            return jsonify({'valid': False, 'error': 'Matriz não é quadrada'})
        
        # Calcular determinante
        try:
            det = matrix.determinant()
            if abs(det) < 1e-10:
                return jsonify({
                    'valid': False, 
                    'error': 'Matriz singular (determinante = 0)',
                    'determinant': det
                })
            
            return jsonify({
                'valid': True,
                'determinant': det,
                'message': 'Matriz válida para criptografia'
            })
            
        except Exception as e:
            return jsonify({'valid': False, 'error': f'Erro ao calcular determinante: {str(e)}'})
        
    except Exception as e:
        return jsonify({'valid': False, 'error': str(e)})
        
# --- Execução do Servidor ---

if __name__ == '__main__':
    # Em ambiente de desenvolvimento, usar debug=True
    app.run(debug=True)