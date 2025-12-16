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


# class TestScalarMultiplication(unittest.TestCase):
#     """Test scalar multiplication."""
    
#     def test_scalar_multiply_by_2(self):
#         """Test multiplying matrix by scalar 2."""
#         A = Matrix(2, 2, [[1, 2], [3, 4]])
#         B = A.scalar_multiply(2)
        
#         expected = [[2, 4], [6, 8]]
#         self.assertEqual(B.to_list(), expected)
    
#     def test_scalar_multiply_by_0(self):
#         """Test multiplying matrix by 0."""
#         A = Matrix(2, 2, [[1, 2], [3, 4]])
#         B = A.scalar_multiply(0)
        
#         expected = [[0, 0], [0, 0]]
#         self.assertEqual(B.to_list(), expected)
    
#     def test_scalar_multiply_by_negative(self):
#         """Test multiplying matrix by negative scalar."""
#         A = Matrix(2, 2, [[1, 2], [3, 4]])
#         B = A.scalar_multiply(-1)
        
#         expected = [[-1, -2], [-3, -4]]
#         self.assertEqual(B.to_list(), expected)


# class TestMatrixMultiplication(unittest.TestCase):
#     """Test matrix multiplication."""
    
#     def test_multiply_2x2_matrices(self):
#         """Test multiplying two 2×2 matrices."""
#         A = Matrix(2, 2, [[1, 2], [3, 4]])
#         B = Matrix(2, 2, [[5, 6], [7, 8]])
#         C = A.multiply(B)
        
#         # (1×5 + 2×7), (1×6 + 2×8)
#         # (3×5 + 4×7), (3×6 + 4×8)
#         expected = [[19, 22], [43, 50]]
#         self.assertEqual(C.to_list(), expected)
    
#     def test_multiply_2x3_by_3x2(self):
#         """Test multiplying 2×3 by 3×2 matrices."""
#         A = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
#         B = Matrix(3, 2, [[7, 8], [9, 10], [11, 12]])
#         C = A.multiply(B)
        
#         self.assertEqual(C.dimensions(), (2, 2))
    
#     def test_multiply_incompatible_dimensions(self):
#         """Test that incompatible matrices raise error."""
#         A = Matrix(2, 2, [[1, 2], [3, 4]])
#         B = Matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        
#         with self.assertRaises(ValueError):
#             A.multiply(B)


# class TestDeterminant(unittest.TestCase):
#     """Test determinant calculation."""
    
#     def test_determinant_1x1(self):
#         """Test determinant of 1×1 matrix."""
#         A = Matrix(1, 1, [[5]])
#         self.assertEqual(A.determinant(), 5)
    
#     def test_determinant_2x2(self):
#         """Test determinant of 2×2 matrix."""
#         # det = 1×4 - 2×3 = 4 - 6 = -2
#         A = Matrix(2, 2, [[1, 2], [3, 4]])
#         self.assertEqual(A.determinant(), -2)
    
#     def test_determinant_identity_2x2(self):
#         """Test determinant of 2×2 identity matrix."""
#         A = Matrix(2, 2, [[1, 0], [0, 1]])
#         self.assertEqual(A.determinant(), 1)
    
#     def test_determinant_zero_determinant(self):
#         """Test determinant of singular matrix."""
#         # Rows are proportional, so det = 0
#         A = Matrix(2, 2, [[1, 2], [2, 4]])
#         self.assertEqual(A.determinant(), 0)
    
#     def test_determinant_non_square_matrix(self):
#         """Test that non-square matrix raises error."""
#         A = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        
#         with self.assertRaises(ValueError):
#             A.determinant()


# class TestMatrixInverse(unittest.TestCase):
#     """Test matrix inverse calculation."""
    
#     def test_inverse_2x2(self):
#         """Test inverse of 2×2 matrix."""
#         A = Matrix(2, 2, [[4, 7], [2, 6]])
#         A_inv = A.inverse()
        
#         # Multiply A × A_inv should give identity
#         I = A.multiply(A_inv)
#         identity = [[1, 0], [0, 1]]
        
#         for i in range(2):
#             for j in range(2):
#                 self.assertAlmostEqual(I.to_list()[i][j], identity[i][j], places=5)
    
#     def test_inverse_singular_matrix(self):
#         """Test that singular matrix raises error."""
#         A = Matrix(2, 2, [[1, 2], [2, 4]])  # Singular matrix
        
#         with self.assertRaises(ValueError):
#             A.inverse()
    
#     def test_inverse_non_square(self):
#         """Test that non-square matrix raises error."""
#         A = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        
#         with self.assertRaises(ValueError):
#             A.inverse()


# class TestMatrixDimensions(unittest.TestCase):
#     """Test dimension comparison."""
    
#     def test_same_dimensions(self):
#         """Test comparing matrices with same dimensions."""
#         A = Matrix(2, 3)
#         B = Matrix(2, 3)
#         self.assertTrue(A.is_same_dimension(B))
    
#     def test_different_rows(self):
#         """Test comparing matrices with different rows."""
#         A = Matrix(2, 3)
#         B = Matrix(3, 3)
#         self.assertFalse(A.is_same_dimension(B))
    
#     def test_different_columns(self):
#         """Test comparing matrices with different columns."""
#         A = Matrix(2, 3)
#         B = Matrix(2, 4)
#         self.assertFalse(A.is_same_dimension(B))


# if __name__ == '__main__':
#     unittest.main()