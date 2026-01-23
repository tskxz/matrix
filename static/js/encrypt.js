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

    const exportXMLBtn = document.createElement('button');
    exportXMLBtn.textContent = 'Exportar como XML';
    exportXMLBtn.className = 'btn-secondary';
    exportXMLBtn.style.marginTop = '0.5rem';

    exportXMLBtn.onclick = () => exportEncryptAsXML(
      payload.message,
      payload.encoding_matrix,
      result.encrypted_matrix
    );

    document.getElementById('result').appendChild(exportXMLBtn);

  } catch (error) {
    showError(error.message);
  }
});

generateBtn.click();

const json = prettyJson(matrixA, 4); 

function exportEncryptAsJSON(message, encodingMatrix, encryptedMatrix) {
  const json =
`{
  "operation": "encrypt",
  "message": "${message}",
  "encodingMatrix": ${prettyJson(encodingMatrix, 4)},
  "encryptedMatrix": ${prettyJson(encryptedMatrix, 4)}
}`;

  const blob = new Blob([json], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'encriptacao.json';
  a.click();

  URL.revokeObjectURL(url);
}

const xml = prettyXML(matrix, tagName);

function exportEncryptAsXML(message, encodingMatrix, encryptedMatrix) {
  const xml =
`<?xml version="1.0" encoding="UTF-8"?>
<operation type="encrypt">
  <message>${message}</message>
  ${prettyXML(encodingMatrix, 'encodingMatrix')}
  ${prettyXML(encryptedMatrix, 'encryptedMatrix')}
</operation>`;

  const blob = new Blob([xml], { type: 'application/xml' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'encriptacao.xml';
  a.click();

  URL.revokeObjectURL(url);
}