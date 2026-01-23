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
    matrix: readMatrixValues('matrix-a'),
    scalar: parseFloat(document.getElementById('scalar').value)
  };
  
  try {
    const result = await apiCall('/scalar', payload);
    displayMatrix(result.result, `Resultado (${payload.scalar} × Matriz)`);
    
    const exportBtn = document.createElement('button');
    exportBtn.textContent = 'Exportar como JSON';
    exportBtn.className = 'btn-secondary';
    exportBtn.style.marginTop = '1rem';
    
    exportBtn.onclick = () => exportScalarAsJSON(
      payload.scalar,
      payload.matrix,
      result.result
    );
    
    document.getElementById('result').appendChild(exportBtn);

    const exportXMLBtn = document.createElement('button');
    exportXMLBtn.textContent = 'Exportar como XML';
    exportXMLBtn.className = 'btn-secondary';
    exportXMLBtn.style.marginTop = '0.5rem';


    exportXMLBtn.onclick = () => exportScalarAsXML(
      payload.scalar,
      payload.matrix,
      result.result
);

document.getElementById('result').appendChild(exportXMLBtn);

  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();

const json = prettyJson(matrixA, 4); 

function exportScalarAsJSON(scalar, matrix, resultMatrix) {
  const json =
`{
  "operation": "scalar",
  "scalar": ${scalar},
  "matrix": ${prettyJson(matrix, 4)},
  "result": ${prettyJson(resultMatrix, 4)}
}`;
  
  const blob = new Blob([json], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  
  const a = document.createElement('a');
  a.href = url;
  a.download = 'scalar_multiplication.json';
  a.click();
  
  URL.revokeObjectURL(url);
}

const xml = formatMatrixXML(matrix, tagName);

function exportScalarAsXML(scalar, matrix, resultMatrix) {
  const xml =
`<?xml version="1.0" encoding="UTF-8"?>
<operation type="scalar">
  <scalar>${scalar}</scalar>
${formatMatrixXML(matrix, 'matrix')}
${formatMatrixXML(resultMatrix, 'result')}
</operation>`;

  const blob = new Blob([xml], { type: 'application/xml' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'scalar_multiplication.xml';
  a.click();

  URL.revokeObjectURL(url);
}