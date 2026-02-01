async function apiCall(endpoint, data) {
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  
  const result = await response.json();
  
  if (!response.ok) {
    throw new Error(result.error || 'API ERROR!');
  }
  
  return result;
}

function showError(message) {
  const errorDiv = document.getElementById('error');
  if (errorDiv) {
    errorDiv.textContent = message;
    errorDiv.classList.add('show');
  }
}

function hideCalculateButton(){
  const btn = document.getElementById('calculate-btn');
  if (btn) btn.style.display = 'none';
}

function showCalculateButton() {
  const btn = document.getElementById('calculate-btn');
  if (btn) btn.style.display = 'block';
}

function hideError() {
  document.getElementById('error')?.classList.remove('show');
}

function showResult() {
  document.getElementById('result')?.classList.add('show');
}

function hideResult() {
  document.getElementById('result')?.classList.remove('show');
}

function prettyJson(matrix, indent = 2) {
  const space = ' '.repeat(indent);
  return '[\n' +
  matrix
  .map(row => `${space}[${row.join(', ')}]`)
  .join(',\n') +
  '\n]';
}

function decimalMatrix(matrix, decimals = 2) {
  return matrix.map(row =>
    row.map(num => Number(num.toFixed(decimals)))
  );
}

function prettyXML(matrix, tagName) {
  let xml =`<${tagName}>\n`;

  matrix.forEach(row => {
    xml += `    <row>${row.join(', ')}</row>\n`;
  });

  xml += `  </${tagName}>\n`;
  return xml;
}

function prettyHTML(matrix, title) {
  let html = `<h3>${title}</h3>`;
  html += '<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; font-family: monospace;">';

  matrix.forEach(row => {
    html += '<tr>';
    row.forEach(value => {
      html += `<td>${value}</td>`;
    });
    html += '</tr>';
  });

  html += '</table>';
  return html;
}

function importMatrixFromCSV(csvText, matrixId, expectedRows, expectedCols) {
  try {
    // Divide o CSV em linhas
    const lines = csvText.trim().split('\n').filter(line => line.trim() !== '');
    
    if (lines.length === 0) {
      throw new Error('Arquivo CSV vazio.');
    }
    
    // Parse da matriz
    const matrix = lines.map(line => 
      line.split(',').map(num => {
        const val = num.trim();
        return val === '' ? 0 : parseFloat(val);
      })
    );
    
    // Verifica se todas as linhas têm o mesmo número de colunas
    const cols = matrix[0].length;
    if (!matrix.every(row => row.length === cols)) {
      throw new Error('Todas as linhas devem ter o mesmo número de elementos.');
    }
    
    // Verifica se as dimensões correspondem às esperadas
    if (expectedRows && expectedCols) {
      if (matrix.length !== expectedRows || cols !== expectedCols) {
        throw new Error(`Dimensões incorretas. Esperado: ${expectedRows}x${expectedCols}, Obtido: ${matrix.length}x${cols}`);
      }
    }
    
    // Preenche os inputs da matriz
    for (let i = 0; i < matrix.length; i++) {
      for (let j = 0; j < matrix[i].length; j++) {
        const input = document.querySelector(`#${matrixId} [data-row="${i}"][data-col="${j}"]`);
        if (input) {
          input.value = matrix[i][j];
          input.dispatchEvent(new Event('input'));
        }
      }
    }
    
    showSuccess(`Matriz ${matrixId === 'matrix-a' ? 'A' : 'B'} importada com sucesso!`);
    
  } catch (error) {
    console.error('Erro ao importar CSV:', error);
    showError('Erro ao importar CSV: ' + error.message);
  }
}

function showSuccess(message) {
  hideError();
  const successDiv = document.createElement('div');
  successDiv.className = 'success-message';
  successDiv.textContent = message;
  successDiv.style.margin = '0.5rem 0';
  successDiv.style.padding = '0.5rem';
  successDiv.style.backgroundColor = '#d4edda';
  successDiv.style.color = '#155724';
  successDiv.style.border = '1px solid #c3e6cb';
  successDiv.style.borderRadius = '0.25rem';
  successDiv.style.fontSize = '0.9rem';
  
  setTimeout(() => {
    if (successDiv.parentNode) {
      successDiv.parentNode.removeChild(successDiv);
    }
  }, 3000);
  
  const form = document.getElementById('matrix-form');
  form.parentNode.insertBefore(successDiv, form.nextSibling);
}