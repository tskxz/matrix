sequenceDiagram
    autonumber
    participant Client
    participant JS as JavaScript<br/>(matrix_encryption.js)
    participant Flask as Flask<br/>(/encrypt route)
    participant Matrix as Encoding Matrix
    participant Crypto as Encryption Module
    participant MsgMatrix as Message Matrix

    Client->>JS: Enter message & encoding matrix
    JS->>JS: collectMatrixData()
    JS->>Flask: POST /encrypt<br/>{message: "text", encoding_matrix: {...}}
    
    Flask->>Flask: request.get_json()
    Flask->>Matrix: Matrix(rows, cols, encoding_data)
    Matrix->>Matrix: determinant()
    
    alt det == 0
        Flask-->>JS: Error 400 "Singular matrix"
        JS->>Client: showError("Matrix is not invertible")
    else det ≠ 0
        Flask->>Crypto: encrypt_message(message, encoding_matrix)
        Crypto->>Crypto: text_to_numbers(message)
        
        Note over Crypto: Convert: A→0, B→1, ..., Z→25<br/>Space→26
        
        Crypto->>Crypto: Calculate chunk_size<br/>(rows * cols of encoding matrix)
        Crypto->>Crypto: Pad message to fit chunks
        
        loop For each chunk
            Crypto->>MsgMatrix: Create message matrix<br/>(based on encoding matrix dimensions)
            MsgMatrix->>Matrix: multiply(message_matrix)
            Matrix-->>MsgMatrix: Encrypted chunk
            Crypto->>Crypto: Append to numeric_sequence
        end
        
        Crypto-->>Flask: {encrypted_matrix, numeric_sequence}
        Flask-->>JS: JSON {encrypted_message: [...]}
        JS->>JS: displayResult(data)
        JS->>Client: Display encrypted numbers
    end