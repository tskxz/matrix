graph TB
    Client([Client])

    Client --> Menu[Access Main Menu]
    
    Menu --> SumSub[Sum/Subtraction Operations]
    Menu --> Scalar[Scalar Multiplication]
    Menu --> Multiply[Matrix Multiplication]
    Menu --> Det[Determinant Calculation]
    Menu --> Inverse[Matrix Inverse]
    Menu --> Encrypt[Hill Cipher Encryption]
    
    SumSub --> SumSubInput[Input Two Matrices<br/>Same Dimensions]
    SumSubInput --> SumOp[Perform Addition]
    SumSubInput --> SubOp[Perform Subtraction]
    SumOp --> DisplayResult[Display Result Matrix]
    SubOp --> DisplayResult
    
    Scalar --> ScalarInput[Input Matrix + Scalar Value]
    ScalarInput --> ScalarCalc[Multiply Each Element]
    ScalarCalc --> DisplayResult
    
    Multiply --> MultiplyInput[Input Two Matrices<br/>A: m×n, B: n×p]
    MultiplyInput --> CompatCheck{Check Compatibility<br/>cols_A = rows_B?}
    CompatCheck -->|Yes| MultiplyCalc[Perform Multiplication]
    CompatCheck -->|No| ShowError[Show Error Message]
    MultiplyCalc --> DisplayResult
    
    Det --> DetInput[Input Square Matrix<br/>n×n, max 6×6]
    DetInput --> SelectMethod[Select Method:<br/>Auto/Direct/Laplace]
    SelectMethod --> DetCalc[Calculate Determinant]
    DetCalc --> DisplayDetValue[Display Determinant Value<br/>Integer/Decimal]
    DetCalc --> ShowSingular{det = 0?}
    ShowSingular -->|Yes| ShowSingularMsg[Show Singular Matrix Message]
    ShowSingular -->|No| ShowNonSingular[Show Non-Singular Message]
    
    Inverse --> InvInput[Input Square Matrix]
    InvInput --> InvMethod[Select Method:<br/>Adjugate/Gauss-Jordan]
    InvMethod --> CheckDet{Check if<br/>Determinant ≠ 0}
    CheckDet -->|Yes| CalcInverse[Calculate Inverse Matrix]
    CheckDet -->|No| ShowSingularError[Show Singular Matrix Error]
    CalcInverse --> DisplayInverse[Display Original + Inverse]
    DisplayInverse --> VerifyInv[Show Verification:<br/>A × A⁻¹ = I]
    
    Encrypt --> EncryptChoice{Choose Operation}
    EncryptChoice --> EncryptMsg[Encrypt Message]
    EncryptChoice --> DecryptMsg[Decrypt Message]
    
    EncryptMsg --> InputMsg[Input Text Message]
    InputMsg --> GenKey[Generate/Input<br/>Key Matrix n×n]
    GenKey --> ValidateKey{Validate Key<br/>det ≠ 0?}
    ValidateKey -->|No| ShowKeyError[Show Invalid Key Error]
    ValidateKey -->|Yes| ConvertText[Convert Text to Numbers<br/>A=1, B=2, ..., Space=29]
    ConvertText --> CreateMsgMatrix[Create Message Matrix]
    CreateMsgMatrix --> MatrixMult[Multiply:<br/>Key × Message]
    MatrixMult --> DisplayEncrypted[Display Encrypted Matrix<br/>+ Number Sequence]
    
    DecryptMsg --> InputEncrypted[Input Encrypted Numbers]
    InputEncrypted --> InputKeyDecrypt[Input Key Matrix]
    InputKeyDecrypt --> CalcKeyInverse[Calculate Key Inverse]
    CalcKeyInverse --> DecryptMult[Multiply:<br/>Key⁻¹ × Encrypted]
    DecryptMult --> ConvertToText[Convert Numbers to Text]
    ConvertToText --> DisplayDecrypted[Display Original Message]
    
    style Client fill:#e1f5ff
    style Menu fill:#fff4e1
    style SumSub fill:#e8f5e9
    style Scalar fill:#e8f5e9
    style Multiply fill:#e8f5e9
    style Det fill:#fff3e0
    style Inverse fill:#fff3e0
    style Encrypt fill:#f3e5f5
    style DisplayResult fill:#c8e6c9
    style ShowError fill:#ffcdd2
    style ShowSingularError fill:#ffcdd2
    style DisplayEncrypted fill:#d1c4e9
    style DisplayDecrypted fill:#d1c4e9