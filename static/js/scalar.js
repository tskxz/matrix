const form = document.getElementById("matrix-form");
const generateBtn = document.getElementById("generate-btn");

generateBtn.addEventListener("click", function () {
        const rows = parseInt(document.getElementById("rows").value);
        const cols = parseInt(document.getElementById("cols").value);

        clearMatrixInputs();
        hideError();
        hideResult();

        generateMatrixInput(rows, cols, "matrix-inputs", "Matriz", "matrix-a");
});

form.addEventListener("submit", async function (e) {
        e.preventDefault();
        hideError();
        hideResult();

        const payload = {
                rows: parseInt(document.getElementById("rows").value),
                cols: parseInt(document.getElementById("cols").value),
                matrix: readMatrixValues("matrix-a"),
                scalar: parseFloat(document.getElementById("scalar").value),
        };

        try {
                const result = await apiCall("/scalar", payload);
                displayMatrix(
                        result.result,
                        `Resultado (${payload.scalar} × Matriz)`,
                );

                const exportBtn = document.createElement("button");
                exportBtn.textContent = "Exportar como JSON";
                exportBtn.className = "btn-secondary";
                exportBtn.style.marginTop = "1rem";

                exportBtn.onclick = () =>
                        exportScalarAsJSON(
                                payload.scalar,
                                payload.matrix,
                                result.result,
                        );

                document.getElementById("result").appendChild(exportBtn);

                const exportXMLBtn = document.createElement("button");
                exportXMLBtn.textContent = "Exportar como XML";
                exportXMLBtn.className = "btn-secondary";
                exportXMLBtn.style.marginTop = "0.5rem";

                exportXMLBtn.onclick = () =>
                        exportScalarAsXML(
                                payload.scalar,
                                payload.matrix,
                                result.result,
                        );

                document.getElementById("result").appendChild(exportXMLBtn);

                const exportHTMLBtn = document.createElement("button");
                exportHTMLBtn.textContent = "Exportar como HTML";
                exportHTMLBtn.className = "btn-secondary";
                exportHTMLBtn.style.marginTop = "0.5rem";

                exportHTMLBtn.onclick = () =>
                        exportScalarAsHTML(
                                payload.scalar,
                                payload.matrix,
                                result.result,
                        );

                document.getElementById("result").appendChild(exportHTMLBtn);
        } catch (error) {
                showError(error.message);
        }
});

generateBtn.click();

function exportScalarAsJSON(scalar, matrix, resultMatrix) {
        const json = `{
  "operation": "scalar",
  "scalar": ${scalar},
  "matrix": ${prettyJson(matrix, 4)},
  "result": ${prettyJson(resultMatrix, 4)}
}`;

        const blob = new Blob([json], { type: "application/json" });
        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "scalar_multiplication.json";
        a.click();

        URL.revokeObjectURL(url);
}

function exportScalarAsXML(scalar, matrix, resultMatrix) {
        const xml = `<?xml version="1.0" encoding="UTF-8"?>
<operation type="scalar">
  <scalar>${scalar}</scalar>
${prettyXML(matrix, "matrix")}
${prettyXML(resultMatrix, "result")}
</operation>`;

        const blob = new Blob([xml], { type: "application/xml" });
        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "scalar_multiplication.xml";
        a.click();

        URL.revokeObjectURL(url);
}

function exportScalarAsHTML(scalar, matrix, resultMatrix) {
        const html = `<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <title>Multiplicação por Escalar</title>
</head>
<body>
  <h1>Operação: Multiplicação por Escalar</h1>
  <h3>Escalar: ${scalar}</h3>

  ${prettyHTML(matrix, "Matriz Original")}
  ${prettyHTML(resultMatrix, "Resultado")}
</body>
</html>`;

        const blob = new Blob([html], { type: "text/html" });
        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "scalar_multiplication.html";
        a.click();

        URL.revokeObjectURL(url);
}
