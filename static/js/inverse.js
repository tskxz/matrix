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
	} catch (error) {
		showError(error.message);
	}
});

generateBtn.click();