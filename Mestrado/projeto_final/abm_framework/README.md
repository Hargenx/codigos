# ABM Framework

Framework simples e modular para simulações baseadas em agentes (Agent-Based Modeling - ABM), com suporte a paralelização e coleta de dados.

## Instalação

```bash
pip install -e .
```

## Uso

```python
from abm_framework import Agent, World, Simulation

# Criar o mundo
world = World()

# Criar os agentes
agentes = [Agent() for _ in range(10)]

# Criar a simulação
simulation = Simulation(world, agents)

# Executar a simulação
simulation.run()
```

```python
from abm.simulation import Simulacao
from examples.market_example import MundoMercado, AgenteFinanceiro

mundo = MundoMercado()
for i in range(50):
    mundo.adicionar_agente(AgenteFinanceiro(i))

simulacao = Simulacao(mundo, ciclos=100)
simulacao.executar()
```

---

### ✅ Progresso final

- [x] Estrutura modular
- [x] Agente generalista
- [x] Mundo generalista
- [x] Paralelização configurável
- [x] Exportação de dados
- [x] Exemplo funcional
- [x] Empacotamento como biblioteca com `setup.py`
- [x] Pronto para publicar no GitHub ou PyPI 🔥

---
