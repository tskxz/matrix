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

    const exportHTMLBtn = document.createElement('button');
    exportHTMLBtn.textContent = 'Exportar como HTML';
    exportHTMLBtn.className = 'btn-secondary';
    exportHTMLBtn.style.marginTop = '0.5rem';

    exportHTMLBtn.onclick = () => exportDeterminantAsHTML(
      payload.matrix,
      result.result
);

    document.getElementById('result').appendChild(exportHTMLBtn);

  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();

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

function exportDeterminantAsXML(matrix, determinant) {
  const xml =
`<?xml version="1.0" encoding="UTF-8"?>
<operation type="determinant">
  ${prettyXML(matrix, 'matrix')}
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

function exportDeterminantAsHTML(matrix, determinant) {
  const html =
`<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <title>Determinante</title>
</head>
<body>
  <h1>Operação: Determinante</h1>

  ${prettyHTML(matrix, 'Matriz')}
  
  <h2>Resultado</h2>
  <p style="font-size:1.5rem; font-family: monospace;">${determinant}</p>
</body>
</html>`;

  const blob = new Blob([html], { type: 'text/html' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'determinante.html';
  a.click();

  URL.revokeObjectURL(url);
}
