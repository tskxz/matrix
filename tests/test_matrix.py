import unittest
from core.matrix import Matrix


class TestMatrixBasics(unittest.TestCase):
    
    def test_init_empty_matrix(self):
        m = Matrix(2, 3)
        self.assertEqual(m.rows, 2)
        self.assertEqual(m.cols, 3)
        self.assertEqual(m.to_list(), [[0, 0, 0], [0, 0, 0]])
    
    def test_init_with_data(self):
        data = [[1, 2], [3, 4]]
        m = Matrix(2, 2, data)
        self.assertEqual(m.to_list(), [[1, 2], [3, 4]])
    
    def test_init_wrong_dimensions(self):
        with self.assertRaises(ValueError):
            Matrix(2, 2, [[1, 2, 3], [4, 5, 6]])
    
    def test_is_square(self):
        m1 = Matrix(2, 2, [[1, 2], [3, 4]])
        m2 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        self.assertTrue(m1.is_square())
        self.assertFalse(m2.is_square())
    
    def test_dimensions(self):
        m = Matrix(3, 4)
        self.assertEqual(m.dimensions(), (3, 4))


class TestMatrixAddition(unittest.TestCase):
    
    def test_add_2x2(self):
        A = Matrix(2, 2, [[1, 2], [3, 4]])
        B = Matrix(2, 2, [[5, 6], [7, 8]])
        result = A.add(B)
        self.assertEqual(result.to_list(), [[6, 8], [10, 12]])
    
    def test_add_3x3(self):
        A = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        B = Matrix(3, 3, [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        result = A.add(B)
        self.assertEqual(result.to_list(), [[10, 10, 10], [10, 10, 10], [10, 10, 10]])
    
    def test_add_incompatible_dimensions(self):
        A = Matrix(2, 2, [[1, 2], [3, 4]])
        B = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            A.add(B)
    
    def test_add_wrong_type(self):
        A = Matrix(2, 2, [[1, 2], [3, 4]])
        with self.assertRaises(TypeError):
            A.add([[1, 2], [3, 4]])


class TestMatrixSubtraction(unittest.TestCase):
    
    def test_subtract_2x2(self):
        A = Matrix(2, 2, [[5, 6], [7, 8]])
        B = Matrix(2, 2, [[1, 2], [3, 4]])
        result = A.subtract(B)
        self.assertEqual(result.to_list(), [[4, 4], [4, 4]])
    
    def test_subtract_incompatible_dimensions(self):
        A = Matrix(2, 2, [[1, 2], [3, 4]])
        B = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
        with self.assertRaises(ValueError):
            A.subtract(B)


class TestMatrixScalarMultiply(unittest.TestCase):
    
    def test_scalar_multiply_2x2(self):
        A = Matrix(2, 2, [[1, 2], [3, 4]])
        result = A.scalar_multiply(3)
        self.assertEqual(result.to_list(), [[3, 6], [9, 12]])
    
    def test_scalar_multiply_zero(self):
        A = Matrix(2, 2, [[1, 2], [3, 4]])
        result = A.scalar_multiply(0)
        self.assertEqual(result.to_list(), [[0, 0], [0, 0]])


class TestMatrixMultiplication(unittest.TestCase):
    
    def test_multiply_2x2(self):
        A = Matrix(2, 2, [[1, 2], [3, 4]])
        B = Matrix(2, 2, [[5, 6], [7, 8]])
        result = A.multiply(B)
        self.assertEqual(result.to_list(), [[19, 22], [43, 50]])
    
    def test_multiply_2x3_3x2(self):
        A = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        B = Matrix(3, 2, [[7, 8], [9, 10], [11, 12]])
        result = A.multiply(B)
        self.assertEqual(result.to_list(), [[58, 64], [139, 154]])
    
    def test_multiply_incompatible_dimensions(self):
        A = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        B = Matrix(2, 2, [[1, 2], [3, 4]])
        with self.assertRaises(ValueError):
            A.multiply(B)


class TestMatrixTranspose(unittest.TestCase):
    
    def test_transpose_2x3(self):
        A = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        result = A.transpose()
        self.assertEqual(result.to_list(), [[1, 4], [2, 5], [3, 6]])
    
    def test_transpose_square(self):
        A = Matrix(2, 2, [[1, 2], [3, 4]])
        result = A.transpose()
        self.assertEqual(result.to_list(), [[1, 3], [2, 4]])


class TestMatrixDeterminant(unittest.TestCase):
    
    def test_determinant_1x1(self):
        A = Matrix(1, 1, [[5]])
        self.assertEqual(A.determinant(), 5)
    
    def test_determinant_2x2(self):
        A = Matrix(2, 2, [[1, 2], [3, 4]])
        self.assertEqual(A.determinant(), -2)
    
    def test_determinant_3x3(self):
        A = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(A.determinant(), 0)
    
    def test_determinant_3x3_nonzero(self):
        A = Matrix(3, 3, [[6, 1, 1], [4, -2, 5], [2, 8, 7]])
        self.assertEqual(A.determinant(), -306)
    
    def test_determinant_4x4(self):
        A = Matrix(4, 4, [
            [1, 0, 2, -1],
            [3, 0, 0, 5],
            [2, 1, 4, -3],
            [1, 0, 5, 0]
        ])
        self.assertEqual(A.determinant(), 30)
    
    def test_determinant_non_square(self):
        A = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            A.determinant()


class TestMatrixInverse(unittest.TestCase):
    
    def test_inverse_2x2(self):
        A = Matrix(2, 2, [[4, 7], [2, 6]])
        inv = A.inverse()
        expected = [[0.6, -0.7], [-0.2, 0.4]]
        result = inv.to_list()
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(result[i][j], expected[i][j], places=5)
    
    def test_inverse_3x3(self):
        A = Matrix(3, 3, [[1, 2, 3], [0, 1, 4], [5, 6, 0]])
        inv = A.inverse()
        identity = A.multiply(inv)
        result = identity.to_list()
        for i in range(3):
            for j in range(3):
                expected = 1 if i == j else 0
                self.assertAlmostEqual(result[i][j], expected, places=5)
    
    def test_inverse_singular_matrix(self):
        A = Matrix(2, 2, [[1, 2], [2, 4]])
        with self.assertRaises(ValueError):
            A.inverse()
    
    def test_inverse_non_square(self):
        A = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            A.inverse()


class TestMatrixEncryption(unittest.TestCase):
    
    def test_encrypt_decrypt_example(self):
        encoding_matrix = Matrix(2, 2, [[5, 7], [2, 3]])
        message = "OS NUMEROS GOVERNAM O MUNDO."
        
        encrypted = encoding_matrix.encrypt_message(message)
        
        self.assertIn('message_matrix', encrypted)
        self.assertIn('encrypted_matrix', encrypted)
        self.assertIn('numeric_sequence', encrypted)
        
        decrypted = encoding_matrix.decrypt_message(encrypted['encrypted_matrix'])
        
        original_upper = message.upper().replace(' ', '_')
        decrypted_text = decrypted['decrypted_message']
        decrypted_text = decrypted_text.rstrip('_')
        original_upper = original_upper.rstrip('_')
        
        self.assertEqual(decrypted_text, original_upper)
    
    def test_char_to_num(self):
        self.assertEqual(Matrix.char_to_num('A'), 1)
        self.assertEqual(Matrix.char_to_num('Z'), 26)
        self.assertEqual(Matrix.char_to_num('.'), 27)
        self.assertEqual(Matrix.char_to_num(' '), 29)
    
    def test_num_to_char(self):
        self.assertEqual(Matrix.num_to_char(1), 'A')
        self.assertEqual(Matrix.num_to_char(26), 'Z')
        self.assertEqual(Matrix.num_to_char(27), '.')
        self.assertEqual(Matrix.num_to_char(29), '_')


if __name__ == '__main__':
    unittest.main()