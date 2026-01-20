const form = document.getElementById('matrix-form');
const generateBtn = document.getElementById('generate-btn');

generateBtn.addEventListener('click', function() {
  const rowsA = parseInt(document.getElementById('rows-a').value);
  const colsA = parseInt(document.getElementById('cols-a').value);
  const rowsB = parseInt(document.getElementById('rows-b').value);
  const colsB = parseInt(document.getElementById('cols-b').value);
  
  clearMatrixInputs();
  hideError();
  hideResult();
  
  generateMatrixInput(rowsA, colsA, 'matrix-inputs', 'Matriz A', 'matrix-a');
  generateMatrixInput(rowsB, colsB, 'matrix-inputs', 'Matriz B', 'matrix-b');
});

form.addEventListener('submit', async function(e) {
  e.preventDefault();
  hideError();
  hideResult();
  
  const payload = {
    rows: parseInt(document.getElementById('rows-a').value),
    cols: parseInt(document.getElementById('cols-a').value),
    matrix_a: readMatrixValues('matrix-a'),
    matrix_b: readMatrixValues('matrix-b')
  };
  
  try {
    const result = await apiCall('/multiply', payload);
    displayMatrix(result.result, 'Resultado (A × B)');
  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();