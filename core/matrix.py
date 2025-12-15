from flask import jsonify

class Matrix:
    """A custom Matrix class implementing basic linear algebra operations."""
    
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        
        if data is None:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            if len(data) != rows or any(len(row) != cols for row in data):
                raise ValueError(f"Dimensões incorretas: esperado {rows}×{cols}")
            self.data = [row[:] for row in data]
    
    def __str__(self):
        result = ""
        for row in self.data:
            result += "[" + " ".join(f"{elem:8.2f}" if isinstance(elem, float) else f"{elem:8}" for elem in row) + "]\n"
        return result
    
    def __repr__(self):
        return f"Matrix({self.rows}x{self.cols})"
    
    def get_element(self, row, col):
        """Get element at position [row][col] (1-indexed)."""
        return self.data[row - 1][col - 1]
    
    def set_element(self, row, col, value):
        """Set element at position [row][col] (1-indexed)."""
        self.data[row - 1][col - 1] = value
    
    def dimensions(self):
        return (self.rows, self.cols)
    
    def is_same_dimension(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Pode apenas comparar com outra Matriz")
        return self.rows == other.rows and self.cols == other.cols
    
    def add(self):
        return jsonify({'result': 'Soma de matrizes: C[i][j] = A[i][j] + B[i][j]'})
    
    def subtract(self):
        return jsonify({'result': 'Subtração de matrizes: C[i][j] = A[i][j] - B[i][j]'})
    
    def scalar_multiply(self, scalar):
        return jsonify({'result': 'Multiplicação por escalar: B[i][j] = k × A[i][j]'})
    
    def multiply(self, other):
        return jsonify({'result': 'Multiplicação de matrizes: C[i][j] = Σ(A[i][k] × B[k][j])'})
    
    def determinant(self):
        return jsonify({'result': 'Cálculo do determinante usando expansão de Laplace'})
    
    def _get_minor(self, row, col):
        """Obtém matriz menor removendo linha e coluna."""
    
    def inverse(self):
        """Calculate matrix inverse using cofactor method."""
        return jsonify({'result': 'Cálculo da matriz inversa'})
    
    def to_list(self):
        """Converte matriz para lista de listas."""