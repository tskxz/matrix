const form = document.getElementById('encrypt-form');
const generateBtn = document.getElementById('generate-btn');

generateBtn.addEventListener('click', function() {
  const size = parseInt(document.getElementById('size').value);
  
  clearMatrixInputs();
  hideError();
  hideResult();
  
  generateMatrixInput(size, size, 'matrix-inputs', 'Matriz de Codificação', 'encoding-matrix');
});

form.addEventListener('submit', async function(e) {
  e.preventDefault();
  hideError();
  hideResult();
  
  const payload = {
    size: parseInt(document.getElementById('size').value),
    encoding_matrix: readMatrixValues('encoding-matrix'),
    message: document.getElementById('message').value
  };

  const payload_determinant = {
    size: parseInt(document.getElementById('size').value),
    matrix: readMatrixValues('encoding-matrix')
  };
  
  try {
    const detResult = await apiCall('/determinant', payload_determinant);
    if (detResult.result === 0) {
      showError('A matriz de codificação deve ser invertível (det ≠ 0).');
      return;
    }
    const result = await apiCall('/encrypt', payload);
    displayMatrix(result.encrypted_matrix, 'Mensagem Encriptada');
  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();