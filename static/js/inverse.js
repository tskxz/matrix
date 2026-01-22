const form = document.getElementById('matrix-form');
const generateBtn = document.getElementById('generate-btn');

generateBtn.addEventListener('click', function() {
	const size = parseInt(document.getElementById('size').value);
	
	clearMatrixInputs();
	hideError();
	hideResult();
	
	generateMatrixInput(size, size, 'matrix-inputs', 'Matriz', 'matrix-a');
});

form.addEventListener('submit', async function(e) {
	e.preventDefault();
	hideError();
	hideResult();
	
	const size = parseInt(document.getElementById('size').value);
	
	const payload = {
		size: size,
		matrix: readMatrixValues('matrix-a')
	};
	
	try {
		const result = await apiCall('/inverse', payload);
		displayMatrix(result.result, 'Matriz Inversa');

		const exportBtn = document.createElement('button');
              exportBtn.textContent = 'Exportar como JSON';
              exportBtn.className = 'btn-secondary';
              exportBtn.style.marginTop = '1rem';
			  

              exportBtn.onclick = () => exportInverseAsJSON(
              payload.matrix,
              roundMatrix(result.result, 2) // ← aqui arredonda
);

    document.getElementById('result').appendChild(exportBtn);

	} catch (error) {
		showError(error.message);
	}
});

generateBtn.click();

const json = formatMatrix(matrixA, 4); 


function exportInverseAsJSON(originalMatrix, inverseMatrix) {
  const json =
`{
  "operation": "inverse",
  "originalMatrix": ${formatMatrix(originalMatrix, 4)},
  "inverseMatrix": ${formatMatrix(inverseMatrix, 4)}
}`;

  const blob = new Blob([json], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'matriz_inversa.json';
  a.click();

  URL.revokeObjectURL(url);
}
