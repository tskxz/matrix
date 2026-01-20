class Matrix:
    
    # Characters to numbers mapping for encryption/decryption
    CHAR_TO_NUM = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
        'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
        '.': 27, ',': 28, ' ': 29, '_': 29, '-': 30
    }

    # Reverse mapping from numbers to characters using CHAR_TO_NUM
    NUM_TO_CHAR = {v: k for k, v in CHAR_TO_NUM.items()}
    # Ensure ' ' space maps to 29 as well
    NUM_TO_CHAR[29] = ' '
    
    def __init__(self, rows, cols, data=None):
        # Intialize matrix with given rows and columns
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            if not isinstance(data, list):
                raise ValueError("Data deve ser uma lista")
            if len(data) != rows:
                raise ValueError(f"Número de linhas incorreto: esperado {rows}, recebido {len(data)}")

            for i, row in enumerate(data):
                if not isinstance(row, list):
                    raise ValueError(f"Linha {i} não é uma lista")
                if len(row) != cols:
                    raise ValueError(f"Linha {i}: esperado {cols} colunas, recebido {len(row)} colunas")
            
            self.data = [row[:] for row in data]
    
    def __str__(self):
        # String representation of the matrix
        return "\n".join("[" + " ".join(f"{x:8.2f}" for x in row) + "]" for row in self.data)
    
    def __repr__(self):
        # Official representation in matrix form
        return f"Matrix({self.rows}×{self.cols})"
    
    def to_list(self):
        # Convert matrix data to a list of lists
        return [row[:] for row in self.data]
    
    def get_element(self, row, col):
        # Get element at specified row and column
        pass
    
    def set_element(self, row, col, value):
        # Set element at specified row and column
        pass
    
    def is_square(self):
        # Check if the matrix is square (rows == cols)
        return self.rows == self.cols
    
    def dimensions(self):
        # Return the dimensions of the matrix as (rows, cols)
        return (self.rows, self.cols)
    
    def add(self, other):
        # Add two matrices (A + B)
        if not isinstance(other, Matrix):
            raise TypeError("Só é possível adicionar outra Matrix")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"Dimensões incompatíveis: {self.dimensions()} vs {other.dimensions()}")
        
        # i = rows, j = cols
        result_data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result_data)
    
    def subtract(self, other):
        # Subtract two matrices (A - B)
        if not isinstance(other, Matrix):
            raise TypeError("Só é possível subtrair outra Matrix")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"Dimensões incompatíveis: {self.dimensions()} vs {other.dimensions()}")
        
        # i = rows, j = cols
        result_data = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result_data)
    
    def scalar_multiply(self, scalar):
        # Multiply matrix by a scalar value (scalar number * A)
        result_data = [[self.data[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result_data)
    
    def multiply(self, other):
        # Multiply two matrices (A * B)
        if not isinstance(other, Matrix):
            raise ValueError("Só é possivel multiplicar por outra Matrix")
        if self.cols != other.rows:
            raise ValueError(f"Dimensões incompatíveis para multiplicar | Tem de ser igual {self.cols} = {other.rows}")
        
        # i = rows, A(k)= cols, B(k) = rows, j = cols
        result_data = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(self.rows, other.cols, result_data)
    
    def transpose(self):
        # Transpose the matrix (A^T)
        result_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(self.cols, self.rows, result_data)
    
    def determinant(self):
        # Calculate the determinant of the matrix (det(A))
        if not self.is_square():
            raise ValueError("Determinante só funciona para matrizes quadradas")
        
        if self.rows == 1:
            return self.data[0][0]
        
        if self.rows == 2:
            # (a*d - b*c)
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data [1][0]
        
        if self.rows == 3:
            # Sarrus Rule criss cross.
            a, b, c = self.data[0]
            d, e, f = self.data[1]
            g, h, i = self.data[2]

            return (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)
        
        # Laplace method for any of the above & +(3x3) matrices
        det = 0
        for j in range(self.cols):
            minor = self._get_minor(0, j)
            sign = (-1) ** j
            det += sign * self.data[0][j] * minor.determinant()
        return det
        
    
    def inverse(self):
        # Calculate the inverse of the matrix (A^-1)
        if not self.is_square():
            raise ValueError("Matriz inversa só existe para matrizes quadradas")
        
        det = self.determinant()
        if abs(det) < 1e-10:
            raise ValueError("Matriz singular (det=0), não possui inversa")
        
        adj = self._adjugate()
        return adj.scalar_multiply(1 / det)
    
    def _get_minor(self, row, col):
        # Get minor matrix after removing specified row and column (for determinant calculation)
        
        # i = rows, j = cols
        minor_data = [[self.data[i][j] for j in range(self.cols) if j != col] for i in range(self.rows) if i != row]
        return Matrix(self.rows - 1, self.cols - 1, minor_data)
    
    def _get_cofactor(self, row, col):
        # Get cofactor of element at specified row and column (for inverse calculation)
        minor = self._get_minor(row, col)
        sign = (-1) ** (row + col)
        return sign * minor.determinant()
    
    def _adjugate(self):
        # Calculate the adjugate of the matrix (for inverse calculation)
        cofactor_data = [[self._get_cofactor(i, j) for j in range(self.cols)] for i in range(self.rows)]
        cofactor_matrix = Matrix(self.rows, self.cols, cofactor_data)
        return cofactor_matrix.transpose()

    # --------------Encryption/Decryption specific methods--------------
    @staticmethod
    def char_to_num(char):
        # Convert character to corresponding number based on CHAR_TO_NUM mapping "encryption"
        return Matrix.CHAR_TO_NUM.get(char.upper(), 29)
    
    @staticmethod
    def num_to_char(num):
        # Convert number to corresponding character based on CHAR_TO_NUM mapping "decryption"
        return Matrix.NUM_TO_CHAR.get(num, ' ')
    
    def encrypt_message(self, message):
        # Encrypt message using matrix multiplication (message_matrix * encoding_matrix = encrypted_matrix)
        message = message.upper()
        numbers = [Matrix.char_to_num(a) for a in message]
        
        while len(numbers) % self.rows != 0:
            numbers.append(29)
        
        num_cols = len(numbers) // self.rows
        # i = rows, j = cols
        message_matrix_data = [[numbers[i * num_cols + j] for j in range(num_cols)] for i in range(self.rows)]
        message_matrix = Matrix(self.rows, num_cols, message_matrix_data)
        
        encrypted_matrix = self.multiply(message_matrix)
        
        numeric_sequence = []
        for rows in range(encrypted_matrix.rows):
            for cols in range(encrypted_matrix.cols):
                numeric_sequence.append(int(encrypted_matrix.data[rows][cols]))
        
        return {
            'message_matrix': message_matrix.to_list(),
            'encrypted_matrix': encrypted_matrix,
            'numeric_sequence': numeric_sequence
        }
    
    def decrypt_message(self, encrypted_matrix):
        # Decrypt message using matrix multiplication (encrypted_matrix * decoding_matrix = original_message_matrix)
        decoding_matrix = self.inverse()
        message_matrix = decoding_matrix.multiply(encrypted_matrix)
        
        numbers = []
        for rows in range(message_matrix.rows):
            for cols in range(message_matrix.cols):
                numbers.append(round(message_matrix.data[rows][cols]))
        
        decrypted_message = ''.join(Matrix.num_to_char(num) for num in numbers)
        
        return {
            'message_matrix': message_matrix.to_list(),
            'decrypted_message': decrypted_message,
            'numeric_sequence': numbers
        }