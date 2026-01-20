const form = document.getElementById('matrix-form');
const generateBtn = document.getElementById('generate-btn');

generateBtn.addEventListener('click', function() {
  const size = parseInt(document.getElementById('size').value);
  
  clearMatrixInputs();
  hideError();
  hideResult();
  
  generateMatrixInput(size, size, 'matrix-inputs', 'Matriz', 'matrix-a');
});

form.addEventListener('submit', async function(e) {
  e.preventDefault();
  hideError();
  hideResult();
  
  const size = parseInt(document.getElementById('size').value);
  
  const payload = {
    size: size,
    matrix: readMatrixValues('matrix-a')
  };
  
  try {
    const result = await apiCall('/determinant', payload);
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `<h3>Determinante</h3><p style="font-size: 1.5rem; text-align: center; font-family: monospace;">${result.result}</p>`;
    showResult();
  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();