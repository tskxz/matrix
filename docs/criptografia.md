Sistema de criptografia/descriptografia de mensagens com álgebra linear, baseado em multiplicação matricial e matrizes inversas.

**Matriz Codificadora A:**

$$
A = \begin{bmatrix}
5 & 7 \\
2 & 3
\end{bmatrix}
$$


**Matriz Decodificadora B (inversa de A):**

$$
B = \begin{bmatrix}
3 & -7 \\
-2 & 5
\end{bmatrix}
$$


**Propriedade:** $A \times B = B \times A = I$

Operação: Criptografia de Mensagens

### Exemplo Completo:

**Mensagem Original:** "OS NUMEROS GOVERNAM O MUNDO."

1. **Converter para números usando a tabela:**

| Posição | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20| 21| 22| 23| 24| 25| 26| 27| 28|
|---------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Letra   | O | S | _ | N | U | M | E | R | O | S | _ | G | O | V | E | R | N | A | M | _ | O | _ | M | U | N | D | O | . |
| Número  | 15| 19| 29| 14| 21| 13| 5 | 18| 15| 19| 29| 7 | 15| 22| 5 | 18| 14| 1 | 13| 29| 15| 29| 13| 21| 14| 4 | 15| 27|




2. **Organizar em matriz M (2×14):**

$$
M = \begin{bmatrix}
15 & 19 & 29 & 14 & 21 & 13 & 5 & 18 & 15 & 19 & 29 & 7 & 15 & 22 \\
5 & 18 & 14 & 1 & 13 & 29 & 15 & 29 & 13 & 21 & 14 & 4 & 15 & 27
\end{bmatrix}
$$

3. **Multiplicar pela matriz codificadora A:**

$$
   N = A \times M
$$

 $$
   A = \begin{bmatrix}
   5 & 7 \\
   2 & 3
   \end{bmatrix}
   \quad
M = \begin{bmatrix}
   15 & 19 & 29 & 14 & 21 & 13 & 5 & 18 & 15 & 19 & 29 & 7 & 15 & 22 \\
   5 & 18 & 14 & 1 & 13 & 29 & 15 & 29 & 13 & 21 & 14 & 4 & 15 & 27
   \end{bmatrix}
$$

**Resultado:**

$$
   N = \begin{bmatrix}
   110 & 221 & 243 & 77 & 196 & 268 & 130 & 293 & 166 & 242 & 243 & 63 & 180 & 299 \\
   45 & 92 & 100 & 31 & 81 & 113 & 55 & 123 & 69 & 101 & 100 & 26 & 75 & 125
   \end{bmatrix}
$$

4. **Mensagem Criptografada:**
110,221,243,77,196,268,130,293,166,242,243,63,180,299,45,92,100,31,81,113,55,123,69,101,100,26,75,125
5. **Descriptografar (usando matriz B):**

$$
M = B \times N
$$

$$
B = \begin{bmatrix}
3 & -7 \\
-2 & 5
\end{bmatrix}
\quad
N = \begin{bmatrix}
110 & 221 & 243 & 77 & 196 & 268 & 130 & 293 & 166 & 242 & 243 & 63 & 180 & 299 \\
45 & 92 & 100 & 31 & 81 & 113 & 55 & 123 & 69 & 101 & 100 & 26 & 75 & 125
\end{bmatrix}
$$

**Resultado:**

$$
M = \begin{bmatrix}
15 & 19 & 29 & 14 & 21 & 13 & 5 & 18 & 15 & 19 & 29 & 7 & 15 & 22 \\
5 & 18 & 14 & 1 & 13 & 29 & 15 & 29 & 13 & 21 & 14 & 4 & 15 & 27
\end{bmatrix}
$$

Convertendo de volta para texto:
"OS NUMEROS GOVERNAM O MUNDO."