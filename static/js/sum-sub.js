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

    const exportBtn = document.createElement('button');
    exportBtn.textContent = 'Exportar como JSON';
    exportBtn.className = 'btn-secondary';
    exportBtn.style.marginTop = '1rem';

    exportBtn.onclick = () => exportAsJSON(
      payload.matrix_a,
      payload.matrix_b,
      result.result,
      payload.operation
    );

    document.getElementById('result').appendChild(exportBtn);

    const exportXMLBtn = document.createElement('button');
          exportXMLBtn.textContent = 'Exportar como XML';
          exportXMLBtn.className = 'btn-secondary';
          exportXMLBtn.style.marginTop = '0.5rem';

          exportXMLBtn.onclick = () => exportAsXML(
          payload.matrix_a,
          payload.matrix_b,
          result.result,
          payload.operation
);

document.getElementById('result').appendChild(exportXMLBtn);

  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();

const json = formatMatrix(matrixA, 4); 

function exportAsJSON(matrixA, matrixB, matrixResult, operation) {
  const json =
`{
  "operation": "${operation}",
  "matrixA": ${formatMatrix(matrixA, 4)},
  "matrixB": ${formatMatrix(matrixB, 4)},
  "result": ${formatMatrix(matrixResult, 4)}
}`;
  
  const blob = new Blob([json], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  
  const a = document.createElement('a');
  a.href = url;
  a.download = 'matrizes.json';
  a.click();
  
  URL.revokeObjectURL(url);
}

const xml = formatMatrixXML(matrix, tagName);

function exportAsXML(matrixA, matrixB, matrixResult, operation) {
  const xml =
  `<?xml version="1.0" encoding="UTF-8"?>
  <operation type="${operation}">
  ${formatMatrixXML(matrixA, 'matrixA')}
  ${formatMatrixXML(matrixB, 'matrixB')}
  ${formatMatrixXML(matrixResult, 'result')}
  </operation>`;

  const blob = new Blob([xml], { type: 'application/xml' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'matrizes.xml';
  a.click();

  URL.revokeObjectURL(url);
}