document.addEventListener("DOMContentLoaded", () => {
    const rowsAInput = document.getElementById("rowsA")
    const colsAInput = document.getElementById("colsA")
    const rowsBInput = document.getElementById("rowsB")
    const colsBInput = document.getElementById("colsB")
    const form = document.getElementById("matrixForm")
    const matricesDiv = document.getElementById("matrices")
  
    function updateRowsB() {
      rowsBInput.value = colsAInput.value
    }
  
    colsAInput.addEventListener("change", updateRowsB)
  
    function generateMatrices() {
      const rowsA = Number.parseInt(rowsAInput.value)
      const colsA = Number.parseInt(colsAInput.value)
      const rowsB = Number.parseInt(rowsBInput.value)
      const colsB = Number.parseInt(colsBInput.value)
  
      matricesDiv.innerHTML = ""
  
      const matrixADiv = document.createElement("div")
      matrixADiv.style.marginBottom = "2rem"
      matrixADiv.innerHTML = "<h3>Matriz A (" + rowsA + " × " + colsA + ")</h3>"
  
      const matrixATable = document.createElement("table")
      matrixATable.style.borderCollapse = "collapse"
      matrixATable.style.marginBottom = "1rem"
  
      for (let i = 0; i < rowsA; i++) {
        const row = document.createElement("tr")
        for (let j = 0; j < colsA; j++) {
          const cell = document.createElement("td")
          const input = document.createElement("input")
          input.type = "number"
          input.name = `matrixA[${i}][${j}]`
          input.id = `matrixA_${i}_${j}`
          input.step = "any"
          input.value = "0"
          input.style.width = "60px"
          input.style.padding = "8px"
          input.style.margin = "2px"
          input.style.border = "1px solid #ccc"
          input.style.textAlign = "center"
          cell.appendChild(input)
          row.appendChild(cell)
        }
        matrixATable.appendChild(row)
      }
  
      matrixADiv.appendChild(matrixATable)
      matricesDiv.appendChild(matrixADiv)
  
      const matrixBDiv = document.createElement("div")
      matrixBDiv.style.marginBottom = "2rem"
      matrixBDiv.innerHTML = "<h3>Matriz B (" + rowsB + " × " + colsB + ")</h3>"
  
      const matrixBTable = document.createElement("table")
      matrixBTable.style.borderCollapse = "collapse"
      matrixBTable.style.marginBottom = "1rem"
  
      for (let i = 0; i < rowsB; i++) {
        const row = document.createElement("tr")
        for (let j = 0; j < colsB; j++) {
          const cell = document.createElement("td")
          const input = document.createElement("input")
          input.type = "number"
          input.name = `matrixB[${i}][${j}]`
          input.id = `matrixB_${i}_${j}`
          input.step = "any"
          input.value = "0"
          input.style.width = "60px"
          input.style.padding = "8px"
          input.style.margin = "2px"
          input.style.border = "1px solid #ccc"
          input.style.textAlign = "center"
          cell.appendChild(input)
          row.appendChild(cell)
        }
        matrixBTable.appendChild(row)
      }
  
      matrixBDiv.appendChild(matrixBTable)
      matricesDiv.appendChild(matrixBDiv)
    }
  
    updateRowsB()
    generateMatrices()
  
    rowsAInput.addEventListener("change", () => {
      updateRowsB()
      generateMatrices()
    })
    colsAInput.addEventListener("change", () => {
      updateRowsB()
      generateMatrices()
    })
    colsBInput.addEventListener("change", generateMatrices)
  
    form.addEventListener("submit", (e) => {
      e.preventDefault()
  
      const rowsA = Number.parseInt(rowsAInput.value)
      const colsA = Number.parseInt(colsAInput.value)
      const rowsB = Number.parseInt(rowsBInput.value)
      const colsB = Number.parseInt(colsBInput.value)
  
      // Extrai os Valores da A
      const matrixA = []
      for (let i = 0; i < rowsA; i++) {
        const row = []
        for (let j = 0; j < colsA; j++) {
          const input = document.getElementById(`matrixA_${i}_${j}`)
          row.push(Number.parseFloat(input.value) || 0)
        }
        matrixA.push(row)
      }
  
      // Extrai os Valores da B
      const matrixB = []
      for (let i = 0; i < rowsB; i++) {
        const row = []
        for (let j = 0; j < colsB; j++) {
          const input = document.getElementById(`matrixB_${i}_${j}`)
          row.push(Number.parseFloat(input.value) || 0)
        }
        matrixB.push(row)
      }
  
      fetch("/multiply", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          matrixA: matrixA,
          matrixB: matrixB,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            displayResult(data.result)
          } else {
            alert("Erro: " + data.error)
          }
        })
        .catch((error) => {
          console.error("Erro:", error)
          alert("Erro ao conectar com o servidor")
        })
    })
  
    // function multiplyMatrices(a, b) {
    //   const result = []
    //   for (let i = 0; i < a.length; i++) {
    //     const row = []
    //     for (let j = 0; j < b[0].length; j++) {
    //       let sum = 0
    //       for (let k = 0; k < a[i].length; k++) {
    //         sum += a[i][k] * b[k][j]
    //       }
    //       row.push(sum)
    //     }
    //     result.push(row)
    //   }
    //   return result
    // }
  
    // Mostar Resultados
    function displayResult(matrix) {
      const resultDiv = document.getElementById("result")
      resultDiv.innerHTML = "<h3>Resultado (" + matrix.length + " × " + matrix[0].length + ")</h3>"
  
      const resultTable = document.createElement("table")
      resultTable.style.borderCollapse = "collapse"
      resultTable.style.marginTop = "1rem"
      resultTable.style.backgroundColor = "#f0f0f0"
  
      for (let i = 0; i < matrix.length; i++) {
        const row = document.createElement("tr")
        for (let j = 0; j < matrix[i].length; j++) {
          const cell = document.createElement("td")
          cell.textContent = Number.isInteger(matrix[i][j]) ? matrix[i][j] : matrix[i][j].toFixed(4)
          cell.style.padding = "10px"
          cell.style.border = "1px solid #999"
          cell.style.textAlign = "center"
          row.appendChild(cell)
        }
        resultTable.appendChild(row)
      }
  
      resultDiv.appendChild(resultTable)
    }
  })