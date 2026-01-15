sequenceDiagram
    participant Client as Client (Browser)
    participant JS as JavaScript<br/>(static/js/*.js)
    participant Flask as Flask Server<br/>(app.py)
    participant Matrix as Matrix Class<br/>(core/matrix.py)
    participant Template as HTML Templates<br>(templates/*.html)
    autonumber

    %% Initial Page Load
    rect rgb(240, 248, 255)
        Note over Client,Template: Initial Page Load (GET Request)
        Client->>Flask: GET /[endpoint]
        Flask->>Template: render_template('*.html')
        Template-->>Flask: HTML Response
        Flask-->>Client: HTML + CSS + JS
        Client->>JS: Load JavaScript files
        JS->>JS: Initialize DOM elements
        JS->>JS: Attach event listeners
        JS->>JS: generateInputs()
    end

    %% Form Submission
    rect rgb(255, 250, 240)
        Note over Client,Matrix: Form Submission (POST Request)
        Client->>JS: Fill form & click Submit
        JS->>JS: e.preventDefault()
        JS->>JS: collectMatrixData()
        JS->>JS: Build payload object
        
        JS->>Flask: fetch('/[endpoint]', {<br/>method: 'POST',<br/>headers: {'Content-Type': 'application/json'},<br/>body: JSON.stringify(payload)})
        
        Flask->>Flask: request.get_json()
        Flask->>Flask: Validate input data
        
        alt Valid Data
            Flask->>Matrix: Create Matrix objects<br/>Matrix(rows, cols, data)
            Matrix->>Matrix: Perform operation<br/>(add/multiply/inverse/etc.)
            Matrix-->>Flask: Return result dict
            Flask-->>JS: jsonify({result, ...})
            JS->>JS: displayResult(data)
            JS->>Client: Update DOM with result
        else Invalid Data
            Flask-->>JS: jsonify({error: '...'}), 400
            JS->>JS: showError(msg)
            JS->>Client: Display error message
        end
    end

    %% Example: Encryption Flow
    rect rgb(240, 255, 240)
        Note over Client,Matrix: Example: Encryption Flow
        Client->>JS: Enter message + matrix
        JS->>Flask: POST /encrypt<br/>{operation, message, matrix}
        Flask->>Matrix: encoding_matrix.determinant()
        
        alt det ≠ 0 (Invertible)
            Flask->>Matrix: encrypt_message(message, matrix)
            Matrix->>Matrix: Convert text → numbers
            Matrix->>Matrix: Build message matrix
            Matrix->>Matrix: Multiply matrices
            Matrix-->>Flask: {encrypted_matrix, numeric_sequence}
            Flask-->>JS: JSON response
            JS->>Client: Show encrypted result
        else det = 0 (Singular)
            Flask-->>JS: {error: 'Matriz singular'}
            JS->>Client: Show error
        end
    end