class Matrix:
    
    def __init__(self, rows, cols, data=None):
        # Intialize matrix with given rows and columns
        pass
    
    def __str__(self):
        # String representation of the matrix
        pass
    
    def __repr__(self):
        # Official representation in matrix form
        pass
    
    def to_list(self):
        # Convert matrix data to a list of lists
        pass
    
    def get_element(self, row, col):
        # Get element at specified row and column
        pass
    
    def set_element(self, row, col, value):
        # Set element at specified row and column
        pass
    
    def is_square(self):
        # Check if the matrix is square (rows == cols)
        pass
    
    def dimensions(self):
        # Return the dimensions of the matrix as (rows, cols)
        pass
    
    def add(self, other):
        # Add two matrices (A + B)
        pass
    
    def subtract(self, other):
        # Subtract two matrices (A - B)
        pass
    
    def scalar_multiply(self, scalar):
        # Multiply matrix by a scalar value (scalar number * A)
        pass
    
    def multiply(self, other):
        # Multiply two matrices (A * B)
        pass
    
    def transpose(self):
        # Transpose the matrix (A^T)
        pass
    
    def determinant(self):
        # Calculate the determinant of the matrix (det(A))
        pass
    
    def inverse(self):
        # Calculate the inverse of the matrix (A^-1)
        pass
    
    def get_minor(self, row, col):
        # Get minor matrix after removing specified row and column (for determinant calculation)
        pass
    
    def get_cofactor(self, row, col):
        # Get cofactor of element at specified row and column (for determinant calculation)
        pass
    
    def adjugate(self):
        # Calculate the adjugate of the matrix (for inverse calculation)
        pass

    CHAR_TO_NUM = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
        'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
        '.': 27, ',': 28, '_': 29, ' ': 29, '-': 30
    }

    def char_to_num(char):
        # Convert character to corresponding number based on CHAR_TO_NUM mapping "encryption"
        pass
    
    def num_to_char(num):
        # Convert number to corresponding character based on CHAR_TO_NUM mapping "decryption"
        pass
    
    def encrypt_message(self, message, encoding_matrix):
        # Encrypt message using matrix multiplication (message_matrix * encoding_matrix = encrypted_matrix)
        pass
    
    def decrypt_message(self, encrypted_matrix, decoding_matrix):
        # Decrypt message using matrix multiplication (encrypted_matrix * decoding_matrix = original_message_matrix)
        pass