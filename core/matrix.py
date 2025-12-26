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
        return "\n".join("[" + " ".join(f"{x:8.2f}" for x in row) + "]" for row in self.data)
    
    def __repr__(self):
        """Return representation of the matrix."""
        return f"Matrix({self.rows}x{self.cols})"
    
    def get_element(self, row, col):
        """Get element at position [row][col] (1-indexed)."""
        return self.data[row - 1][col - 1]
    
    def set_element(self, row, col, value):
        """Set element at position [row][col] (1-indexed)."""
        self.data[row - 1][col - 1] = value
    
    def dimensions(self):
        """Return dimensions as tuple (rows, cols)."""
        return (self.rows, self.cols)
    
    def is_same_dimension(self, other):
        """Check if two matrices have the same dimensions."""
        if not isinstance(other, Matrix):
            raise TypeError("Can only compare with another Matrix")
        return self.rows == other.rows and self.cols == other.cols
    
    def to_list(self):
        return [row[:] for row in self.data]
    
    def is_square(self):
        # Validar que a matriz é quadrada (mesmo número de linhas e colunas)
        return self.cols == self.rows
    
    def _get_minor(self, rows, col):
        # ter a matriz menor, remover linha e coluna para calcular determinante com metodo laplace
        minor_data = []
        for i in range(self.rows):
            if i == rows:
                continue
            new_row = []
            for j in range(self.cols):
                if j == col:
                    continue
                new_row.append(self.data[i][j])
            minor_data.append(new_row)
        return Matrix(self.rows - 1, self.cols - 1, minor_data)

    def add(self, other):
        """Add two matrices: C[i][j] = A[i][j] + B[i][j]"""
        if not self.is_same_dimension(other):
            raise ValueError(f"Dimensões incompatíveis: {self.dimensions()} vs {other.dimensions()}")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return {'data': result}
    
    def subtract(self, other):
        """Subtract two matrices: C[i][j] = A[i][j] - B[i][j]"""
        if not self.is_same_dimension(other):
            raise ValueError(f"Dimensões incompatíveis: {self.dimensions()} vs {other.dimensions()}")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return {'data': result}
    
    def scalar_multiply(self, scalar):
        result = [[self.data[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return {'data': result}
    
    def multiply(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Operando deve ser uma Matrix")
    
        if self.cols != other.rows:
            raise ValueError(f"Não é possível multiplicar: A.cols({self.cols}) ≠ B.rows({other.rows})")
        
        # Inicializar matriz resultado
        result = Matrix(self.rows, other.cols)
        
        # Multiplicação matricial
        for i in range(self.rows):
            for j in range(other.cols):
                soma = 0
                for k in range(self.cols):  # ou other.rows
                    soma += self.data[i][k] * other.data[k][j]
                result.data[i][j] = soma
        
        return result
    
    def determinant(self):
        # calcular determinante com o uso de laplace
        if not self.is_square():
            raise ValueError("Determinante so tem pa matrizes quadradas")

        # matrizes 1x1
        if self.rows == 1:
            return self.data[0][0]
        
        # matrizes 2x2
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        
        # matrizes 3x3 (regra sarras)
        if self.rows == 3:
            a, b, c = self.data[0][0], self.data[0][1], self.data[0][2]
            d, e, f = self.data[1][0], self.data[1][1], self.data[1][2]
            g, h, i = self.data[2][0], self.data[2][1], self.data[2][2]
            
            # aquela cena de diagonal principal vezes diagonal secundaria
            return (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)
        
        # matrizes 4x4 ou maiores (cpfatores)
        det = 0
        for j in range(self.cols):
            minor = self._get_minor(0, j)
            cofactor = ((-1) ** j) * self.data[0][j] * minor.determinant()
            det += cofactor
        return det
    
    def inverse(self):
        """Calculate matrix inverse using cofactor method."""
        return {'result': 'Cálculo da matriz inversa'}
    
    def encrypt(self):
        """Encrypt the following message"""
        return {'result': 'Mensagem Encryptada'}
    
    def des_encrypt(self):
        """Des-Encrypt the following message"""
        return {'result': 'Mensagem Desencryptada'}