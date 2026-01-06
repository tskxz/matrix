import unittest
from core.matrix import Matrix


class TestMatrixCreation(unittest.TestCase):
    """Test matrix initialization and basic operations."""
    
    def test_create_matrix_with_data(self):
        """Test creating a matrix with initial data."""
        data = [[1, 2], [3, 4]]
        m = Matrix(2, 2, data)
        self.assertEqual(m.rows, 2)
        self.assertEqual(m.cols, 2)
        self.assertEqual(m.data, data)
        print(f"Created matrix: {m}")
    
    def test_create_matrix_zeros(self):
        """Test creating a matrix initialized with zeros."""
        m = Matrix(3, 3)
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(m.data, expected)
        print(f"Zero matrix created correctly")
    
    def test_invalid_dimensions(self):
        """Test that wrong data dimensions raise error."""
        with self.assertRaises(ValueError):
            Matrix(2, 2, [[1, 2, 3], [4, 5, 6]])
        print(f"Invalid dimensions error raised correctly")


class TestMatrixElements(unittest.TestCase):
    """Test getting and setting matrix elements."""
    
    def setUp(self):
        """Create a test matrix before each test."""
        self.matrix = Matrix(2, 2, [[1, 2], [3, 4]])
    
    def test_get_element(self):
        """Test getting elements from matrix (1-indexed)."""
        self.assertEqual(self.matrix.get_element(1, 1), 1)
        self.assertEqual(self.matrix.get_element(1, 2), 2)
        self.assertEqual(self.matrix.get_element(2, 1), 3)
        self.assertEqual(self.matrix.get_element(2, 2), 4)
        print(f"All elements retrieved correctly")
    
    def test_set_element(self):
        """Test setting elements in matrix."""
        self.matrix.set_element(1, 1, 10)
        self.assertEqual(self.matrix.get_element(1, 1), 10)
        print(f"Element set correctly: {self.matrix}")
    
    def test_dimensions(self):
        """Test getting matrix dimensions."""
        dims = self.matrix.dimensions()
        self.assertEqual(dims, (2, 2))
        print(f"Dimensions correct: {dims}")
    
    def test_to_list(self):
        """Test converting matrix to list."""
        result = self.matrix.to_list()
        expected = [[1, 2], [3, 4]]
        self.assertEqual(result, expected)
    
    def test_is_square(self):
        """Test checking if matrix is square."""
        self.assertTrue(self.matrix.is_square())
        non_square = Matrix(2, 3)
        self.assertFalse(non_square.is_square())


class TestMatrixAddition(unittest.TestCase):
    """Test matrix addition."""
    
    def test_add_2x2_matrices(self):
        """Test adding two 2×2 matrices."""
        A = Matrix(2, 2, [[1, 2], 
                          [3, 4]])

        B = Matrix(2, 2, [[5, 6], 
                          [7, 8]])

        result = A.add(B)
        expected = [[6, 8], [10, 12]]
        self.assertEqual(result['data'], expected)
        print(f"Addition result: {result['data']}")

    def test_add_with_negatives(self):
        """Test addition with negative numbers."""
        A = Matrix(2, 2, [[1, -2],
                          [-3, 4]])

        B = Matrix(2, 2, [[-1, 2],
                          [3, -4]])
        result = A.add(B)

        expected = [[0, 0],
                    [0, 0]]
        self.assertEqual(result['data'], expected)
        print(f"Addition with negatives result: {result['data']}")

    def test_add_incompatible_dimensions(self):
        """Test that adding incompatible matrices raises error."""
        A = Matrix(2, 2, [[1, 2],
                          [3, 4]])

        B = Matrix(3, 3, [[1, 2, 3], 
                          [4, 5, 6], 
                          [7, 8, 9]])
        
        with self.assertRaises(ValueError):
            A.add(B)
        print(f"Incompatible dimensions error raised correctly")


class TestMatrixSubtraction(unittest.TestCase):
    """Test matrix subtraction."""
    
    def test_subtract_2x2_matrices(self):
        """Test subtracting two 2×2 matrices."""
        A = Matrix(2, 2, [[5, 6], 
                          [7, 8]])

        B = Matrix(2, 2, [[1, 2], 
                          [3, 4]])
        result = A.subtract(B)
        expected = [[4, 4], [4, 4]]
        self.assertEqual(result['data'], expected)
        print(f"Subtraction result: {result['data']}")

    def test_subtract_same_matrix(self):
        """Test subtracting a matrix from itself gives zeros."""
        A = Matrix(2, 2, [[1, 2], [3, 4]])
        result = A.subtract(A)
        expected = [[0, 0], [0, 0]]
        self.assertEqual(result['data'], expected)
        print(f"Self-subtraction result: {result['data']}")
    
    def test_subtract_incompatible_dimensions(self):
        """Test that subtracting incompatible matrices raises error."""
        A = Matrix(2, 2, [[1, 2], 
                          [3, 4]])

        B = Matrix(3, 3, [[1, 2, 3], 
                          [4, 5, 6], 
                          [7, 8, 9]])
        
        with self.assertRaises(ValueError):
            A.subtract(B)
        print(f"Incompatible dimensions error raised correctly")


