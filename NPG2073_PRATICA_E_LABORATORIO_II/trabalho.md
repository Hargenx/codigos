# Avaliação: Instalação e Configuração do Hadoop

**Objetivo:**  
Avaliar a compreensão teórica e prática dos passos envolvidos na instalação e configuração do Hadoop, além da capacidade de identificar e resolver problemas comuns.

**Instruções Gerais:**  

- A avaliação deve ser respondida de forma individual.
- Utilize o script apresentado como base e, se necessário, consulte a documentação do Hadoop.

---

## Questões Teóricas

1. **Contextualização do Hadoop (2 pontos):**  
   Explique brevemente o que é o Hadoop, qual a sua importância no processamento de grandes volumes de dados e como ele se encaixa no contexto de Big Data.

2. **Análise dos Comandos (3 pontos):**  
   No script de instalação, são utilizados os comandos `wget`, `tar`, `cp` e `readlink`. Para cada um deles, responda:
   - Qual a função do comando?
   - Por que ele é necessário no contexto da instalação do Hadoop?

3. **Configuração do JAVA_HOME (2 pontos):**
   Justifique a importância de configurar corretamente a variável `JAVA_HOME` no arquivo `hadoop-env.sh` para o funcionamento do Hadoop. Quais problemas podem ocorrer se essa configuração não estiver correta?

4. **Solução de Problemas (3 pontos):**  
   Durante a instalação e configuração, erros podem ocorrer (por exemplo, problemas de permissão ou download incompleto). Identifique dois possíveis problemas que podem surgir e sugira uma solução ou procedimento de verificação para cada um.

---

## Exercício Prático

- **Modificação do Script (Exercício Prático – 5 pontos):**  
   Faça uma modificação no script original de instalação para que, após a cópia do diretório do Hadoop para `/usr/local/`, seja exibida uma mensagem de confirmação no terminal, informando que a instalação foi concluída com sucesso.  
       - **Tarefa:** Insira, no final do script, um comando que exiba a mensagem "Instalação do Hadoop concluída com sucesso!"  
       - **Documente:** Explique brevemente a modificação realizada e como ela contribui para a validação do processo de instalação.

---

## Avaliação

---

**Critérios de Avaliação:**  

- Clareza e objetividade nas respostas teóricas.
- Correção e relevância das explicações.
- Funcionalidade e clareza na modificação prática do script.
- Boa organização do conteúdo e utilização adequada dos comandos.

Boa avaliação!
