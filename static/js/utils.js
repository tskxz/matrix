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

function formatMatrixXML(matrix, tagName) {
  let xml = `<${tagName}>\n`;

  matrix.forEach(row => {
    xml += `    <row>${row.join(', ')}</row>\n`;
  });

  xml += `  </${tagName}>\n`;
  return xml;
}