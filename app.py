from flask import Flask, render_template, request, jsonify
from core.matrix import Matrix

app = Flask(__name__)

def parse_matrix_from_form(form_data, prefix):
    """Parse matrix from form data in text format - auto-detect dimensions."""
    # Get the text from form data
    text = form_data.get(prefix)
    if not text:
        raise ValueError(f"Matriz {prefix} vazia")
    
    # Parse the text - format is "1 2 3 4\n5 6 7 8"
    lines = text.strip().split('\r\n')
    
    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]
    
    if not lines:
        raise ValueError(f"Matriz {prefix} não contém dados")
    
    # Split each line by spaces
    rows = []
    num_cols = None
    
    for line in lines:
        # Split by spaces and remove empty strings
        values = [val for val in line.split() if val]
        if not values:
            continue
            
        # Convert to float
        row = [float(val) for val in values]
        rows.append(row)
        
        # Check if all rows have same number of columns
        if num_cols is None:
            num_cols = len(row)
        elif len(row) != num_cols:
            raise ValueError(f"Matriz {prefix}: linhas têm número diferente de colunas")
    
    if not rows:
        raise ValueError(f"Matriz {prefix} não contém dados válidos")
    
    return rows, len(rows), num_cols

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
            print(data) 
            
            # o resultado disto e ImmutableMultiDict([('matrix_a', '1 2 5 2\r\n1 2 2 1'), ('matrix_b', '1 3 4 5\r\n1 1 1 2')])
            
            # isto da erro "int() argument must be a string, a bytes-like object or a real number, not 'NoneType'"
            #rows = int(data.get('rows'))
            #cols = int(data.get('cols'))

            matrix_a_data, rows_a, cols_a = parse_matrix_from_form(data, 'matrix_a')
            matrix_b_data, rows_b, cols_b = parse_matrix_from_form(data, 'matrix_b')
                        # Verificar se as matrizes têm as mesmas dimensões
            if rows_a != rows_b or cols_a != cols_b:
                return jsonify({
                    'error': f'Matrizes têm dimensões diferentes: A({rows_a}x{cols_a}) vs B({rows_b}x{cols_b})'
                }), 400
            
            # Criar objetos Matrix
            matrix_a = Matrix(rows_a, cols_a, matrix_a_data)
            matrix_b = Matrix(rows_b, cols_b, matrix_b_data)
            
            # Fazer a soma (por enquanto só soma)
            result = matrix_a.add(matrix_b)
            
            return jsonify({
                'matrix_a': matrix_a_data,
                'matrix_b': matrix_b_data,
                'result': result.to_list() if hasattr(result, 'to_list') else str(result),
                'dimensions': f'{rows_a}x{cols_a}'
            })
            
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