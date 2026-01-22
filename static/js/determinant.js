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
  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();

const json = formatMatrix(matrixA, 4); 

function exportDeterminantAsJSON(matrix, determinant) {
  const json =
`{
  "operation": "determinant",
  "matrix": ${formatMatrix(matrix, 4)},
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