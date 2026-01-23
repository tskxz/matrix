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
			decimalMatrix(result.result, 2)
		);

		document.getElementById('result').appendChild(exportBtn);

		const exportXMLBtn = document.createElement('button');
		exportXMLBtn.textContent = 'Exportar como XML';
		exportXMLBtn.className = 'btn-secondary';
		exportXMLBtn.style.marginTop = '0.5rem';

		exportXMLBtn.onclick = () => exportInverseAsXML(
			payload.matrix,
			decimalMatrix(result.result, 2)
		);

        document.getElementById('result').appendChild(exportXMLBtn);
		
	} catch (error) {
		showError(error.message);
	}
});

generateBtn.click();

const json = prettyJson(matrixA, 4); 


function exportInverseAsJSON(originalMatrix, inverseMatrix) {
	const json =
`{
  "operation": "inverse",
  "originalMatrix": ${prettyJson(originalMatrix, 4)},
  "inverseMatrix": ${prettyJson(inverseMatrix, 4)}
}`;
	
	const blob = new Blob([json], { type: 'application/json' });
	const url = URL.createObjectURL(blob);
	
	const a = document.createElement('a');
	a.href = url;
	a.download = 'matriz_inversa.json';
	a.click();
	
	URL.revokeObjectURL(url);
}

const xml = prettyXML(matrix, tagName);

function exportInverseAsXML(originalMatrix, inverseMatrix) {
  const xml =
`<?xml version="1.0" encoding="UTF-8"?>
<operation type="inverse">
${prettyXML(originalMatrix, 'originalMatrix')}
${prettyXML(inverseMatrix, 'inverseMatrix')}
</operation>`;

  const blob = new Blob([xml], { type: 'application/xml' });
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'matriz_inversa.xml';
  a.click();

  URL.revokeObjectURL(url);
}