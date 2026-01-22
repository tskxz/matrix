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

    const exportBtn = document.createElement('button');
    exportBtn.textContent = 'Exportar como JSON';
    exportBtn.className = 'btn-secondary';
    exportBtn.style.marginTop = '1rem';
    
    exportBtn.onclick = () => exportTransposeAsJSON(
      payload.matrix,
      result.result
    );

    document.getElementById('result').appendChild(exportBtn);
  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();

const json = prettyJson(matrixA, 4); 

function exportTransposeAsJSON(matrix, transposedMatrix) {
  const json =
`{
  "operation": "transpose",
  "matrix": ${prettyJson(matrix, 4)},
  "result": ${prettyJson(transposedMatrix, 4)}
}`;

  const blob = new Blob([json], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'matriz_transposta.json';
  a.click();

  URL.revokeObjectURL(url);
}