import numpy as np

# Definir a matriz A
A = np.array([
    [4, -2, -1],
    [-2, 3, 3],
    [-1, 3, 4]
], dtype=float)  # garante que A seja float

# Função para aplicar a Regra de Sarrus com passo a passo
def sarrus_step_by_step(matrix):
    a11, a12, a13 = matrix[0]
    a21, a22, a23 = matrix[1]
    a31, a32, a33 = matrix[2]

    # Diagonais principais (↘)
    dp1 = a11 * a22 * a33
    dp2 = a12 * a23 * a31
    dp3 = a13 * a21 * a32
    soma_principais = dp1 + dp2 + dp3

    # Diagonais secundárias (↙)
    ds1 = a13 * a22 * a31
    ds2 = a11 * a23 * a32
    ds3 = a12 * a21 * a33
    soma_secundarias = ds1 + ds2 + ds3

    resultado = soma_principais - soma_secundarias

    passos = {
        "diagonais_principais": {
            "dp1": f"{a11}*{a22}*{a33} = {dp1}",
            "dp2": f"{a12}*{a23}*{a31} = {dp2}",
            "dp3": f"{a13}*{a21}*{a32} = {dp3}",
            "soma": f"{dp1} + {dp2} + {dp3} = {soma_principais}"
        },
        "diagonais_secundarias": {
            "ds1": f"{a13}*{a22}*{a31} = {ds1}",
            "ds2": f"{a11}*{a23}*{a32} = {ds2}",
            "ds3": f"{a12}*{a21}*{a33} = {ds3}",
            "soma": f"{ds1} + {ds2} + {ds3} = {soma_secundarias}"
        },
        "resultado": f"{soma_principais} - {soma_secundarias} = {resultado}"
    }

    return passos

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

# Executar Sarrus
sarrus_explicado = sarrus_step_by_step(A)

print("=== REGRA DE SARRUS ===\n")
for passo, descricao in sarrus_explicado.items():
    print(f"{passo.upper()}:\n")
    if isinstance(descricao, dict):
        for chave, valor in descricao.items():
            print(f"{chave}: {valor}")
    else:
        print(descricao)
    print("\n")

# Executar Cholesky
try:
    G, explicacao_cholesky = cholesky_step_by_step(A)
    print("=== FATORAÇÃO DE CHOLESKY (A = GᵀG) ===\n")
    for chave, valor in explicacao_cholesky.items():
        print(f"{chave}: {valor}")
    print("\nMatriz G (triangular superior):\n", G)
    print("\nProva real (GᵀG):\n", G.T @ G)
    print("\nMatriz original A:\n", A)
    # Mostrar a matriz L (inferior)
    L = G.T
    print("\nMatriz L (triangular inferior):\n", L)
    # Verificação alternativa: A = LLᵀ
    print("\nVerificação A = L·Lᵀ:\n", L @ L.T)
except ValueError as e:
    print("\n❌ Erro na fatoração de Cholesky:")
    print(e)