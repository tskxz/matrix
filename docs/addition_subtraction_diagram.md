sequenceDiagram
    autonumber
    participant Client
    participant JS as JavaScript<br/>(matrix_operations.js)
    participant Flask as Flask<br/>(/add or /subtract route)
    participant MatrixA as Matrix A
    participant MatrixB as Matrix B

    Client->>JS: Fill two matrices & select operation
    JS->>JS: collectMatrixData()
    
    alt Addition Selected
        JS->>Flask: POST /add<br/>{matrixA: {...}, matrixB: {...}}
    else Subtraction Selected
        JS->>Flask: POST /subtract<br/>{matrixA: {...}, matrixB: {...}}
    end
    
    Flask->>Flask: request.get_json()
    Flask->>MatrixA: Matrix(rows_A, cols_A, data_A)
    Flask->>MatrixB: Matrix(rows_B, cols_B, data_B)
    
    MatrixA->>MatrixB: is_same_dimension(matrixB)
    
    alt Different Dimensions
        Flask-->>JS: Error 400 "Incompatible dimensions"
        JS->>Client: showError("Matrices must have same dimensions")
    else Same Dimensions
        alt Addition Operation
            MatrixA->>MatrixB: add(matrixB)
            
            loop For each row i
                loop For each col j
                    MatrixB->>MatrixB: result[i][j] = A[i][j] + B[i][j]
                end
            end
        else Subtraction Operation
            MatrixA->>MatrixB: subtract(matrixB)
            
            loop For each row i
                loop For each col j
                    MatrixB->>MatrixB: result[i][j] = A[i][j] - B[i][j]
                end
            end
        end
        
        MatrixB-->>MatrixA: Result matrix
        MatrixA->>MatrixA: to_dict()
        MatrixA-->>Flask: {rows, cols, data}
        Flask-->>JS: JSON {result: {...}}
        JS->>JS: displayResult(data)
        JS->>Client: Display result matrix
    end