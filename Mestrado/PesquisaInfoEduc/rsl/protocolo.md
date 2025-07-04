# Protocolo de Revisão Sistemática

## 1. Título e Objetivo

**Título:**  
Revisão Sistemática sobre a Aplicação de Modelos ABM em Simulações de Investimentos no Mercado Financeiro

**Objetivo Geral:**  
Identificar metodologias, estratégias de modelagem e validação empírica utilizadas em simulações de investimentos no mercado financeiro, e identificar lacunas na literatura.

> “Quais metodologias e aplicações de modelos ABM têm sido utilizadas em simulações de investimentos no mercado financeiro no período de 2015 a 2025, e quais lacunas metodológicas ainda persistem na literatura?”

---

## 2. Critérios de Inclusão e Exclusão

1. **Período de Publicação:**

   * “Publicações entre 2015 e 2024 (inclusive).”

2. **Tipo de Publicação:**

   * anais de conferências, artigos de periódicos ou estudos empíricos inclui apenas conferências indexadas em bases como Scopus/IEEE Xplore, ou se aceita também eventos regionais não indexados.

3. **Critérios de Exclusão:**

   * Estudos empíricos que não descrevem a estrutura do modelo ABM (isto é, apenas utilizam o termo ABM sem detalhar a implementação) serão excluídos.
   * Trabalhos aplicados a outros setores (ex.: saúde, logística) serão excluídos.

---

## 3. Estratégia de Busca

**Pontos fortes:**

* As bases de dados serão Web of Science, Scopus e IEEE Xplore.
* Os termos principais (“Agent-Based Modeling”, “ABM” etc.) cobrem a terminologia-chave.

**Detalhamento adicional:**

1. **Strings de Busca por Base de Dados:**

   * Cada base possui sintaxe ligeiramente diferente. Por exemplo:

   **Web of Science**

   ```code
   TS=("Agent-Based Modeling" OR "ABM") 
   AND TS=("financial market" OR "market simulation" OR "investment strategies" OR "market microstructure")
   AND PY=(2015–2024)
   AND LA=(English OR Portuguese)
   ```

   **Scopus**

   ```code
   TITLE-ABS-KEY("Agent-Based Modeling" OR "ABM") 
   AND TITLE-ABS-KEY("financial market" OR "market simulation" OR "investment strategies" OR "market microstructure")
   AND PUBYEAR > 2014 AND PUBYEAR < 2025
   AND (LIMIT-TO(LANGUAGE, "English") OR LIMIT-TO(LANGUAGE, "Portuguese"))
   ```

   **IEEE Xplore**

   ```code
   ("Agent-Based Modeling" OR "ABM") 
   AND ("financial market" OR "market simulation" OR "investment strategies" OR "market microstructure")
   Filter: Year: 2015-2024; Language: English, Portuguese
   ```

   **SSRN**

   ```code
   Abstract:("Agent-Based Modeling" OR "ABM") 
   AND Abstract:("financial market" OR "investment strategies" OR "market microstructure")
   Date: 01/01/2015 – 31/12/2024
   ```

2. **Registro das Datas de Busca:**

   * Há uma planilha e uma tabela indicando:

     * Data exata da busca em cada base (por exemplo, “Web of Science – 15/05/2025”).
     * String completa utilizada.
     * Número total de resultados brutos retornados e, depois, número após aplicação de filtros de idioma/ano.

3. **Uso de Filtros Automáticos:**

   * Sempre que possível, ative filtros internos das bases (por ano, idioma, área temática).
   * Documente se o filtro engloba artigos “in press” ou “aceitos” (sobressair se incluir ou não).

---

## 4. Métodos de Seleção e Triagem

**Pontos fortes:**

* Divisão em triagem inicial (título/resumo) e completa (texto integral).
* Indicação de ferramentas (Rayyan, Covidence).

**Aprimoramentos possíveis:**

1. **Fluxograma PRISMA:**

   * Antecipe a criação do fluxograma (PRISMA Flow Diagram), detalhando estimativas de números (por exemplo: “Estima-se encontrar 5 registros na Scopus, 4 na Web of Science, etc.”). Mesmo que sejam estimativas, o protocolo deve indicar as etapas do diagrama:

     1. Identificação (número bruto de registros).
     2. Remoção de duplicatas.
     3. Triagem de títulos/ resumos.
     4. Avaliação de elegibilidade (texto completo).
     5. Incluídos na síntese.
2. **Documentação de Duplicatas:**

   * Descreva como será o processo de deduplicação (por exemplo, primeiro com ferramenta automática do Rayyan; depois, remoção manual de casos ambíguos).
3. **Critérios de Avaliação na Triagem Completa:**

   * Crie um formulário padronizado (dentro do Rayyan ou em planilha) com marcações tipo:

     * [ ] Estudo ABM descrito detalhadamente?
     * [ ] Simula explicitamente estratégia de investimento?
     * [ ] Validação empírica (dados reais ou comparações)?
     * [ ] Contexto de mercado identificado (Bolsa específica, ativos, etc.)?
   * Isso ajuda a tornar o processo mais objetivo e mensurável.

---

## 5. Extração e Análise dos Dados

**Pontos fortes:**

* Colunas bem definidas (autor, ano, metodologia ABM, tipo de mercado, etc.).
* Uso de checklists (CASP e PRISMA).

**Detalhamento adicional:**

