# Plano de Estudo Intensivo (até Quinta de Manhã)

## **Dia 1 – Fundamentos e Métodos Diretos**

**Manhã: Revisão dos Fundamentos**  

- **Álgebra Linear e Sistemas Lineares:**
  - Revise operações com matrizes, cálculo de determinantes e condições de existência/uniqueness.
  - Anote fórmulas essenciais para consultas rápidas.

**Tarde: Métodos Diretos**  

- **Eliminação de Gauss:**  
  - Estude o procedimento, focando na escolha dos pivôs e na organização das operações.
- **Fatoração LU e Cholesky:**  
  - Compreenda como decompor a matriz e use as substituições progressiva e retroativa.
- **Dica para o Papel:** Utilize “checklists” para registrar cada etapa e minimizar erros.

**Noite: Exercícios Práticos**  

- Resolva alguns problemas simples para fixar os métodos diretos.
- Revise as anotações e reforce os conceitos com exemplos práticos.

---

### **Dia 2 – Métodos Iterativos e Integração Numérica**

**Manhã: Métodos Iterativos**  

- **Revisão de Conceitos:**  
  - Entenda os critérios de convergência e as condições (como diagonal dominante).
- **Método de Jacobi e Gauss-Seidel:**  
  - Estude os passos de cada método e compare a atualização simultânea versus sequencial.
- **Método SOR (opcional):**  
  - Veja a introdução do fator de relaxação e como ele pode acelerar a convergência.

**Tarde: Integração Numérica**  

- **Fórmulas Básicas:**  
  - Revise a regra do trapézio e a regra de Simpson.  
  - Entenda as condições de aplicação e as fórmulas de erro associadas.
- **Exemplos Práticos:**  
  - Resolva integrais simples “no papel”, anotando cada etapa e os cálculos aproximados.
- **Dica para o Papel:** Anote as fórmulas essenciais em um resumo rápido para facilitar a consulta durante a resolução dos exercícios.

**Noite: Revisão e Consolidação**  

- Revise os tópicos do dia (tanto métodos iterativos quanto integração numérica) e resolva exercícios mistos que integrem os conceitos.

---

### **Dia 3 – Revisão Geral e Simulação**

**Manhã/Tarde: Revisão Integrada**  

- **Integração dos Tópicos:**  
  - Releia os resumos e “checklists” dos métodos diretos, iterativos e integração numérica.
  - Compare as vantagens e peculiaridades de cada método e técnica.

**Final do Dia: Simulação de Prova**  

- Resolva um problema completo (ou questões diversas) como se estivesse na prova.
- Cronometre-se para praticar a gestão do tempo e identifique possíveis dúvidas para revisão final.

---

### **Dia 4 – Quinta de Manhã: Revisão Rápida e Preparação Final**

- **Revisão dos Pontos-Chave:**  
  - Consulte os resumos e listas de fórmulas dos métodos diretos, iterativos e integração numérica.
- **Organize seu Material:**  
  - Tenha à mão seus “checklists”, anotações e exemplos práticos.
- **Calma e Foco:**  
  - Faça uma revisão mental ou rápida resolução de um exemplo simples para “aquecer” o raciocínio antes da prova.

## **Matrizes: Definições e Propriedades Básicas**

1. **Definição de Matriz:**
   - Uma **matriz** é um arranjo retangular de números organizado em linhas e colunas.
   - Uma matriz \( A \) de ordem \( m \times n \) possui \( m \) linhas e \( n \) colunas, e seus elementos são denotados por \( a_{ij} \), onde \( i \) é o índice da linha e \( j \) o da coluna.

2. **Operações com Matrizes:**

   - **Adição:**
     - **Condição:** Somente é possível somar duas matrizes se elas tiverem as mesmas dimensões.
     - **Definição:** Se \( A = [a_{ij}] \) e \( B = [b_{ij}] \) são matrizes de mesmo tamanho, então a soma \( A + B \) é dada por:
       \[
       (A+B)_{ij} = a_{ij} + b_{ij}
       \]
     - **Propriedades:**  
       - **Comutativa:** \( A + B = B + A \)
       - **Associativa:** \( (A+B)+C = A+(B+C) \)

   - **Multiplicação:**
     - **Condição:** Para multiplicar duas matrizes, o número de colunas da primeira deve ser igual ao número de linhas da segunda. Se \( A \) é \( m \times n \) e \( B \) é \( n \times p \), então o produto \( AB \) é uma matriz \( m \times p \).
     - **Definição:** O elemento \( (AB)_{ij} \) é calculado como:
       \[
       (AB)_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj}
       \]
     - **Propriedades:**  
       - **Associativa:** \( A(BC) = (AB)C \)
       - **Distributiva:** \( A(B+C) = AB + AC \) e \( (A+B)C = AC + BC \)
       - **Não Comutativa:** Em geral, \( AB \neq BA \).

   - **Transposição:**
     - **Definição:** A **transposta** de uma matriz \( A \), denotada por \( A^T \), é obtida trocando suas linhas por colunas. Se \( A \) é \( m \times n \), então \( A^T \) é \( n \times m \).
     - **Propriedades:**  
       - \( (A^T)^T = A \)
       - \( (A+B)^T = A^T + B^T \)
       - \( (AB)^T = B^T A^T \)

   - **Inversão:**
     - **Definição:** A matriz inversa \( A^{-1} \) de uma matriz \( A \) (apenas definida se \( A \) for quadrada e não-singular, ou seja, \( \det(A) \neq 0 \)) é a matriz que satisfaz:
       \[
       A \cdot A^{-1} = I
       \]
       onde \( I \) é a matriz identidade.
     - **Propriedades:**  
       - \( (A^{-1})^{-1} = A \)
       - \( (AB)^{-1} = B^{-1}A^{-1} \) (para matrizes inversíveis \( A \) e \( B \))

3. **Propriedades Importantes:**
   - **Associatividade:**  
     - Para adição: \( (A+B)+C = A+(B+C) \)  
     - Para multiplicação: \( A(BC) = (AB)C \)
   - **Distributividade:**  
     - \( A(B+C) = AB + AC \)  
     - \( (A+B)C = AC + BC \)
   - **Comutatividade (na adição):**  
     - \( A+B = B+A \)  
     - _Nota:_ A multiplicação de matrizes, em geral, **não é** comutativa.

Esse conjunto de definições e propriedades forma a base para o entendimento e manipulação de matrizes, sendo essencial para avançar em temas como métodos diretos, iterativos, e outras aplicações em álgebra linear e análise numérica.
