sequenceDiagram
    autonumber
    participant Client
    participant JS as JavaScript<br/>(matrix_advanced.js)
    participant Flask as Flask<br/>(/inverse route)
    participant Matrix as Matrix Object
    participant Det as determinant()
    participant Minor as _get_minor()

    Client->>JS: Fill matrix & click "Calculate Inverse"
    JS->>JS: collectMatrixData()
    JS->>Flask: POST /inverse<br/>{matrix: {...}}
    
    Flask->>Flask: request.get_json()
    Flask->>Matrix: Matrix(rows, cols, data)
    Matrix->>Matrix: is_square()
    
    alt Not Square
        Flask-->>JS: Error 400 "Must be square"
        JS->>Client: showError()
    else Square
        Matrix->>Det: determinant()
        Det-->>Matrix: det_value
        
        alt det == 0
            Flask-->>JS: Error 400 "Singular matrix"
            JS->>Client: showError("Matrix is not invertible")
        else det ≠ 0
            Matrix->>Matrix: inverse()
            
            alt 2×2 Matrix
                Matrix->>Matrix: Swap a↔d, negate b,c
                Matrix->>Matrix: scalar_multiply(1/det)
            else n×n Matrix (n≥3)
                loop For each row i
                    loop For each col j
                        Matrix->>Minor: _get_minor(i, j)
                        Minor-->>Matrix: submatrix
                        Matrix->>Det: determinant() on minor
                        Det-->>Matrix: minor_det
                        Matrix->>Matrix: cofactor = (-1)^(i+j) * minor_det
                        Matrix->>Matrix: adjugate[j][i] = cofactor
                    end
                end
                Matrix->>Matrix: scalar_multiply(1/det)
            end
            
            Matrix-->>Flask: Inverse matrix
            Flask->>Flask: inverse.to_dict()
            Flask-->>JS: JSON {result: {...}}
            JS->>JS: displayResult(data)
            JS->>JS: matrixToHTML(inverse)
            JS->>Client: Display inverse matrix
        end
    end