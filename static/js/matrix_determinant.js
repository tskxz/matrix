const elements = {
    size: document.getElementById("size"),
    matrixInput: document.getElementById("matrixInput"),
    form: document.getElementById("matrixForm"),
    result: document.getElementById("result"),
    generateBtn: document.getElementById("generateBtn"),
    calculateBtn: document.getElementById("calculateBtn"),
    method: document.getElementById("method")
};

function generateInputs() {
    const n = parseInt(elements.size.value);
    
    elements.matrixInput.innerHTML = `
        <div class="matrix-input">
            <h3>Matriz ${n}×${n}</h3>
            ${Array(n).fill().map((_, i) => `
                <div class="matrix-row">
                    ${Array(n).fill().map((_, j) => `
                        <input type="number" step="0.01" value="${i === j ? 1 : 0}" 
                               data-row="${i}" data-col="${j}" required
                               placeholder="${i}.${j}">
                    `).join('')}
                </div>
            `).join('')}
            <p class="hint">Preencha todos os elementos da matriz quadrada</p>
        </div>
    `;
    
    elements.calculateBtn.disabled = false;
}

function collectMatrixData() {
    const n = parseInt(elements.size.value);
    const matrix = [];
    
    for (let i = 0; i < n; i++) {
        matrix[i] = [];
        for (let j = 0; j < n; j++) {
            const input = document.querySelector(
                `input[data-row="${i}"][data-col="${j}"]`
            );
            matrix[i][j] = parseFloat(input.value) || 0;
        }
    }
    
    return matrix;
}

function matrixToHTML(matrix, title) {
    return `
        <div class="matrix-result">
            <h4>${title}</h4>
            <table>
                <tbody>
                    ${matrix.map(row => `
                        <tr>
                            ${row.map(val => {
                                // Formatar número
                                const num = parseFloat(val);
                                const isInteger = Math.abs(num - Math.round(num)) < 0.0001;
                                const formatted = isInteger ? 
                                    num.toFixed(0) : 
                                    num.toFixed(2);
                                
                                // Classe CSS baseada no tipo
                                const cellClass = isInteger ? 'integer' : 'decimal number';
                                
                                return `<td class="${cellClass}">${formatted}</td>`;
                            }).join('')}
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        </div>
    `;
}

function displayResult(data) {
    // Formatar determinante
    const detValue = parseFloat(data.determinant);
    const isInteger = Math.abs(detValue - Math.round(detValue)) < 0.0001;
    const formattedDet = isInteger ? detValue.toFixed(0) : detValue.toFixed(4);
    const valueType = isInteger ? 'integer' : 'float';
    
    elements.result.innerHTML = `
        <div class="result-container show">
            <div class="matrix-display">
                <h4>Matriz Informada</h4>
                ${matrixToHTML(data.matrix)}
            </div>
            
            <div class="result-details">
                <div class="determinant-value">
                    det(A) = <strong>${formattedDet}</strong>
                    <span class="value-type ${valueType}">
                        ${isInteger ? 'INTEIRO' : 'DECIMAL'}
                    </span>
                </div>
                
                <div style="text-align: center; margin-top: 1rem;">
                    ${data.determinant === 0 ? 
                        '<div class="alert alert-warning">⚠️ Matriz SINGULAR (determinante = 0)</div>' : 
                        '<div class="alert alert-success">✓ Matriz NÃO-SINGULAR (determinante ≠ 0)</div>'}
                </div>
            </div>
        </div>
    `;
}
function showError(msg) {
    elements.result.innerHTML = `
        <div class="alert alert-error show">
            <p><strong>Erro:</strong> ${msg}</p>
        </div>
    `;
}

// Event listeners
elements.generateBtn.addEventListener('click', generateInputs);
elements.size.addEventListener('change', generateInputs);

elements.form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const matrix = collectMatrixData();
    const size = parseInt(elements.size.value);
    const method = elements.method.value;
    
    const payload = {
        size: size,
        matrix: matrix,
        method: method
    };
    
    console.log("Enviando:", payload);
    
    try {
        const response = await fetch("/determinant", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        
        const data = await response.json();
        console.log("Resposta:", data);
        
        if (response.ok) {
            displayResult(data);
        } else {
            showError(data.error || "Erro desconhecido");
        }
    } catch (error) {
        console.error("Erro:", error);
        showError("Erro de comunicação com o servidor");
    }
});

// Inicializar
generateInputs();