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

    const exportBtn = document.createElement('button');
    exportBtn.textContent = 'Exportar como JSON';
    exportBtn.className = 'btn-secondary';
    exportBtn.style.marginTop = '1rem';
    
    exportBtn.onclick = () => exportDeterminantAsJSON(
      payload.matrix,
      result.result
    );

    resultDiv.appendChild(exportBtn);

    showResult();

    const exportXMLBtn = document.createElement('button');
    exportXMLBtn.textContent = 'Exportar como XML';
    exportXMLBtn.className = 'btn-secondary';
    exportXMLBtn.style.marginTop = '0.5rem';

    exportXMLBtn.onclick = () => exportDeterminantAsXML(
      payload.matrix,
      result.result
    );

    resultDiv.appendChild(exportXMLBtn);

  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();

const json = prettyJson(matrixA, 4); 

function exportDeterminantAsJSON(matrix, determinant) {
  const json =
`{
  "operation": "determinant",
  "matrix": ${prettyJson(matrix, 4)},
  "result": ${determinant}
}`;

  const blob = new Blob([json], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'determinante.json';
  a.click();

  URL.revokeObjectURL(url);
} 

const xml = formatMatrixXML(matrix, tagName);

function exportDeterminantAsXML(matrix, determinant) {
  const xml =
`<?xml version="1.0" encoding="UTF-8"?>
<operation type="determinant">
  ${formatMatrixXML(matrix, 'matrix')}
  <result>${determinant}</result>
</operation>`;

  const blob = new Blob([xml], { type: 'application/xml' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'determinante.xml';
  a.click();

  URL.revokeObjectURL(url);
}
