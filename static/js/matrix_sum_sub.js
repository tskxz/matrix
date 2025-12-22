const elements = {
  rows: document.getElementById("rows"),
  cols: document.getElementById("cols"),
  matrices: document.getElementById("matrices"),
  form: document.getElementById("matrixForm"),
  result: document.getElementById("result"),
  operation: document.getElementById("operation"),
};

function generateInputs() {
  const r = parseInt(elements.rows.value);
  const c = parseInt(elements.cols.value);

  elements.matrices.innerHTML = `
                <div class="matrix-container">
                    ${["A", "B"]
                      .map(
                        (name) => `
                        <div class="matrix-input">
                            <h3>Matriz ${name}</h3>
                            ${Array(r)
                              .fill()
                              .map(
                                (_, i) => `
                                <div class="matrix-row">
                                    ${Array(c)
                                      .fill()
                                      .map(
                                        (_, j) =>
                                          `<input type="number" step="0.01" value="0" data-matrix="${name}" data-row="${i}" data-col="${j}" required>`
                                      )
                                      .join("")}
                                </div>
                            `
                              )
                              .join("")}
                        </div>
                    `
                      )
                      .join("")}
                </div>
            `;
}

function collectMatrixData() {
  const r = parseInt(elements.rows.value);
  const c = parseInt(elements.cols.value);
  const matrices = { matrix_a: [], matrix_b: [] };

  for (let i = 0; i < r; i++) {
    matrices.matrix_a[i] = [];
    matrices.matrix_b[i] = [];
    for (let j = 0; j < c; j++) {
      const a = document.querySelector(
        `input[data-matrix="A"][data-row="${i}"][data-col="${j}"]`
      );
      const b = document.querySelector(
        `input[data-matrix="B"][data-row="${i}"][data-col="${j}"]`
      );
      matrices.matrix_a[i][j] = parseFloat(a.value);
      matrices.matrix_b[i][j] = parseFloat(b.value);
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
                    <h3>${data.operation}</h3>
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

elements.rows.addEventListener("change", generateInputs);
elements.cols.addEventListener("change", generateInputs);

elements.form.addEventListener("submit", async (e) => {
  e.preventDefault();
  e.stopPropagation();

  const payload = {
    rows: parseInt(elements.rows.value),
    cols: parseInt(elements.cols.value),
    operation: elements.operation.value,
    ...collectMatrixData(),
  };

  try {
    const response = await fetch("/sum", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    
    response.ok ? displayResult(data) : showError(data.error);
  } catch (error) {
    console.error("Error:", error);
    showError("Erro de comunicação");
  }
});

generateInputs();
