const form = document.getElementById("decrypt-form");
const generateBtn = document.getElementById("generate-btn");

generateBtn.addEventListener("click", function () {
        const size = parseInt(document.getElementById("size").value);
        const encryptedCols = parseInt(
                document.getElementById("encrypted-cols").value,
        );

        clearMatrixInputs();
        hideError();
        hideResult();

        generateMatrixInput(
                size,
                size,
                "matrix-inputs",
                "Matriz de Codificação",
                "encoding-matrix",
        );
        generateMatrixInput(
                size,
                encryptedCols,
                "matrix-inputs",
                "Matriz Encriptada",
                "encrypted-matrix",
        );
});

form.addEventListener("submit", async function (e) {
        e.preventDefault();
        hideError();
        hideResult();

        const size = parseInt(document.getElementById("size").value);
        const encryptedCols = parseInt(
                document.getElementById("encrypted-cols").value,
        );

        const payload = {
                size: size,
                encoding_matrix: readMatrixValues("encoding-matrix"),
                encrypted_cols: encryptedCols,
                encrypted_matrix: readMatrixValues("encrypted-matrix"),
        };

        try {
                const result = await apiCall("/decrypt", payload);
                const resultDiv = document.getElementById("result");
                resultDiv.innerHTML = `<h3>Mensagem Desencriptada</h3><p style="font-size: 1.2rem; padding: 1rem; background: #f8f9fa; border-radius: 4px;">${result.decrypted_message}</p>`;
                showResult();

                const exportBtn = document.createElement("button");
                exportBtn.textContent = "Exportar como JSON";
                exportBtn.className = "btn-secondary";
                exportBtn.style.marginTop = "1rem";

                exportBtn.onclick = () =>
                        exportDecryptAsJSON(
                                payload.encoding_matrix,
                                payload.encrypted_matrix,
                                result.decrypted_message,
                        );

                resultDiv.appendChild(exportBtn);

                showResult();

                const exportXMLBtn = document.createElement("button");
                exportXMLBtn.textContent = "Exportar como XML";
                exportXMLBtn.className = "btn-secondary";
                exportXMLBtn.style.marginTop = "0.5rem";

                exportXMLBtn.onclick = () =>
                        exportDecryptAsXML(
                                payload.encoding_matrix,
                                payload.encrypted_matrix,
                                result.decrypted_message,
                        );

                resultDiv.appendChild(exportXMLBtn);

                const exportHTMLBtn = document.createElement("button");
                exportHTMLBtn.textContent = "Exportar como HTML";
                exportHTMLBtn.className = "btn-secondary";
                exportHTMLBtn.style.marginTop = "0.5rem";

                exportHTMLBtn.onclick = () =>
                        exportDecryptAsHTML(
                                payload.encoding_matrix,
                                payload.encrypted_matrix,
                                result.decrypted_message,
                        );

                document.getElementById("result").appendChild(exportHTMLBtn);
        } catch (error) {
                showError(error.message);
        }
});

generateBtn.click();

function exportDecryptAsJSON(
        encodingMatrix,
        encryptedMatrix,
        decryptedMessage,
) {
        const json = `{
  "operation": "decrypt",
  "encodingMatrix": ${prettyJson(encodingMatrix, 4)},
  "encryptedMatrix": ${prettyJson(encryptedMatrix, 4)},
  "decryptedMessage": "${decryptedMessage}"
}`;

        const blob = new Blob([json], { type: "application/json" });
        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "desencriptacao.json";
        a.click();

        URL.revokeObjectURL(url);
}

function exportDecryptAsXML(encodingMatrix, encryptedMatrix, decryptedMessage) {
        const xml = `<?xml version="1.0" encoding="UTF-8"?>
<operation type="decrypt">
  ${prettyXML(encodingMatrix, "encodingMatrix")}
  ${prettyXML(encryptedMatrix, "encryptedMatrix")}
  <decryptedMessage>${decryptedMessage}</decryptedMessage>
</operation>`;

        const blob = new Blob([xml], { type: "application/xml" });
        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "desencriptacao.xml";
        a.click();

        URL.revokeObjectURL(url);
}

function exportDecryptAsHTML(
        encodingMatrix,
        encryptedMatrix,
        decryptedMessage,
) {
        const html = `<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <title>Desencriptação</title>
</head>
<body>
  <h1>Operação: Decrypt</h1>

  <h2>Matriz de Codificação</h2>
  ${prettyHTML(encodingMatrix, "encodingMatrix")}

  <h2>Matriz Encriptada</h2>
  ${prettyHTML(encryptedMatrix, "encryptedMatrix")}

  <h2>Mensagem Desencriptada</h2>
  <p style="font-size:1.2rem; padding:1rem; background:#f8f9fa; border-radius:4px;">
    ${decryptedMessage}
  </p>
</body>
</html>`;

        const blob = new Blob([html], { type: "text/html" });
        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "desencriptacao.html";
        a.click();

        URL.revokeObjectURL(url);
}
