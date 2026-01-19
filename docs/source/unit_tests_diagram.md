graph TD
    Start([Run Unit Tests]) --> TestCreation[Test Matrix Creation]
    
    TestCreation --> TC1[Create with data]
    TestCreation --> TC2[Create zeros]
    TestCreation --> TC3[Invalid dimensions]
    
    TC1 --> TestElements[Test Matrix Elements]
    TC2 --> TestElements
    TC3 --> TestElements
    
    TestElements --> TE1[Get/Set elements]
    TestElements --> TE2[Check dimensions]
    TestElements --> TE3[Is square?]
    
    TE1 --> TestBasic[Test Basic Operations]
    TE2 --> TestBasic
    TE3 --> TestBasic
    
    TestBasic --> TBA[Addition 2×2, 3×3]
    TestBasic --> TBS[Subtraction 2×2, 3×3]
    TestBasic --> TBSc[Scalar ×2, ×0, ×-1]
    TestBasic --> TBErr[Dimension errors]
    
    TBA --> TestMultiply[Test Multiplication]
    TBS --> TestMultiply
    TBSc --> TestMultiply
    TBErr --> TestMultiply
    
    TestMultiply --> TM1[2×2 × 2×2]
    TestMultiply --> TM2[2×3 × 3×2]
    TestMultiply --> TM3[Identity property]
    TestMultiply --> TM4[Incompatible error]
    
    TM1 --> TestDet[Test Determinant]
    TM2 --> TestDet
    TM3 --> TestDet
    TM4 --> TestDet
    
    TestDet --> TD1[1×1, 2×2, 3×3]
    TestDet --> TD2[Zero det singular]
    TestDet --> TD3[Non-square error]
    
    TD1 --> TestTranspose[Test Transpose]
    TD2 --> TestTranspose
    TD3 --> TestTranspose
    
    TestTranspose --> TT1[2×2 square]
    TestTranspose --> TT2[3×2 rectangular]
    
    TT1 --> TestInverse[Test Inverse]
    TT2 --> TestInverse
    
    TestInverse --> TI1[2×2 invertible]
    TestInverse --> TI2[3×3 invertible]
    TestInverse --> TI3[Verify A × A⁻¹ = I]
    TestInverse --> TI4[Singular error]
    TestInverse --> TI5[Non-square error]
    
    TI1 --> TestEncrypt[Test Encryption]
    TI2 --> TestEncrypt
    TI3 --> TestEncrypt
    TI4 --> TestEncrypt
    TI5 --> TestEncrypt
    
    TestEncrypt --> TEn1[Setup encoding matrix]
    TestEncrypt --> TEn2[Encrypt message]
    TestEncrypt --> TEn3[Decrypt message]
    TestEncrypt --> TEn4[Verify inverse matrices]
    TestEncrypt --> TEn5[Round-trip test]
    
    TEn1 --> End([All Tests Complete])
    TEn2 --> End
    TEn3 --> End
    TEn4 --> End
    TEn5 --> End
    
    style Start fill:#e1f5ff
    style TestCreation fill:#fff4e1
    style TestElements fill:#e8f5e9
    style TestBasic fill:#f3e5f5
    style TestMultiply fill:#ffe0b2
    style TestDet fill:#fff9c4
    style TestTranspose fill:#e1bee7
    style TestInverse fill:#ffccbc
    style TestEncrypt fill:#c5cae9
    style End fill:#c8e6c9