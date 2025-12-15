# Matrix

Uma calculadora para operações com matrizes, desenvolvida como projeto interdisciplinar focado em Álgebra Linear e Matemática.

---

## Operações Implementadas

### 1. Soma e Subtração de Matrizes

$$
C = A \pm B
$$

onde

$$
c_{ij} = a_{ij} \pm b_{ij}
$$

**Condição:**

$$
A, B \in \mathbb{R}^{m \times n}
$$

---

### 2. Multiplicação por Escalar

$$
B = k \cdot A
$$

onde

$$
b_{ij} = k \cdot a_{ij}
$$

**Exemplo:**

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix},
\quad
k = 3
$$

$$
3A =
\begin{bmatrix}
3 & 6 \\
9 & 12
\end{bmatrix}
$$

---

### 3. Multiplicação de Matrizes

$$
C = A \cdot B
$$

onde

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj}
$$

**Condição:**

$$
\text{colunas}(A) = \text{linhas}(B)
$$

---

### 4. Determinante de Matriz

- Para matriz $1 \times 1$:

$$
\det(A) = a
$$

- Para matriz $2 \times 2$:

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\Rightarrow
\det(A) = ad - bc
$$

- Caso geral (expansão por cofatores):

$$
\det(A) = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} M_{ij}
$$

**Condição:**

$$
A \in \mathbb{R}^{n \times n}
$$

---

### 5. Matriz Inversa

$$
A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)
$$

**Condições:**

- $A$ é quadrada  
- $\det(A) \neq 0$

**Exemplo (2×2):**

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\Rightarrow
A^{-1} =
\frac{1}{ad - bc}
\begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix}
$$

---

## Criptografia com Matrizes

### Matrizes de Codificação e Decodificação

$$
A =
\begin{bmatrix}
5 & 7 \\
2 & 3
\end{bmatrix},
\quad
B = A^{-1} =
\begin{bmatrix}
3 & -7 \\
-2 & 5
\end{bmatrix}
$$

**Verificação:**

$$
A \cdot B = B \cdot A = I
$$

---

### Tabela de Codificação

$$
\begin{aligned}
A=1 &\quad B=2 &\quad C=3 &\quad \dots &\quad Z=26 \\
.=27 &\quad ,=28 &\quad \_=29 &\quad -=30
\end{aligned}
$$

---

### Exemplo de Criptografia

**Mensagem:**

OS NUMEROS GOVERNAM O MUNDO.

**Conversão para números:**

$$
15,19,29,14,21,13,5,18,15,19,29,7,15,22,5,18,14,1,13,29,15,29,13,21,14,4,15,27
$$

---

### Matriz da Mensagem $M$

$$
M =
\begin{bmatrix}
15 & 19 & 29 & 14 & 21 & 13 & 5 & 18 & 15 & 19 & 29 & 7 & 15 & 22 \\
5 & 18 & 14 & 1 & 13 & 29 & 15 & 29 & 13 & 21 & 14 & 4 & 15 & 27
\end{bmatrix}
$$

---

### Criptografia

$$
N = A \cdot M
$$

$$
N =
\begin{bmatrix}
110 & 221 & 243 & 77 & 196 & 268 & 130 & 293 & 166 & 242 & 243 & 63 & 180 & 299 \\
45 & 92 & 100 & 31 & 81 & 113 & 55 & 123 & 69 & 101 & 100 & 26 & 75 & 125
\end{bmatrix}
$$

**Mensagem criptografada:**  

110,221,243,77,196,268,130,293,166,242,243,63,180,299,
45,92,100,31,81,113,55,123,69,101,100,26,75,125
---

### Descriptografia

$$
M = B \cdot N
$$

Resultado: **matriz original da mensagem**


### Comandos para rodar o Programa
git clone https://github.com/tskxz/matrix.git
pip3 install -r requirements.txt
python app.py