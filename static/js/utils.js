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
    setTimeout(() => errorDiv.classList.remove('show'), 2000);
  }
}

function hideCalcularBotao(){
  const btn = document.getElementById('calcular-btn');
  if (btn) btn.style.display = 'none';
}

function showCalcularBotao() {
  const btn = document.getElementById('calcular-btn');
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