class TestScalarMultiplication(unittest.TestCase):
    """Test scalar multiplication."""
    
    def test_scalar_multiply_by_2(self):
        """Test multiplying matrix by scalar 2."""
        A = Matrix(2, 2, [[1, 2],
                          [3, 4]])
        result = A.scalar_multiply(2)
        expected = [[2, 4], 
                    [6, 8]]
        self.assertEqual(result['data'], expected)
        print(f"Scalar multiply by 2 result: {result['data']}")

    def test_scalar_multiply_by_0(self):
        """Test multiplying matrix by 0."""
        A = Matrix(2, 2, [[1, 2], 
                          [3, 4]])
        result = A.scalar_multiply(0)
        expected = [[0, 0], 
                    [0, 0]]
        self.assertEqual(result['data'], expected)
    
    def test_scalar_multiply_by_negative(self):
        """Test multiplying matrix by negative scalar."""
        A = Matrix(2, 2, [[1, 2], 
                          [3, 4]])
        result = A.scalar_multiply(-1)
        expected = [[-1, -2], 
                    [-3, -4]]
        self.assertEqual(result['data'], expected)
        print(f"Scalar multiply by negative result: {result['data']}")


class TestMatrixMultiplication(unittest.TestCase):
    """Test matrix multiplication."""
    
    def test_multiply_2x2_matrices(self):
        """Test multiplying two 2×2 matrices."""
        A = Matrix(2, 2, [[1, 2], 
                          [3, 4]])
        B = Matrix(2, 2, [[5, 6], 
                          [7, 8]])
        C = A.multiply(B)
        expected = [[19, 22], [43, 50]]
        self.assertEqual(C.to_list(), expected)
    
    def test_multiply_2x3_by_3x2(self):
        """Test multiplying 2×3 by 3×2 matrices."""
        A = Matrix(2, 3, [[1, 2, 3], 
                          [4, 5, 6]])
        B = Matrix(3, 2, [[7, 8], 
                          [9, 10], 
                          [11, 12]])
        C = A.multiply(B)
        self.assertEqual(C.dimensions(), (2, 2))
    
    def test_multiply_incompatible_dimensions(self):
        """Test that incompatible matrices raise error."""
        A = Matrix(2, 2, [[1, 2], 
                          [3, 4]])
        B = Matrix(3, 3, [[1, 2, 3], 
                          [4, 5, 6], 
                          [7, 8, 9]])
        with self.assertRaises(ValueError):
            A.multiply(B)


class TestDeterminant(unittest.TestCase):
    """Test determinant calculation."""
    
    def test_determinant_1x1(self):
        """Test determinant of 1×1 matrix."""
        A = Matrix(1, 1, [[5]])
        self.assertEqual(A.determinant(), 5)
    
    def test_determinant_2x2(self):
        """Test determinant of 2×2 matrix."""
        A = Matrix(2, 2, [[1, 2], 
                          [3, 4]])
        self.assertEqual(A.determinant(), -2)
    
    def test_determinant_3x3(self):
        """Test determinant of 3×3 matrix."""
        A = Matrix(3, 3, [[1, 2, 3], 
                          [0, 1, 4], 
                          [5, 6, 0]])
        self.assertEqual(A.determinant(), 1)
    
    def test_determinant_identity_2x2(self):
        """Test determinant of 2×2 identity matrix."""
        A = Matrix(2, 2, [[1, 0], 
                          [0, 1]])
        self.assertEqual(A.determinant(), 1)
    
    def test_determinant_zero_determinant(self):
        """Test determinant of singular matrix."""
        A = Matrix(2, 2, [[1, 2], 
                          [2, 4]])
        self.assertEqual(A.determinant(), 0)
    
    def test_determinant_non_square_matrix(self):
        """Test that non-square matrix raises error."""
        A = Matrix(2, 3, [[1, 2, 3], 
                          [4, 5, 6]])
        with self.assertRaises(ValueError):
            A.determinant()


class TestMatrixTranspose(unittest.TestCase):
    """Test matrix transpose."""
    
    def test_transpose_2x2(self):
        """Test transpose of 2×2 matrix."""
        A = Matrix(2, 2, [[1, 2], 
                          [3, 4]])
        A_T = A.transpose()
        expected = [[1, 3], 
                    [2, 4]]
        self.assertEqual(A_T.to_list(), expected)
    
    def test_transpose_2x3(self):
        """Test transpose of 2×3 matrix."""
        A = Matrix(2, 3, [[1, 2, 3], 
                          [4, 5, 6]])
        A_T = A.transpose()
        self.assertEqual(A_T.dimensions(), (3, 2))
        expected = [[1, 4], 
                    [2, 5], 
                    [3, 6]]
        self.assertEqual(A_T.to_list(), expected)


