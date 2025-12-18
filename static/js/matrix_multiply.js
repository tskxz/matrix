const elements = {
  rows_a: document.getElementById("rows_a"),
  cols_a: document.getElementById("cols_a"),
  rows_b: document.getElementById("rows_b"),
  cols_b: document.getElementById("cols_b"),
  matrices: document.getElementById("matrices"),
  form: document.getElementById("matrixForm"),
  result: document.getElementById("result"),
  compatibilityMsg: document.getElementById("compatibilityMessage"),
  generateBtn: document.getElementById("generateBtn")
};

function checkCompatibility() {
  const cols_a = parseInt(elements.cols_a.value);
  const rows_b = parseInt(elements.rows_b.value);
  
  if (cols_a === rows_b) {
    elements.compatibilityMsg.innerHTML = " ✓ Compatível";
    elements.compatibilityMsg.style.color = "green";
    elements.generateBtn.disabled = false;
    return true;
  } else {
    elements.compatibilityMsg.innerHTML = ` ✗ Incompatível (colunas A=${cols_a} ≠ linhas B=${rows_b})`;
    elements.compatibilityMsg.style.color = "red";
    elements.generateBtn.disabled = true;
    return false;
  }
}

function generateInputs() {
  const r_a = parseInt(elements.rows_a.value);
  const c_a = parseInt(elements.cols_a.value);
  const r_b = parseInt(elements.rows_b.value);
  const c_b = parseInt(elements.cols_b.value);

  elements.matrices.innerHTML = `
    <div class="matrix-container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
      <div class="matrix-input">
        <h3>Matriz A (${r_a}×${c_a})</h3>
        ${Array(r_a).fill().map((_, i) => `
          <div class="matrix-row">
            ${Array(c_a).fill().map((_, j) => `
              <input type="number" step="0.01" value="0" data-matrix="A" data-row="${i}" data-col="${j}" required>
            `).join('')}
          </div>
        `).join('')}
      </div>
      
      <div class="matrix-input">
        <h3>Matriz B (${r_b}×${c_b})</h3>
        ${Array(r_b).fill().map((_, i) => `
          <div class="matrix-row">
            ${Array(c_b).fill().map((_, j) => `
              <input type="number" step="0.01" value="0" data-matrix="B" data-row="${i}" data-col="${j}" required>
            `).join('')}
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

function collectMatrixData() {
  const r_a = parseInt(elements.rows_a.value);
  const c_a = parseInt(elements.cols_a.value);
  const r_b = parseInt(elements.rows_b.value);
  const c_b = parseInt(elements.cols_b.value);
  
  const matrices = { matrix_a: [], matrix_b: [] };
  // Matriz A
  for (let i = 0; i < r_a; i++) {
    matrices.matrix_a[i] = [];
    for (let j = 0; j < c_a; j++) {
      const a = document.querySelector(
        `input[data-matrix="A"][data-row="${i}"][data-col="${j}"]`
      );
      matrices.matrix_a[i][j] = parseFloat(a.value) || 0;
    }
  }
  // Matriz B
  for (let i = 0; i < r_b; i++) {
    matrices.matrix_b[i] = [];
    for (let j = 0; j < c_b; j++) {
      const b = document.querySelector(
        `input[data-matrix="B"][data-row="${i}"][data-col="${j}"]`
      );
      matrices.matrix_b[i][j] = parseFloat(b.value) || 0;
    }
  }

  return matrices;
}

function matrixToHTML(matrix, title) {
  return `
                <div class="matrix-result">
                    <h4>${title}</h4>
                    <table>
                        <tbody>
                            ${matrix
                              .map(
                                (row) => `
                                <tr>
                                    ${row
                                      .map(
                                        (val) =>
                                          `<td>${parseFloat(val).toFixed(
                                            2
                                          )}</td>`
                                      )
                                      .join("")}
                                </tr>
                            `
                              )
                              .join("")}
                        </tbody>
                    </table>
                </div>
            `;
}

function displayResult(data) {
  elements.result.innerHTML = `
                <div class="result-container show">
                    <p><strong>Dimensões:</strong> ${data.dimensions}</p>
                    <div class="matrix-container">
                        ${matrixToHTML(data.matrix_a, "Matriz A")}
                        ${matrixToHTML(data.matrix_b, "Matriz B")}
                        ${matrixToHTML(data.result, "Resultado")}
                    </div>
                </div>
            `;
  elements.result.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function showError(msg) {
  elements.result.innerHTML = `<div class="alert alert-error show"><p>${msg}</p></div>`;
}

[elements.rows_a, elements.cols_a, elements.rows_b, elements.cols_b].forEach(input => {
  input.addEventListener('change', checkCompatibility);
});

elements.generateBtn.addEventListener('click', function() {
  if (checkCompatibility()) {
    generateInputs();
  }
});

elements.form.addEventListener("submit", async (e) => {
  e.preventDefault();
  e.stopPropagation();

  const payload = {
    rows_a: parseInt(elements.rows_a.value),
    cols_a: parseInt(elements.cols_a.value),
    rows_b: parseInt(elements.rows_b.value),
    cols_b: parseInt(elements.cols_b.value),
    ...collectMatrixData(),
  };

  console.log("Sending:", payload);

  try {
    const response = await fetch("/multiply", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    console.log("Response:", data);

    response.ok ? displayResult(data) : showError(data.error);
  } catch (error) {
    console.error("Error:", error);
    showError("Erro de comunicação");
  }
});

checkCompatibility();  // Verifica compatibilidade inicial