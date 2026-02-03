# Matrix

Matrix is a web-based matrix calculator built with Flask. It provides a user-friendly interface to perform a wide range of matrix operations, from basic arithmetic to advanced applications like message encryption and decryption.

## Features

- **Basic Arithmetic:** Addition, subtraction, and multiplication of matrices.
- **Scalar Operations:** Multiply a matrix by a scalar value.
- **Advanced Calculations:**
    - Matrix Transpose
    - Determinant (for square matrices of any size via Laplace expansion)
    - Matrix Inverse (using the adjugate method)
- **Cryptography:**
    - Encrypt text messages using an invertible encoding matrix (a form of Hill Cipher).
    - Decrypt messages using the inverse of the encoding matrix.
- **Dynamic UI:** The interface dynamically generates input fields based on user-specified matrix dimensions.
- **Data Export:** Export the results of operations (including the input matrices) to JSON, XML, or HTML formats.
- **Error Handling:** Validates matrix dimensions and mathematical conditions (e.g., non-singular matrices for inversion) and provides clear error messages.

## Technology Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Math Engine:** Custom `Matrix` class with core logic in Python.
- **Testing:** Pytest
- **CI/CD:** GitHub Actions

## Installation and Usage

To get a local copy up and running, follow these steps.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/tskxz/matrix.git
    cd matrix
    ```

2.  **Create and activate a virtual environment:**
    - On macOS/Linux:
      ```sh
      python3 -m venv venv
      source venv/bin/activate
      ```
    - On Windows:
      ```sh
      python -m venv venv
      .\venv\Scripts\activate
      ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```sh
    python app.py
    ```

5.  Open your browser and navigate to `http://127.0.0.1:5000`.

## Running Tests

The project includes a suite of unit tests to ensure the correctness of the matrix operations. To run the tests:

```sh
python -m pytest tests/ -v -s
```

## Project Structure

The repository is organized as follows:

```
├── app.py                  # Main Flask application with all routes
├── core/
│   └── matrix.py           # Core Matrix class with all mathematical logic
├── static/
│   ├── css/                # CSS stylesheets
│   └── js/                 # Frontend JavaScript for each operation
├── templates/              # HTML templates for the web interface
├── tests/
│   ├── test_matrix.py      # Unit tests for the Matrix class
│   └── test_routes.py      # Unit tests for the Flask routes
├── docs/                   # System analysis, diagrams, and documentation
├── requirements.txt        # Python dependencies
└── .github/                # CI workflows and PR templates
```

## Cryptography Implementation

The application uses matrix multiplication for encryption and decryption, a method similar to the Hill Cipher.

1.  **Character Mapping:** Each character in the message is converted to a number based on a predefined map (`A=1, B=2, ..., ' '=29`).
2.  **Message Matrix:** The resulting sequence of numbers is organized into a matrix (`M`). The number of rows of this matrix matches the dimensions of the encoding matrix.
3.  **Encryption:** The message matrix `M` is multiplied by a user-provided, invertible *encoding matrix* `A` to produce the *encrypted matrix* `N`.
    - `N = A * M`
4.  **Decryption:** To recover the original message, the encrypted matrix `N` is multiplied by the inverse of the encoding matrix, `A⁻¹`.
    - `M = A⁻¹ * N`
5.  **Conversion to Text:** The numbers in the resulting matrix `M` are converted back to characters to reveal the original message.

An encoding matrix must be invertible (i.e., its determinant must be non-zero) for decryption to be possible. The application validates this condition before performing any encryption.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
