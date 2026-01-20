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
  
  try {
    const result = await apiCall('/encrypt', payload);
    displayMatrix(result.encrypted_matrix, 'Mensagem Encriptada');
  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();