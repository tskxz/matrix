sequenceDiagram
    autonumber
    participant Client
    participant JS as JavaScript<br/>(static/js/*.js)
    participant Flask as Flask<br/>(/multiply route)
    participant MatrixA as Matrix A Object
    participant MatrixB as Matrix B Object
    participant Result as Result Matrix

    Client->>JS: Fill matrices & click "Multiply"
    JS->>JS: collectMatrixData()
    JS->>JS: Validate dimensions<br/>(cols_A == rows_B)
    
    alt Incompatible Dimensions
        JS->>Client: showError("Incompatible dimensions")
    else Compatible
        JS->>Flask: POST /multiply<br/>{matrixA: {...}, matrixB: {...}}
        Flask->>Flask: request.get_json()
        Flask->>MatrixA: Matrix(rows, cols, data_A)
        Flask->>MatrixB: Matrix(rows, cols, data_B)
        
        MatrixA->>MatrixB: multiply(matrixB)
        
        loop For each row i in A
            loop For each col j in B
                MatrixB->>MatrixB: sum(A[i][k] * B[k][j])
            end
        end
        
        MatrixB-->>MatrixA: New Matrix (result)
        MatrixA->>Result: Create result matrix
        Result->>Result: to_dict()
        Result-->>Flask: {rows, cols, data}
        Flask-->>JS: JSON {result: {...}}
        JS->>JS: displayResult(data)
        JS->>JS: matrixToHTML(result)
        JS->>Client: Display result matrix
    end