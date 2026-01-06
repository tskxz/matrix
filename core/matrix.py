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
    
    def _get_minor(self, row, col):
        # ter a matriz menor, remover linha e coluna para calcular determinante com metodo laplace
        minor_data = []
        for i in range(self.rows):
            if i == row:
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

    def get_cofactor(self, row, col):
        """Calculate the cofactor at position (row, col)."""
        minor = self._get_minor(row, col)
        sign = 1 if (row + col) % 2 == 0 else -1
        return sign * minor.determinant()

    def adjugate(self):
        """Calculate the adjugate (adjoint) matrix."""
        if not self.is_square():
            raise ValueError("Adjunta só existe para matrizes quadradas")
        
        n = self.rows
        adj_data = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                # adjunta é a transposta da matriz de cofatores
                adj_data[j][i] = self.get_cofactor(i, j)
        
        return Matrix(n, n, adj_data)

    def transpose(self):
        """Return the transpose of the matrix."""
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(self.cols, self.rows, transposed_data)
  
    def identity(self, n=None):
        """Create an identity matrix of size n×n."""
        if n is None:
            n = self.rows
        identity_data = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        return Matrix(n, n, identity_data)

    def inverse(self):
        """Calculate matrix inverse using adjugate method."""
        # Verificar se é quadrada
        if not self.is_square():
            raise ValueError("Matriz inversa só existe para matrizes quadradas")
        
        # Calcular determinante
        det = self.determinant()
        
        # Verificar se é singular
        if abs(det) < 1e-10:
            raise ValueError("Matriz singular (determinante = 0). Não tem inversa.")
        
        n = self.rows
        
        # matriz 1x1
        if n == 1:
            inverse_data = [[1 / self.data[0][0]]]
            return Matrix(1, 1, inverse_data)
        
        # matriz 2x2
        if n == 2:
            a, b = self.data[0][0], self.data[0][1]
            c, d = self.data[1][0], self.data[1][1]
            
            inverse_data = [
                [d / det, -b / det],
                [-c / det, a / det]
            ]
            return Matrix(2, 2, inverse_data)
        
        # Matrizes maiores: método da adjunta
        # A⁻¹ = (1/det(A)) * adj(A)
        adj = self.adjugate()
        scalar = 1 / det
        
        # Multiplicar adjunta pelo escalar 1/det
        inverse_data = [[adj.data[i][j] * scalar for j in range(n)] for i in range(n)]
        
        # Arredondar valores próximos de zero
        for i in range(n):
            for j in range(n):
                if abs(inverse_data[i][j]) < 1e-10:
                    inverse_data[i][j] = 0.0
        
        return Matrix(n, n, inverse_data)

    def gauss_jordan_inverse(self):
        """Calculate inverse using Gauss-Jordan elimination (método alternativo)."""
        if not self.is_square():
            raise ValueError("Matriz deve ser quadrada para ter inversa")
        
        n = self.rows
        det = self.determinant()
        
        if abs(det) < 1e-10:
            raise ValueError("Matriz singular (determinante = 0)")
        
        # Criar matriz aumentada [A|I]
        augmented = [[0 for _ in range(2*n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                augmented[i][j] = self.data[i][j]
            augmented[i][n + i] = 1
        
        # Aplicar eliminação de Gauss-Jordan
        for i in range(n):
            # Pivot
            pivot = augmented[i][i]
            
            # Normalizar linha
            for j in range(2*n):
                augmented[i][j] /= pivot
            
            # Eliminar outras linhas
            for k in range(n):
                if k != i:
                    factor = augmented[k][i]
                    for j in range(2*n):
                        augmented[k][j] -= factor * augmented[i][j]
        
        # Extrair a inversa da parte direita
        inverse_data = [[augmented[i][n + j] for j in range(n)] for i in range(n)]
        
        # Arredondar valores próximos de zero
        for i in range(n):
            for j in range(n):
                if abs(inverse_data[i][j]) < 1e-10:
                    inverse_data[i][j] = 0.0
        
        return Matrix(n, n, inverse_data)

    def verify_inverse(self, inverse_matrix):
        """Verify that A × A⁻¹ = I."""
        n = self.rows
        
        # Multiplicar A × A⁻¹
        product = self.multiply(inverse_matrix)
        
        # Criar matriz identidade
        identity = self.identity(n)
        
        # Verificar se o produto é aproximadamente a identidade
        is_correct = True
        max_error = 0
        
        for i in range(n):
            for j in range(n):
                error = abs(product.data[i][j] - identity.data[i][j])
                max_error = max(max_error, error)
                if error > 1e-8:
                    is_correct = False
        
        return {
            'is_correct': is_correct,
            'product_matrix': product.to_list(),
            'identity_matrix': identity.to_list(),
            'max_error': max_error
        }

    def encrypt_message(self, message, encoding_matrix):
        """
        Encrypt a message using matrix multiplication.
        
        Args:
            message: String to encrypt (letters, spaces, punctuation)
            encoding_matrix: Matrix object used for encoding (must be square)
        
        Returns:
            dict with 'encrypted_matrix', 'message_matrix', 'numeric_sequence'
        """
        if not isinstance(encoding_matrix, Matrix):
            raise ValueError("Encoding matrix must be a Matrix object")
        
        if not encoding_matrix.is_square():
            raise ValueError("Encoding matrix must be square")
        
        # Mapping de letras para números
        char_map = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
            'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
            'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
            'Z': 26, ' ': 27, '.': 28, 'Ú': 29, 'Ã': 30, 'Ç': 31, 'Õ': 32, 'É': 33
        }
        
        #  Converter mensagem para sequência numérica
        message = message.upper()
        numeric_sequence = [char_map.get(char, 27) for char in message]
        
        # Determinar dimensões da matriz
        rows = encoding_matrix.rows
        cols = len(numeric_sequence) // rows
        
        # Preencher com espaços (27) se necessário
        if len(numeric_sequence) % rows != 0:
            cols += 1
            padding_needed = (rows * cols) - len(numeric_sequence)
            numeric_sequence.extend([27] * padding_needed)
        
        # Criar a mensagem
        message_data = []
        for i in range(rows):
            row = []
            for j in range(cols):
                index = j * rows + i
                row.append(numeric_sequence[index])
            message_data.append(row)
        
        message_matrix = Matrix(rows, cols, message_data)
        
        # Encriptar: A × M = C
        encrypted_matrix = encoding_matrix.multiply(message_matrix)
        
        return {
            'encrypted_matrix': encrypted_matrix,
            'message_matrix': message_matrix,
            'numeric_sequence': numeric_sequence,
            'original_message': message
        }
    
    def decrypt_message(self, encrypted_matrix, decoding_matrix):
        """
        Decrypt an encrypted matrix using the inverse matrix.
        
        Args:
            encrypted_matrix: Matrix object with encrypted data
            decoding_matrix: Inverse of the encoding matrix
        
        Returns:
            dict with 'decrypted_message', 'numeric_sequence', 'message_matrix'
        """
        if not isinstance(encrypted_matrix, Matrix):
            raise ValueError("Encrypted matrix must be a Matrix object")
        
        if not isinstance(decoding_matrix, Matrix):
            raise ValueError("Decoding matrix must be a Matrix object")
        
        # Mapping reverso
        reverse_map = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I',
            10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q',
            18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
            26: 'Z', 27: ' ', 28: '.', 29: 'Ú', 30: 'Ã', 31: 'Ç', 32: 'Õ', 33: 'É'
        }
        
        # Decriptar: B × C = M
        message_matrix = decoding_matrix.multiply(encrypted_matrix)
        
        # Extrair numeros da matriz
        numeric_sequence = []
        for j in range(message_matrix.cols):
            for i in range(message_matrix.rows):
                numeric_sequence.append(round(message_matrix.get_element(i + 1, j + 1)))
        
        # Converter para mensagem
        decrypted_message = ''.join([reverse_map.get(num, ' ') for num in numeric_sequence])
        
        return {
            'decrypted_message': decrypted_message.rstrip(),
            'numeric_sequence': numeric_sequence,
            'message_matrix': message_matrix
        }