const form = document.getElementById('matrix-form');
const generateBtn = document.getElementById('generate-btn');

generateBtn.addEventListener('click', function() {
  const rows = parseInt(document.getElementById('rows').value);
  const cols = parseInt(document.getElementById('cols').value);
  
  clearMatrixInputs();
  hideError();
  hideResult();
  
  generateMatrixInput(rows, cols, 'matrix-inputs', 'Matriz', 'matrix-a');
});

form.addEventListener('submit', async function(e) {
  e.preventDefault();
  hideError();
  hideResult();
  
  const payload = {
    rows: parseInt(document.getElementById('rows').value),
    cols: parseInt(document.getElementById('cols').value),
    matrix: readMatrixValues('matrix-a')
  };
  
  try {
    const result = await apiCall('/transpose', payload);
    displayMatrix(result.result, 'Matriz Transposta');
  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();