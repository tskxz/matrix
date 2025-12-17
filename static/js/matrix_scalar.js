const elements = {
  rows: document.getElementById("rows"),
  cols: document.getElementById("cols"),
  matrices: document.getElementById("matrices"),
  form: document.getElementById("matrixForm"),
  result: document.getElementById("result"),
};

function generateInputs() {
  const r = parseInt(elements.rows.value);
  const c = parseInt(elements.cols.value);

  elements.matrices.innerHTML = `
                <div class="matrix-container">
                    ${["A"]
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
  const matrices = { matrix_a: [] };

  for (let i = 0; i < r; i++) {
    matrices.matrix_a[i] = [];
    for (let j = 0; j < c; j++) {
      const a = document.querySelector(
        `input[data-matrix="A"][data-row="${i}"][data-col="${j}"]`
      );
      
      matrices.matrix_a[i][j] = parseFloat(a.value);
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
    ...collectMatrixData(),
  };

  console.log("Sending:", payload);

  try {
    const response = await fetch("/scalar", {
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

generateInputs();
