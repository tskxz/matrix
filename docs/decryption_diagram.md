sequenceDiagram
    autonumber
    participant Client
    participant JS as JavaScript<br/>(static/js/*.js)
    participant Flask as Flask<br/>(/decrypt route)
    participant Matrix as Encoding Matrix
    participant Inverse as Inverse Matrix
    participant Crypto as Encryption Module
    participant MsgMatrix as Encrypted Matrix

    Client->>JS: Enter encrypted numbers & encoding matrix
    JS->>JS: collectMatrixData()
    JS->>Flask: POST /decrypt<br/>{encrypted: [...], encoding_matrix: {...}}
    
    Flask->>Flask: request.get_json()
    Flask->>Matrix: Matrix(rows, cols, encoding_data)
    Matrix->>Matrix: determinant()
    
    alt det == 0
        Flask-->>JS: Error 400 "Singular matrix"
        JS->>Client: showError("Cannot decrypt")
    else det ≠ 0
        Matrix->>Inverse: inverse()
        Inverse-->>Flask: Inverse matrix
        
        Flask->>Crypto: decrypt_message(encrypted, encoding_matrix)
        Crypto->>Crypto: Split encrypted into chunks
        
        loop For each encrypted chunk
            Crypto->>MsgMatrix: Create encrypted matrix
            MsgMatrix->>Inverse: multiply(inverse_matrix)
            Inverse-->>MsgMatrix: Decrypted numbers
            Crypto->>Crypto: Append to numeric_sequence
        end
        
        Crypto->>Crypto: numbers_to_text(numeric_sequence)
        
        Note over Crypto: Convert: 0→A, 1→B, ..., 25→Z<br/>26→Space
        
        Crypto-->>Flask: Original message (string)
        Flask-->>JS: JSON {decrypted_message: "text"}
        JS->>JS: displayResult(data)
        JS->>Client: Display original message
    end