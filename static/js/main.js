/**
 * Attach event listeners to form elements
 */
function attachEventListeners() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', handleFormSubmit);
    });
}

/**
 * Handle form submission
 */
function handleFormSubmit(e) {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const endpoint = form.action || window.location.pathname;

    // Show loading state
    showLoading(true);

    fetch(endpoint, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        showLoading(false);
        if (data.error) {
            showAlert('error', data.error);
        } else {
            displayResult(data);
            showAlert('success', 'Cálculo realizado com sucesso!');
        }
    })
    .catch(error => {
        showLoading(false);
        console.error('Error:', error);
        showAlert('error', 'Erro ao processar o cálculo. Verifique os dados e tente novamente.');
    });
}

/**
 * Display result in the page
 */
function displayResult(data) {
    let resultHTML = '<h3>Resultado:</h3>';
    
    if (data.result) {
        resultHTML += `<div class="matrix-result"><p>${data.result}</p></div>`;
    }
    
    if (data.matrix) {
        resultHTML += matrixToHTML(data.matrix);
    }
    
    if (data.details) {
        resultHTML += `<div class="alert alert-info"><p>${data.details}</p></div>`;
    }

    let resultContainer = document.querySelector('.result-container');
    
    if (!resultContainer) {
        resultContainer = document.createElement('div');
        resultContainer.className = 'result-container';
        document.querySelector('main').appendChild(resultContainer);
    }
    
    resultContainer.innerHTML = resultHTML;
    resultContainer.classList.add('show');
    resultContainer.scrollIntoView({ behavior: 'smooth' });
}

/**
 * Convert matrix to HTML table
 */
function matrixToHTML(matrix) {
    if (!Array.isArray(matrix) || matrix.length === 0) {
        return '';
    }

    let html = '<div class="matrix-result"><table>';
    
    matrix.forEach(row => {
        html += '<tr>';
        if (Array.isArray(row)) {
            row.forEach(cell => {
                html += `<td>${parseFloat(cell).toFixed(2)}</td>`;
            });
        } else {
            html += `<td>${parseFloat(row).toFixed(2)}</td>`;
        }
        html += '</tr>';
    });
    
    html += '</table></div>';
    return html;
}

/**
 * Show/hide loading indicator
 */
function showLoading(show) {
    let loader = document.querySelector('.loader');
    
    if (show) {
        if (!loader) {
            loader = document.createElement('div');
            loader.className = 'loader';
            loader.innerHTML = '<p>Calculando...</p>';
            document.body.appendChild(loader);
        }
        loader.style.display = 'flex';
    } else {
        if (loader) {
            loader.style.display = 'none';
        }
    }
}

/**
 * Show alert message
 */
function showAlert(type, message) {
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.innerHTML = `<p>${message}</p>`;
    document.querySelector('main').prepend(alert);
    setTimeout(() => alert.remove(), 5000);
}

/**
 * Parse matrix input from form
 * Expected format: rows separated by semicolons, elements by commas
 * Example: "1,2,3;4,5,6"
 */
function parseMatrixInput(input) {
    if (!input) return null;
    
    try {
        const rows = input.split(';').map(row => {
            return row.trim().split(',').map(num => {
                const parsed = parseFloat(num.trim());
                if (isNaN(parsed)) {
                    throw new Error(`Valor inválido: "${num.trim()}"`);
                }
                return parsed;
            });
        });
        return rows;
    } catch (error) {
        showAlert('error', `Erro ao processar matriz: ${error.message}`);
        return null;
    }
}

/**
 * Validate matrix dimensions
 */
function validateMatrixDimensions(matrix) {
    if (!matrix || !Array.isArray(matrix) || matrix.length === 0) {
        return false;
    }
    
    const firstRowLength = matrix[0].length;
    return matrix.every(row => row.length === firstRowLength);
}

/**
 * Get matrix dimensions
 */
function getMatrixDimensions(matrix) {
    if (!matrix || matrix.length === 0) return null;
    return {
        rows: matrix.length,
        columns: matrix[0].length
    };
}

/**
 * Format number for display
 */
function formatNumber(num) {
    if (Number.isInteger(num)) {
        return num.toString();
    }
    return parseFloat(num).toFixed(4);
}

/**
 * Clear form and results
 */
function clearResults() {
    const resultContainer = document.querySelector('.result-container');
    if (resultContainer) {
        resultContainer.classList.remove('show');
        setTimeout(() => {
            resultContainer.innerHTML = '';
        }, 300);
    }
}

/**
 * Export matrix as CSV
 */
function exportMatrixAsCSV(matrix, filename = 'matrix.csv') {
    if (!matrix || !Array.isArray(matrix)) return;
    
    let csvContent = 'data:text/csv;charset=utf-8,';
    matrix.forEach(row => {
        csvContent += row.join(',') + '\n';
    });
    
    const link = document.createElement('a');
    link.setAttribute('href', encodeURI(csvContent));
    link.setAttribute('download', filename);
    link.click();
}

/**
 * Show matrix info (dimensions, type, etc)
 */
function showMatrixInfo(matrix) {
    const dims = getMatrixDimensions(matrix);
    if (!dims) return '';
    
    return `Dimensões: ${dims.rows}×${dims.columns}`;
}

console.log('✓ main.js loaded');