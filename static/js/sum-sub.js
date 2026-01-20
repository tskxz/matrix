const form = document.getElementById('matrix-form');
const generateBtn = document.getElementById('generate-btn');

generateBtn.addEventListener('click', function() {
  const rows = parseInt(document.getElementById('rows').value);
  const cols = parseInt(document.getElementById('cols').value);
  
  clearMatrixInputs();
  hideError();
  hideResult();
  
  generateMatrixInput(rows, cols, 'matrix-inputs', 'Matriz A', 'matrix-a');
  generateMatrixInput(rows, cols, 'matrix-inputs', 'Matriz B', 'matrix-b');
});

form.addEventListener('submit', async function(e) {
  e.preventDefault();
  hideError();
  hideResult();
  
  const payload = {
    rows: parseInt(document.getElementById('rows').value),
    cols: parseInt(document.getElementById('cols').value),
    matrix_a: readMatrixValues('matrix-a'),
    matrix_b: readMatrixValues('matrix-b'),
    operation: document.getElementById('operation').value
  };
  
  try {
    const result = await apiCall('/sum-sub', payload);
    const title = payload.operation === 'add' ? 'Resultado (A + B)' : 'Resultado (A - B)';
    displayMatrix(result.result, title);
  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();