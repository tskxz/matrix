Análise de sistema  
Authors: Tanjil Khan, Dmytro Bohutsky, Luís Martins, Ricardo Magalhães  
Date: 01/19/2026  

## Requisitos funcionais
O sistema deve ter as seguintes funcionalidades:
##### RF01 – Introdução de Matrizes
O sistema deve permitir ao utilizador introduzir matrizes de dimensão variável, definindo explicitamente o número de linhas e colunas, bem como os respetivos valores reais.

##### RF02 – Soma de Matrizes
O sistema deve permitir a soma de duas matrizes 

##### RF03 – Subtração de Matrizes
O sistema deve permitir a subtração de duas matrizes 

##### RF04 – Multiplicação de Matriz por Escalar
O sistema deve permitir a multiplicação de uma matriz 

##### RF05 – Multiplicação de Matrizes
O sistema deve permitir a multiplicação de duas matrizes 

##### RF06 – Cálculo do Determinante
O sistema deve calcular o determinante de uma matriz quadrada:
	- Matrizes de ordem superior através da expansão por cofatores
	- Caso a matriz não seja quadrada, o sistema deve informar o utilizador.

##### RF07 – Cálculo da Matriz Inversa
O sistema deve calcular a matriz inversa de uma matriz quadrada, desde que o determinante seja diferente de zero.
Caso contrário, o sistema deve apresentar uma mensagem de erro adequada.

##### RF08 – Conversão de Texto para Matriz Numérica
O sistema deve converter uma mensagem de texto numa matriz numérica com base numa tabela de codificação pré-definida (A=1, B=2, …, Z=26, sinais especiais).

##### RF09 – Criptografia de Mensagens
O sistema deve permitir a criptografia de mensagens através da multiplicação da matriz da mensagem por uma matriz de codificação.

##### RF10 – Descriptografia de Mensagens
O sistema deve permitir a recuperação da mensagem original através da multiplicação da matriz criptografada pela matriz inversa de decodificação.

##### RF11 – Validação de Dados
O sistema deve validar:
- Dimensões das matrizes
- Valores numéricos introduzidos
- Condições matemáticas necessárias para cada operação

## Requisitos não funcionais

##### RNF01 – Desempenho
O sistema deve executar operações matriciais de pequena e média dimensão num tempo de resposta inferior a 1 segundo, garantindo fluidez na interação com o utilizador.

##### RNF02 – Usabilidade
O sistema deve apresentar uma interface simples e intuitiva, permitindo que utilizadores com conhecimentos básicos de matemática consigam realizar operações sem dificuldade.

##### RNF03 – Fiabilidade
O sistema deve garantir resultados matematicamente corretos, respeitando rigorosamente as definições formais das operações matriciais.

##### RNF04 – Segurança dos Dados
O sistema não deve armazenar permanentemente mensagens introduzidas para criptografia, garantindo a confidencialidade dos dados do utilizador durante a execução.

##### RNF05 – Robustez
O sistema deve lidar corretamente com erros, como:
    - Matrizes incompatíveis
    - Determinantes nulos
    - Introdução de dados inválidos
    - Apresentar mensagens claras ao utilizador.

##### RNF06 – Escalabilidade
O sistema deve ser projetado de forma a permitir, no futuro, a adição de novas operações matemáticas ou métodos de criptografia sem necessidade de reestruturação profunda.

##### RNF07 – Conformidade
O sistema deve respeitar boas práticas de desenvolvimento de software e normas académicas, garantindo clareza, organização e manutenção do código.

### Casos de uso
![casos_uso](./assets/casos_uso.png)

### Diagrama de classes
Neste diagrama, representamos a estrutura e relações da classe Matriz:
![diagrama_classes](./assets/matrix_class.png)

### Diagrama de sequências
O seguinte diagrama mostra a sequência dos processos e a estrutura do nossso projeto:
![diagrama_sequencia](./assets/Sequence_Diagram.png)

### Fluxograma - unit test
O seguinte fluxograma descreve como seria o fluxo enquanto se executa os testes:
![fluxograma_unittest](./assets/unit_tests_diagram.png)