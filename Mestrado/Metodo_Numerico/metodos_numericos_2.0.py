import numpy as np

# Definir a matriz A
A = np.array([[7, 3], 
              [3, 5]], dtype=float)


# =============================
# Função para detalhamento do determinante
# =============================
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

        # Menor principal de ordem 1
        print("1️⃣ Menor principal de ordem 1:\n")
        print(f"det(A1) = {a11}\n")

        # Menor principal de ordem 2
        print("2️⃣ Menor principal de ordem 2:\n")
        det2 = a11 * a22 - a12 * a21
        print(f"det(A2) = {a11}*{a22} - {a12}*{a21} = {a11*a22} - {a12*a21} = {det2}\n")

        # Regra de Sarrus (ordem 3)
        print("3️⃣ Regra de Sarrus para matriz 3x3:\n")

        dp1 = a11 * a22 * a33
        dp2 = a12 * a23 * a31
        dp3 = a13 * a21 * a32
        soma_principais = dp1 + dp2 + dp3

        ds1 = a13 * a22 * a31
        ds2 = a11 * a23 * a32
        ds3 = a12 * a21 * a33
        soma_secundarias = ds1 + ds2 + ds3

        resultado = soma_principais - soma_secundarias

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

        print(
            f"Determinante final = {soma_principais} - {soma_secundarias} = {resultado}\n"
        )

        return resultado

    else:
        det = np.linalg.det(matrix)
        print("Matriz de ordem diferente de 2x2 ou 3x3. Usando numpy.linalg.det:")
        print(f"Determinante ≈ {det:.4f}\n")
        return det


# =============================
# Função para fatoração de Cholesky com passo a passo da matriz G (triangular superior)
# =============================
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
                    raise ValueError(
                        f"Não é possível aplicar Cholesky: valor negativo sob raiz quadrada (linha {i+1})"
                    )
                G[i][i] = np.sqrt(valor)
                explicacao[f"g{i+1}{i+1}"] = f"sqrt({A[i][i]} - {soma}) = {G[i][i]}"
            else:
                G[i][j] = (A[j][i] - soma) / G[i][i]
                explicacao[f"g{i+1}{j+1}"] = (
                    f"({A[j][i]} - {soma}) / {G[i][i]} = {G[i][j]}"
                )

    return G, explicacao


# =============================
# Execução principal
# =============================

# Mostra determinante com todos os passos
det = mostrar_determinante(A)

# Executar Cholesky
try:
    G, explicacao_cholesky = cholesky_step_by_step(A)

    print("=== FATORAÇÃO DE CHOLESKY - MATRIZ G (Triangular Superior) ===\n")
    for chave, valor in explicacao_cholesky.items():
        print(f"{chave}: {valor}")

    print("\nMatriz G (triangular superior):\n", G)

    # Matriz L (triangular inferior) como a transposta de G
    L = G.T
    print("\n=== MATRIZ L (Triangular Inferior) ===")
    print(
        "Nota: Como estamos calculando G, obtemos L como a transposta de G (L = Gᵀ).\n"
    )
    print("Matriz L (triangular inferior):\n", L)

    # Provas reais
    print("\n=== PROVAS REAIS ===\n")
    print("Prova real (Gᵀ · G):\n", G.T @ G)
    print("Prova real (L · Lᵀ):\n", L @ L.T)
    print("\nMatriz original A:\n", A)

    # Determinante via Cholesky
    detG = np.prod(np.diag(G))
    detA = detG**2
    print("\nDeterminante via Cholesky:")
    print(f"det(G) = {detG}")
    print(f"det(A) = (det(G))² = ({detG})² = {detA}")

except ValueError as e:
    print("\n❌ Erro na fatoração de Cholesky:")
    print(e)
