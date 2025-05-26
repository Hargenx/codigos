# 📚 **Apresentação Técnica — Evolução do Simulador de Mercado para Framework ABM Modular**

---

## **1. Introdução**

### Contextualização do Projeto

O projeto iniciou-se como um simulador de mercado financeiro com agentes que compravam e vendiam ativos.
A proposta inicial era criar uma simulação utilizando técnicas de modelagem baseada em agentes (ABM), onde cada agente representa um participante do mercado.

### Objetivo das Melhorias

Transformar o simulador de mercado em uma **framework modular e escalável de ABM**, capaz de ser reutilizada para diferentes contextos além do mercado financeiro, incluindo:

- Generalização de agentes e ambientes
- Paralelização do processamento
- Estrutura modular e empacotável
- Exportação e análise de dados
- Pronto para publicação e expansão

---

## **2. Evolução da Arquitetura**

### Situação inicial

- 🎯 Simulador específico de mercado financeiro
- 🔄 Execução sequencial
- 📁 Código monolítico (tudo num notebook único)
- ❌ Sem modularização
- ❌ Sem coleta estruturada de dados
- ❌ Sem possibilidade de reutilização geral

### Situação atual

- ✅ Estrutura modularizada em múltiplos arquivos
- ✅ Agente generalista (`AgenteBase`)
- ✅ Mundo generalista (`MundoBase`)
- ✅ Execução paralela com `ThreadPoolExecutor`
- ✅ Exportação automática de resultados (JSON)
- ❌ Empacotável como biblioteca Python
- ❌ Pronto para outros cenários ABM

---

## **3. Nova Estrutura de Diretórios**

```bash
abm_framework/
│
├── abm/                    # Módulo principal do framework
│   ├── __init__.py
│   ├── agent.py            # Agente base
│   ├── world.py            # Mundo base
│   ├── simulation.py       # Motor da simulação + paralelização
│   ├── collector.py        # Coletor de dados (em evolução)
│   └── utils.py            # Utilitários gerais (logger, medição de tempo)
│
├── examples/
│   └── market_example.py   # Exemplo usando a framework (mercado financeiro)
│
├── tests/                  # Testes unitários (próximos passos)
│
├── setup.py                # Empacotamento como biblioteca
├── README.md               # Documentação de uso
└── requirements.txt        # Dependências
```

---

## **4. Componentes Criados**

### `AgenteBase (agent.py)`

- Define a estrutura geral de um agente.
- Pode ser estendido para qualquer tipo de simulação.

### `MundoBase (world.py)`

- Gerencia agentes e recursos do ambiente.
- Centraliza atualizações e coleta de dados.

### `Simulacao (simulation.py)`

- Controla o loop da simulação.
- Permite execução paralela configurável.

### `Utils (utils.py)`

- Medição de tempo e funções auxiliares.

### Exemplo de Mercado (market_example.py)

- Demonstra como implementar um caso específico usando a framework.

### Exportação de resultados

- Coleta e exporta dados da simulação automaticamente para JSON.

---

## **5. Foco na Generalização**

Um dos maiores ganhos foi a **generalização** das estruturas:

- O código da simulação não está mais acoplado ao modelo de mercado financeiro.
- Agentes e ambientes são abstraídos, permitindo:
  - Simulações de mercados
  - Simulações de logística
  - Simulações de saúde pública
  - E muitos outros cenários

---

## **6. Paralelização Implementada**

Implementamos **paralelização com ThreadPoolExecutor**, permitindo escalabilidade:

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=None) as executor:
    executor.map(lambda agente: processar_agente(agente, ambiente), agentes)
```

Benefícios:

- Simulações mais rápidas com grandes volumes de agentes
- Melhor uso de CPU
- Flexibilidade para definir número de threads

Próximo passo possível:

- Uso de `ProcessPoolExecutor` para workloads CPU-bound ainda mais pesados.

---

## **7. Coleta de Dados e Exportação**

Automatizamos a coleta de dados:

- Snapshot do estado do mundo e dos agentes a cada ciclo.
- Exportação em formato JSON pronta para análise.

Exemplo de estrutura exportada:

```json
{
    "tempo": 1,
    "estado_mundo": {"compras": 10, "vendas": 5},
    "estado_agentes": [
        {"id": 0, "recursos": {"saldo": 1000, "ativos": {}}},
        ...
    ]
}
```

Próximo passo:

- Exportação adicional para CSV ou integração com Pandas.

---

## **8. Empacotamento como Biblioteca**

Criamos um arquivo `setup.py` para transformar a framework em biblioteca Python.

Instalação local:

```bash
pip install -e .
```

Preparação para distribuição:

- GitHub
- PyPI (Python Package Index)

Próximo passo:

- Publicação oficial como pacote Python!

---

## **9. Roadmap Futuro**

✔️ Estrutura modular finalizada  
✔️ Paralelização básica implementada  
✔️ Coleta de dados automatizada  
✔️ Exemplo funcional completo  

🔜 Próximos aprimoramentos:

- Integração com Pandas e visualização dos resultados
- Adição de testes unitários
- Publicação no PyPI
- Suporte a diferentes motores de execução (threading / multiprocessing)
- Interface gráfica com Streamlit ou Dash para simulações interativas
- Geração automática de relatórios PDF/HTML

---

## **10. Conclusão**

A evolução do projeto transformou um simulador pontual em uma **framework simulações ABM**.

- 🔧 Um ambiente de desenvolvimento limpo e modular.
- 🚀 Potencial de escalabilidade para grandes simulações.
- 📦 Pronto para publicação como pacote reutilizável.
- 📊 Estrutura de coleta e análise de dados integrada.
