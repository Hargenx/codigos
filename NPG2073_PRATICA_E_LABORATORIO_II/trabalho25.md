# Avaliação Integrada: Uso do Hadoop com PySpark e MapReduce

## Avaliação

- **Disciplina**: Práticas e Laboratório II
- **Professor**: Raphael Mauricio Sanches de Jesus
- **Email**: <raphael.jesus@estacio.br>
- **Período**: Pós-Graduação  
- **Data de Entrega**: ~30/03/2025~

---

## Objetivos

- **Conceitual:** Verificar a compreensão sobre o papel do Hadoop no processamento distribuído, as diferenças entre MapReduce tradicional e PySpark, e a importância da configuração correta do ambiente.
- **Prático:** Avaliar a capacidade de implementar um job simples em PySpark (por exemplo, um word count) e, opcionalmente, demonstrar conhecimento do paradigma MapReduce através de um código.

---

## Parte Teórica

**1. Papel do Hadoop e Vantagens do PySpark (2 pontos)**  
Explique brevemente:

- O que é o Hadoop e como ele viabiliza o processamento e armazenamento de grandes volumes de dados em ambientes distribuídos.
- Quais são as vantagens de utilizar frameworks como o PySpark em comparação com o paradigma MapReduce tradicional.

**2. Configuração do Ambiente (2 pontos)**  
Liste e explique os passos essenciais para configurar o Hadoop de forma a integrá-lo com jobs do PySpark, destacando a importância da variável `JAVA_HOME` e da correta instalação do Hadoop.

**3. Paradigma MapReduce (2 pontos)**  
Descreva o funcionamento do paradigma MapReduce, utilizando como exemplo a contagem de palavras (word count). Em sua resposta, defina:

- A função de **Map**: como ela processa os dados de entrada.
- A função de **Reduce**: como ela agrega os resultados do map.
  
**4. Desafios na Integração Hadoop e PySpark (2 pontos)**  
Cite dois desafios comuns ao utilizar PySpark em conjunto com o Hadoop (por exemplo, questões de compatibilidade de versões, configuração de acesso ao HDFS, etc.) e proponha uma solução ou estratégia para cada um.

---

## Parte Prática

**5. Job PySpark para Word Count (2 pontos)**  
Desenvolva um script em PySpark que execute as seguintes etapas:

- **Leitura dos Dados:** Leia um arquivo de texto a partir do HDFS (ou, para fins de teste, simule a leitura de um arquivo local).
- **Processamento:** Realize a contagem de palavras (word count) do texto.
- **Escrita dos Resultados:** Salve o resultado da contagem em um arquivo CSV de volta no HDFS (ou localmente, se for o caso).
- **Comentários:** Comente cada etapa do código explicando o que está sendo feito.

*Dica:* Caso não possua acesso direto a um cluster Hadoop/HDFS, utilize um arquivo local e comente como o código seria adaptado para o HDFS.

**6. (Opcional) código MapReduce para Word Count (Opcional – 1 pontos)**  
Escreva um código que descreva um job MapReduce para realizar a mesma tarefa de word count. Em sua resposta:

- Destaque as etapas do **Map** e do **Reduce**.
- Comente as principais diferenças práticas entre essa abordagem e o uso do PySpark para a mesma tarefa.

---

### Critérios de Avaliação

- **Clareza e Coerência:** As respostas devem demonstrar domínio dos conceitos teóricos e práticos.
- **Correção Técnica:** As soluções (código e pseudo-código) devem estar corretas e funcionais, mesmo que a execução seja simulada.
- **Documentação e Comentários:** O código deve conter comentários claros que expliquem cada etapa do processo.
- **Organização:** A estrutura do relatório e a apresentação das respostas devem ser organizadas e objetivas.

---

Exemplo hadoop: <https://colab.research.google.com/drive/1kxHuC_wf804aKDSJvHikCqyDv9CS4b_8?usp=sharing>
Exemplo PySpark: <https://colab.research.google.com/drive/12fXM9G0OPbvNoUPRFhBoSIafXUTpdtor?usp=sharing>

Boa avaliação!