class TestMatrixInverse(unittest.TestCase):
    """Test matrix inverse calculation."""
    
    def test_inverse_2x2(self):
        """Test inverse of 2×2 matrix."""
        A = Matrix(2, 2, [[4, 7], 
                          [2, 6]])
        A_inv = A.inverse()
        I = A.multiply(A_inv)
        identity = [[1, 0], 
                    [0, 1]]
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(I.to_list()[i][j], identity[i][j], places=5)
    
    def test_inverse_singular_matrix(self):
        """Test that singular matrix raises error."""
        A = Matrix(2, 2, [[1, 2], 
                          [2, 4]])
        with self.assertRaises(ValueError):
            A.inverse()
    
    def test_inverse_non_square(self):
        """Test that non-square matrix raises error."""
        A = Matrix(2, 3, [[1, 2, 3], 
                          [4, 5, 6]])
        with self.assertRaises(ValueError):
            A.inverse()


class TestMatrixIdentity(unittest.TestCase):
    """Test identity matrix creation."""
    
    def test_identity_3x3(self):
        """Test creating 3×3 identity matrix."""
        A = Matrix(3, 3)
        I = A.identity(3)
        expected = [[1, 0, 0], 
                    [0, 1, 0], 
                    [0, 0, 1]]
        self.assertEqual(I.to_list(), expected)


class TestMatrixDimensions(unittest.TestCase):
    """Test dimension comparison."""
    
    def test_same_dimensions(self):
        """Test comparing matrices with same dimensions."""
        A = Matrix(2, 3)
        B = Matrix(2, 3)
        self.assertTrue(A.is_same_dimension(B))
    
    def test_different_rows(self):
        """Test comparing matrices with different rows."""
        A = Matrix(2, 3)
        B = Matrix(3, 3)
        self.assertFalse(A.is_same_dimension(B))
    
    def test_different_columns(self):
        """Test comparing matrices with different columns."""
        A = Matrix(2, 3)
        B = Matrix(2, 4)
        self.assertFalse(A.is_same_dimension(B))


class TestMatrixEncryption(unittest.TestCase):
    """Test matrix encryption and decryption."""
    
    def setUp(self):
        """Set up encoding and decoding matrices."""
        self.encoding_matrix = Matrix(2, 2, [[5, 7], [2, 3]])
        self.decoding_matrix = Matrix(2, 2, [[3, -7], [-2, 5]])
    
    def test_encrypt_decrypt_example_message(self):
        """Test encrypting and decrypting the example message."""
        message = "OS NÚMEROS GOVERNAM O MUNDO."
        
        result = self.encoding_matrix.encrypt_message(message, self.encoding_matrix)
        encrypted = result['encrypted_matrix']
        
        decrypted_result = self.encoding_matrix.decrypt_message(encrypted, self.decoding_matrix)
        decrypted_message = decrypted_result['decrypted_message']
        
        self.assertEqual(decrypted_message, message)
    
    def test_encrypt_message_structure(self):
        """Test that encryption returns expected structure."""
        message = "HELLO"
        result = self.encoding_matrix.encrypt_message(message, self.encoding_matrix)
        
        self.assertIn('encrypted_matrix', result)
        self.assertIn('message_matrix', result)
        self.assertIn('numeric_sequence', result)
        self.assertIn('original_message', result)
    
    def test_encrypt_short_message(self):
        """Test encrypting a short message."""
        message = "HI"
        result = self.encoding_matrix.encrypt_message(message, self.encoding_matrix)
        
        self.assertIsInstance(result['encrypted_matrix'], Matrix)
    
    def test_encrypt_with_padding(self):
        """Test that odd-length messages get padded correctly."""
        message = "HELLO"
        result = self.encoding_matrix.encrypt_message(message, self.encoding_matrix)
        
        self.assertEqual(len(result['numeric_sequence']), 6)
    
    def test_decrypt_returns_original(self):
        """Test that decrypt returns original message."""
        message = "TEST MESSAGE"
        
        encrypted = self.encoding_matrix.encrypt_message(message, self.encoding_matrix)
        decrypted = self.encoding_matrix.decrypt_message(
            encrypted['encrypted_matrix'],
            self.decoding_matrix
        )
        
        self.assertEqual(decrypted['decrypted_message'], message)
    
    def test_encryption_with_special_chars(self):
        """Test encryption with special characters."""
        message = "HELLO WORLD."
        
        result = self.encoding_matrix.encrypt_message(message, self.encoding_matrix)
        decrypted = self.encoding_matrix.decrypt_message(
            result['encrypted_matrix'],
            self.decoding_matrix
        )
        
        self.assertEqual(decrypted['decrypted_message'], message)
    
    def test_verify_encoding_decoding_matrices(self):
        """Test that encoding and decoding matrices are inverses."""
        identity = self.encoding_matrix.multiply(self.decoding_matrix)
        
        self.assertAlmostEqual(identity.get_element(1, 1), 1, places=5)
        self.assertAlmostEqual(identity.get_element(1, 2), 0, places=5)
        self.assertAlmostEqual(identity.get_element(2, 1), 0, places=5)
        self.assertAlmostEqual(identity.get_element(2, 2), 1, places=5)


if __name__ == '__main__':
    unittest.main()