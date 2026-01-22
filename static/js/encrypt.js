const form = document.getElementById('encrypt-form');
const generateBtn = document.getElementById('generate-btn');

generateBtn.addEventListener('click', function() {
  const size = parseInt(document.getElementById('size').value);
  
  clearMatrixInputs();
  hideError();
  hideResult();
  
  generateMatrixInput(size, size, 'matrix-inputs', 'Matriz de Codificação', 'encoding-matrix');
});

form.addEventListener('submit', async function(e) {
  e.preventDefault();
  hideError();
  hideResult();
  
  const payload = {
    size: parseInt(document.getElementById('size').value),
    encoding_matrix: readMatrixValues('encoding-matrix'),
    message: document.getElementById('message').value
  };

  const payload_determinant = {
    size: parseInt(document.getElementById('size').value),
    matrix: readMatrixValues('encoding-matrix')
  };
  
  try {
    const detResult = await apiCall('/determinant', payload_determinant);
    if (detResult.result === 0) {
      showError('A matriz de codificação deve ser invertível (det ≠ 0).');
      return;
    }
    const result = await apiCall('/encrypt', payload);
    displayMatrix(result.encrypted_matrix, 'Mensagem Encriptada');
    
    const exportBtn = document.createElement('button');
      exportBtn.textContent = 'Exportar como JSON';
      exportBtn.className = 'btn-secondary';
      exportBtn.style.marginTop = '1rem';

      exportBtn.onclick = () => exportEncryptAsJSON(
       payload.message,
       payload.encoding_matrix,
       result.encrypted_matrix
   );
       document.getElementById('result').appendChild(exportBtn);
  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();

function formatMatrix(matrix, indent = 2) {
  const space = ' '.repeat(indent);
  return '[\n' +
    matrix
      .map(row => `${space}[${row.join(', ')}]`)
      .join(',\n') +
    '\n]';
}

function exportEncryptAsJSON(message, encodingMatrix, encryptedMatrix) {
  const json =
`{
  "operation": "encrypt",
  "message": "${message}",
  "encodingMatrix": ${formatMatrix(encodingMatrix, 4)},
  "encryptedMatrix": ${formatMatrix(encryptedMatrix, 4)}
}`;

  const blob = new Blob([json], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'encriptacao.json';
  a.click();

  URL.revokeObjectURL(url);
}