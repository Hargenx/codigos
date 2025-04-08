from simulation import Simulacao
from exemplo_basico_mercado import AgenteFinanceiro, MundoMercado

# Criar o mundo
mundo = MundoMercado()

# Adicionar agentes
for i in range(50):
    mundo.adicionar_agente(AgenteFinanceiro(id_agente=i, saldo_inicial=1000))

# Criar a simulação
simulacao = Simulacao(mundo=mundo, ciclos=100, paralelo=True)

# Executar a simulação
simulacao.executar()
