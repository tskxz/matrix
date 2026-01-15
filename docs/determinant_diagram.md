sequenceDiagram
    autonumber
    participant Client
    participant JS as JavaScript<br/>(matrix_advanced.js)
    participant Flask as Flask<br/>(/determinant route)
    participant Matrix as Matrix Object

    Client->>JS: Fill matrix & click "Calculate Determinant"
    JS->>JS: collectMatrixData()
    JS->>JS: Check if square matrix
    
    alt Not Square
        JS->>Client: showError("Matrix must be square")
    else Square Matrix
        JS->>Flask: POST /determinant<br/>{matrix: {...}}
        Flask->>Flask: request.get_json()
        Flask->>Matrix: Matrix(rows, cols, data)
        Matrix->>Matrix: is_square()
        
        alt Not Square (server check)
            Flask-->>JS: Error 400
            JS->>Client: showError()
        else Square
            Matrix->>Matrix: determinant()
            
            alt 1×1 Matrix
                Matrix->>Matrix: return data[0][0]
            else 2×2 Matrix
                Matrix->>Matrix: return (a*d - b*c)
            else 3×3 Matrix
                Matrix->>Matrix: Sarrus rule calculation
            else n×n Matrix (n>3)
                loop For each column
                    Matrix->>Matrix: _get_minor(0, col)
                    Matrix->>Matrix: determinant() [recursive]
                    Matrix->>Matrix: cofactor * minor_det
                end
            end
            
            Matrix-->>Flask: determinant value (float)
            Flask-->>JS: JSON {determinant: value}
            JS->>JS: displayResult(data)
            JS->>Client: Display "Determinant: {value}"
        end
    end