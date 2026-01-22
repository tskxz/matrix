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
  hideCalculateButton();

  if(colsA !== rowsB) {
    showError('Error: As Colunas de A tem de ter a mesma quantidade das Linhas de B ( col_a = row_b )');
    return;
  }
  generateMatrixInput(rowsA, colsA, 'matrix-inputs', 'Matriz A', 'matrix-a');
  generateMatrixInput(rowsB, colsB, 'matrix-inputs', 'Matriz B', 'matrix-b');
  showCalculateButton();
});

form.addEventListener('submit', async function(e) {
  e.preventDefault();
  hideError();
  hideResult();
  showCalculateButton();

  const payload = {
    rows_a: parseInt(document.getElementById('rows-a').value),
    cols_a: parseInt(document.getElementById('cols-a').value),
    rows_b: parseInt(document.getElementById('rows-b').value),
    cols_b: parseInt(document.getElementById('cols-b').value),
    matrix_a: readMatrixValues('matrix-a'),
    matrix_b: readMatrixValues('matrix-b')
  };
  
  try {
    const result = await apiCall('/multiply', payload);
    displayMatrix(result.result, 'Resultado (A × B)');

    const exportBtn = document.createElement('button');
    exportBtn.textContent = 'Exportar como JSON';
    exportBtn.className = 'btn-secondary';
    exportBtn.style.marginTop = '1rem';
    
    exportBtn.onclick = () => exportMultiplyAsJSON(
      payload.matrix_a,
      payload.matrix_b,
      result.result
    );
    
    document.getElementById('result').appendChild(exportBtn);
  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();

const json = formatMatrix(matrixA, 4); 

function exportMultiplyAsJSON(matrixA, matrixB, resultMatrix) {
  const json =
`{
  "operation": "multiply",
  "matrixA": ${formatMatrix(matrixA, 4)},
  "matrixB": ${formatMatrix(matrixB, 4)},
  "result": ${formatMatrix(resultMatrix, 4)}
}`;

  const blob = new Blob([json], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'multiplicacao_matrizes.json';
  a.click();

  URL.revokeObjectURL(url);
}