1. **Modelo de Planilha de Extração:**

   * Recomendo criar previamente a planilha (por exemplo, em Google Sheets ou Excel) com cabeçalhos e exemplos fictícios preenchidos para guiar quem for extrair. Assim:

   | Autor(es)     | Ano  | Título do Estudo                          | Objetivos                                           | Tipo de ABM (topologia, decison rules)     | Ferramentas/linguagem | Ativos/mercado simulado | Estratégias modeladas               | Principais resultados                        | Limitações/Avaliação qualitativa                         |
   | ------------- | ---- | ----------------------------------------- | --------------------------------------------------- | ------------------------------------------ | --------------------- | ----------------------- | ----------------------------------- | -------------------------------------------- | -------------------------------------------------------- |
   | Silva & Souza | 2018 | “Agent-Based Trading in Emerging Markets” | Avaliar impacto de especuladores em bolsa do Brasil | Agentes heterogêneos; redes de comunicação | NetLogo               | B3 (IBOV)               | Estratégias momentum vs. contrarian | Momentum causou bolhas de preço na simulação | Amostra de parâmetros pequena; não valida em dados reais |
   | …             | …    | …                                         | …                                                   | …                                          | …                     | …                       | …                                   | …                                            | …                                                        |

2. **Campos Extras (se aplicável):**

   * **Tipo de Validação:** Se houve comparação com dados reais ou validação estatística.
   * **Fonte dos Parâmetros:** Como definiram valores de volatilidade, volume de negociação, tamanho dos lotes, etc.
   * **Ferramentas e Plataformas:** Ex.: NetLogo, Repast, Python + Mesa, Matlab, etc.

3. **Avaliação de Qualidade Metodológica:**

   * Para cada artigo, descreva brevemente:

     * Se há descrição completa das regras de decisão dos agentes (transparência no modelo).
     * Se existe verificação de robustez (por exemplo, análise de sensibilidade dos parâmetros).
   * Você pode atribuir notas (p.ex., de 0 a 1) para aspectos como “transparência do modelo”, “validação empírica”, “reprodutibilidade” e “clareza na descrição das equações”.

---

## 6. Métodos de Análise dos Dados

**Aspectos positivos:**

* Separação clara entre análise qualitativa e quantitativa.
* Menciona uso de Python para análise.

**Sugestões:**

1. **Síntese Narrativa:**

   * Crie categorias temáticas específicas, por exemplo:

     1. **Arquitetura dos agentes** (ex.: agentes fundamentalistas vs. chartistas, agentes zero-intelligence, etc.);
     2. **Topologias de interação** (rede completa, vizinhança local, market-making centralizado);
     3. **Métricas de saída** (volatilidade gerada, formação de bolhas, liquidez, etc.).
   * Para cada categoria, indique em quais estudos cada subitem aparece, e se há tendências (por ex., “nos últimos 3 anos, cresce o uso de Mesa/Python ao invés de NetLogo”).
2. **Meta-Análise (se viável):**

   * A meta-análise em estudos ABM é incomum, pois frequentemente os resultados não são numéricos comparáveis diretamente. Ainda assim, você pode agrupar algumas métricas (como volatilidade média simulada) e, se existirem estudos suficientes com medidas comparáveis, calcular efeitos médios ou intervalos de confiança.
   * Caso não seja possível fazer meta-análise numérica, deixe claro no protocolo que a análise quantitativa será uma “meta-síntese de métricas correlacionadas”, sem cálculo formal de estatística combinada.
3. **Uso de Python para Visualizações:**

   * Projete, desde já, como você pretende gerar:

     * Gráficos de barras ou boxplots comparando métricas em diferentes estudos.
     * Redes de coautoria (talvez usando bibliotecas como NetworkX) para mapear colaborações entre grupos de pesquisa.
   * Documente na seção de métodos quais scripts Python (ou módulos) serão usados para cada tipo de visualização.

---

## 7. Considerações Éticas e de Transparência

**Comentário:**

* Excelente incluir a ideia de registro do protocolo (por exemplo, em PROSPERO ou num repositório público).

**Reforço:**

1. Se o protocolo for registrado (por exemplo, em Open Science Framework), inclua o link e data de registro no documento final.
2. Demonstre como serão relatadas possíveis fontes de viés (por exemplo, limitação ao inglês e português, exclusão de trabalhos não indexados, etc.).
3. Informe se haverá algum tipo de verificação duplo (dois revisores independentes) na triagem de títulos/resumos e/ou na extração de dados.

---

## 8. Cronograma e Responsabilidades

**Comentário:**

* Está em formato genérico (“(data)”), portanto falta detalhamento temporal.

**Sugestão de preenchimento (exemplo):**

* **Busca e triagem de estudos:**
  * 19/05/2025 – 26/05/2025

* **Extração de dados:**
  * 28/05/2025 – 15/06/2025

* **Avaliação de qualidade:**
  * 16/06/2025 – 25/06/2025

* **Análise e síntese dos resultados:**
  * 25/06/2025 – 30/06/2025

* **Redação do relatório e ajustes finais:**
  * 30/06/2025 – 05/07/2025

---

## 9. Disseminação dos Resultados

**Comentário:**

* Boa identificação de relatório técnico e publicação em periódico especializado.

**Que mais considerar:**

1. **Apresentação em Conferência:**

   * Você pode planejar submeter um workshop ou pôster em evento de modelagem computacional ou finanças (por exemplo, “International Conference on Computational Economics and Finance”).
2. **Repositório de Dados:**

   * Caso produza planilha com todos os dados extraídos, pense em deixar esse material público (por exemplo, no Zenodo ou GitHub) para maior transparência e reutilização.
3. **Versão Resumida em Língua Portuguesa e Inglesa:**

   * Se o público-alvo incluir pesquisadores brasileiros, considere preparar um “relatório abreviado” em português, além do artigo em inglês para periódico internacional.
