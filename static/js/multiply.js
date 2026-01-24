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

    const exportXMLBtn = document.createElement('button');
    exportXMLBtn.textContent = 'Exportar como XML';
    exportXMLBtn.className = 'btn-secondary';
    exportXMLBtn.style.marginTop = '0.5rem';

    exportXMLBtn.onclick = () => exportMultiplyAsXML(
      payload.matrix_a,
      payload.matrix_b,
      result.result
);

document.getElementById('result').appendChild(exportXMLBtn);

    const exportHTMLBtn = document.createElement('button');
    exportHTMLBtn.textContent = 'Exportar como HTML';
    exportHTMLBtn.className = 'btn-secondary';
    exportHTMLBtn.style.marginTop = '0.5rem';

    exportHTMLBtn.onclick = () => exportMultiplyAsHTML(
      payload.matrix_a,
      payload.matrix_b,
      result.result
);

document.getElementById('result').appendChild(exportHTMLBtn);

  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();

const json = prettyJson(matrixA, 4); 

function exportMultiplyAsJSON(matrixA, matrixB, resultMatrix) {
  const json =
`{
  "operation": "multiply",
  "matrixA": ${prettyJson(matrixA, 4)},
  "matrixB": ${prettyJson(matrixB, 4)},
  "result": ${prettyJson(resultMatrix, 4)}
}`;

  const blob = new Blob([json], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'multiplicacao_matrizes.json';
  a.click();

  URL.revokeObjectURL(url);
}

const xml = prettyXML(matrix, tagName);

function exportMultiplyAsXML(matrixA, matrixB, resultMatrix) {
  const xml =
`<?xml version="1.0" encoding="UTF-8"?>
<operation type="multiply">
${prettyXML(matrixA, 'matrixA')}
${prettyXML(matrixB, 'matrixB')}
${prettyXML(resultMatrix, 'result')}
</operation>`;

  const blob = new Blob([xml], { type: 'application/xml' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'multiplicacao_matrizes.xml';
  a.click();

  URL.revokeObjectURL(url);
}

function exportMultiplyAsHTML(matrixA, matrixB, resultMatrix) {
  const html =
`<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <title>Multiplicação de Matrizes</title>
</head>
<body>
  <h1>Operação: Multiplicação de Matrizes (A × B)</h1>

  ${prettyHTML(matrixA, 'Matriz A')}
  ${prettyHTML(matrixB, 'Matriz B')}
  ${prettyHTML(resultMatrix, 'Resultado')}
</body>
</html>`;

  const blob = new Blob([html], { type: 'text/html' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'multiplicacao_matrizes.html';
  a.click();

  URL.revokeObjectURL(url);
}
