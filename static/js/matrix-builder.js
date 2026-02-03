function generateMatrixInput(rows, cols, containerId, label, gridId) {
  const container = document.getElementById(containerId);
  
  const section = document.createElement('div');
  section.className = 'matrix-section';
  section.innerHTML = `<h3>${label}</h3>`;

  const header = document.createElement('div');
  const importBtn = document.createElement('button');
  const fileInput = document.createElement('input');
  importBtn.textContent = 'Importar CSV';
  importBtn.type = 'button';
  fileInput.type = 'file';
  fileInput.accept = '.csv,text/csv';
  fileInput.style.display = 'none';
  fileInput.dataset.matrixId = gridId;

  importBtn.addEventListener('click', function() {
    fileInput.click();
  });

  fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    const reader = new FileReader();
    
    reader.onload = function(e) {
      const csvText = e.target.result;
      importMatrixFromCSV(csvText, gridId, rows, cols);
    };
    
    reader.onerror = function() {
      showError('Erro ao ler o ficheiro CSV.');
    };
    
    reader.readAsText(file);
    
    event.target.value = '';
  });

  header.appendChild(importBtn);
  header.appendChild(fileInput);

  section.appendChild(header);
  
  const grid = document.createElement('div');
  grid.className = 'matrix-input-grid';
  grid.style.gridTemplateColumns = `repeat(${cols}, 60px)`;
  grid.id = gridId;
  
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      const input = document.createElement('input');
      input.type = 'number';
      input.step = 'any';
      input.value = '0';
      input.dataset.row = i;
      input.dataset.col = j;
      grid.appendChild(input);
    }
  }
  
  section.appendChild(grid);
  container.appendChild(section);
}

function readMatrixValues(gridId) {
  const inputs = document.getElementById(gridId).querySelectorAll('input');
  const rows = Math.max(...Array.from(inputs).map(inp => parseInt(inp.dataset.row))) + 1;
  const cols = Math.max(...Array.from(inputs).map(inp => parseInt(inp.dataset.col))) + 1;
  
  const matrix = Array(rows).fill().map(() => Array(cols).fill(0));
  
  inputs.forEach(input => {
    const row = parseInt(input.dataset.row);
    const col = parseInt(input.dataset.col);
    matrix[row][col] = parseFloat(input.value) || 0;
  });
  
  return matrix;
}

function displayMatrix(matrix, title) {
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = `<h3>${title}</h3>`;
  
  const display = document.createElement('div');
  display.className = 'matrix-display';
  
  const table = document.createElement('table');
  matrix.forEach(row => {
    const tr = document.createElement('tr');
    row.forEach(value => {
      const td = document.createElement('td');
      td.textContent = Number.isInteger(value) ? value : value.toFixed(2);
      tr.appendChild(td);
    });
    table.appendChild(tr);
  });
  
  display.appendChild(table);
  resultDiv.appendChild(display);
  showResult();
}

function clearMatrixInputs() {
  const container = document.getElementById('matrix-inputs');
  if (container) container.innerHTML = '';
}