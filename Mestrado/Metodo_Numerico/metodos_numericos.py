import numpy as np

# Definir a matriz A
A = np.array([
    [6, 3, 1],
    [3, 5, 2],
    [1, 2, 4]
], dtype=float)

def mostrar_determinante(matrix):
    shape = matrix.shape
    print("=== DETALHAMENTO DO DETERMINANTE ===\n")

    if shape == (2, 2):
        a11, a12 = matrix[0]
        a21, a22 = matrix[1]
        det = a11 * a22 - a12 * a21
        print("Regra para matriz 2x2:\n")
        print(f"det(A) = {a11}*{a22} - {a12}*{a21} = {a11*a22} - {a12*a21} = {det}\n")
        return det

    elif shape == (3, 3):
        a11, a12, a13 = matrix[0]
        a21, a22, a23 = matrix[1]
        a31, a32, a33 = matrix[2]

        dp1 = a11 * a22 * a33
        dp2 = a12 * a23 * a31
        dp3 = a13 * a21 * a32
        soma_principais = dp1 + dp2 + dp3

        ds1 = a13 * a22 * a31
        ds2 = a11 * a23 * a32
        ds3 = a12 * a21 * a33
        soma_secundarias = ds1 + ds2 + ds3

        resultado = soma_principais - soma_secundarias

        print("Regra de Sarrus para matriz 3x3:\n")
        print("↘ Diagonais principais:")
        print(f"dp1: {a11}*{a22}*{a33} = {dp1}")
        print(f"dp2: {a12}*{a23}*{a31} = {dp2}")
        print(f"dp3: {a13}*{a21}*{a32} = {dp3}")
        print(f"Soma principais: {dp1} + {dp2} + {dp3} = {soma_principais}\n")

        print("↙ Diagonais secundárias:")
        print(f"ds1: {a13}*{a22}*{a31} = {ds1}")
        print(f"ds2: {a11}*{a23}*{a32} = {ds2}")
        print(f"ds3: {a12}*{a21}*{a33} = {ds3}")
        print(f"Soma secundárias: {ds1} + {ds2} + {ds3} = {soma_secundarias}\n")

        print(f"Determinante = {soma_principais} - {soma_secundarias} = {resultado}\n")
        return resultado

    else:
        det = np.linalg.det(matrix)
        print("Matriz de ordem diferente de 2x2 ou 3x3. Usando numpy.linalg.det:")
        print(f"Determinante ≈ {det:.4f}\n")
        return det


# Função para fatoração de Cholesky com passo a passo
def cholesky_step_by_step(A):
    n = A.shape[0]
    G = np.zeros((n, n), dtype=float)
    explicacao = {}

    for i in range(n):
        for j in range(i, n):
            soma = sum(G[k][i] * G[k][j] for k in range(i))
            if i == j:
                valor = A[i][i] - soma
                if valor <= 0:
                    raise ValueError(f"Não é possível aplicar Cholesky: valor negativo sob raiz quadrada (linha {i+1})")
                G[i][i] = np.sqrt(valor)
                explicacao[f"g{i+1}{i+1}"] = f"sqrt({A[i][i]} - {soma}) = {G[i][i]}"
            else:
                G[i][j] = (A[i][j] - soma) / G[i][i]
                explicacao[f"g{i+1}{j+1}"] = f"({A[i][j]} - {soma}) / {G[i][i]} = {G[i][j]}"
    
    return G, explicacao

det = mostrar_determinante(A)

# Executar Cholesky
try:
    G, explicacao_cholesky = cholesky_step_by_step(A)
    print("=== FATORAÇÃO DE CHOLESKY (A = GᵀG) ===\n")
    for chave, valor in explicacao_cholesky.items():
        print(f"{chave}: {valor}")

    print("\nMatriz G (triangular superior):\n", G)

    # Matriz L (triangular inferior)
    L = G.T
    print("\nMatriz L (triangular inferior):\n", L)

    # Provas reais
    print("\nProva real (GᵀG):\n", G.T @ G)
    print("Prova real (LLᵀ):\n", L @ L.T)
    print("\nMatriz original A:\n", A)

    # Determinante via Cholesky
    detG = np.prod(np.diag(G))
    detA = detG ** 2
    print(f"\nDeterminante via Cholesky:\n")
    print(f"det(G) = {detG}")
    print(f"det(A) = (det(G))² = ({detG})² = {detA}")

except ValueError as e:
    print("\n❌ Erro na fatoração de Cholesky:")
    print(e)