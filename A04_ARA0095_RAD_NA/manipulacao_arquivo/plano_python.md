A seguir, apresento uma proposta de material de aula em nível de graduação para abordar os três módulos mencionados, **focando exclusivamente em Python**. O conteúdo pode ser adaptado de acordo com a carga horária disponível e o perfil dos estudantes. A estrutura inclui objetivos de aprendizagem, conteúdo programático, exemplos e sugestões de exercícios.

---

## **Módulo 1: Identificar as funções de manipulação de arquivos em Python**

### 1. Objetivos de Aprendizagem

- Entender como funcionam os arquivos em Python (texto, binário, etc.).
- Aprender a abrir, ler, escrever e fechar arquivos corretamente.
- Conhecer os diferentes modos de abertura (leitura, escrita, adição, etc.).
- Manipular o “cursor” de leitura/escrita com métodos como `seek()` e `tell()`.
- Aplicar boas práticas de tratamento de erros e gerenciamento de recursos (uso de `with`).

### 2. Conteúdo Programático

1. **Conceitos básicos**  
   - O que é um arquivo (textual e binário).  
   - Estrutura de diretórios e caminhos (paths) absolutos e relativos.  
   - Diferenças entre leitura sequencial e aleatória.

2. **Abrindo e fechando arquivos**  
   - Uso da função `open()`.  
   - Modos de abertura:  
     - `'r'` (leitura), `'w'` (escrita, sobrescreve), `'a'` (adição),  
     - `'r+'` (leitura/escrita), `'w+'` (escrita/leitura), `'a+'` (adição/leitura),  
     - `'rb'`, `'wb'`, `'ab'` para arquivos binários.  
   - Uso do gerenciador de contexto `with open(...) as file:` para fechar o arquivo automaticamente.

3. **Lendo arquivos**  
   - Métodos: `read()`, `readline()`, `readlines()`.  
   - Iterar linha a linha usando `for line in file:`.  
   - Leitura de arquivos binários (ex.: `file.read(1024)` para ler 1024 bytes).

4. **Escrevendo em arquivos**  
   - Método `write()`.  
   - Escrita de texto vs. escrita binária.  
   - Usando `print(..., file=file)` para redirecionar a saída.

5. **Posicionamento no arquivo**  
   - Métodos `seek(offset, whence)` e `tell()`.  
   - Exemplos de uso para manipulação aleatória de arquivos.

6. **Tratamento de erros**  
   - Exceções comuns: `FileNotFoundError`, `PermissionError`, `IOError`.  
   - Uso de `try/except` para capturar e tratar erros na abertura/leitura/escrita.

7. **Boas práticas**  
   - Uso do `with` para garantir fechamento.  
   - Verificação de caminhos (ex.: uso do módulo `os` ou `pathlib`).  
   - Log e mensagens de erro claras.

### 3. Exemplos

**Exemplo 1: Leitura de arquivo texto**

```python
filename = "exemplo.txt"

try:
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"Arquivo {filename} não encontrado.")
except PermissionError:
    print(f"Sem permissão para ler o arquivo {filename}.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
```

**Exemplo 2: Escrita de arquivo texto**

```python
dados = ["Linha 1", "Linha 2", "Linha 3"]
with open("saida.txt", "w") as file:
    for linha in dados:
        file.write(linha + "\n")
```

**Exemplo 3: Leitura de arquivo binário**

```python
with open("imagem.jpg", "rb") as file:
    conteudo = file.read(100)  # lê 100 bytes
    print(conteudo)
```

### 4. Exercícios Propostos

1. **Leitura Simples**: Crie um programa que leia um arquivo texto (de no máximo 10 linhas) e imprima seu conteúdo na tela, numerando cada linha.
2. **Escrita de Notas**: Desenvolva um programa que receba nomes e notas de alunos via teclado e salve em um arquivo CSV (`dados.csv`). Cada linha do arquivo deve ter a forma: `nome,nota`.
3. **Manipulação de Cursor**: Faça um programa que abra um arquivo texto e, usando `seek()` e `tell()`, leia apenas a terceira linha do arquivo. Em seguida, retorne ao início para ler a primeira linha.

---

## **Módulo 2: Reconhecer as funções de manipulação de strings em Python**

### 1. Objetivos de Aprendizagem

- Entender como strings são representadas e manipuladas em Python.
- Aprender métodos de busca, substituição, formatação, fatiamento (slicing) e concatenação.
- Saber converter strings em números e vice-versa.
- Aplicar boas práticas de uso de strings, incluindo formatação avançada com f-strings.

### 2. Conteúdo Programático

1. **Conceito de string em Python**  
   - Tipo `str`: imutabilidade.  
   - Indexação e slicing: `texto[0]`, `texto[1:5]`, `texto[::-1]`.

2. **Principais métodos de manipulação**  
   - **Busca**: `find()`, `index()`, `count()`.  
   - **Substituição**: `replace(antigo, novo)`.  
   - **Remoção de espaços**: `strip()`, `lstrip()`, `rstrip()`.  
   - **Alteração de caixa**: `upper()`, `lower()`, `title()`.  
   - **Divisão e junção**: `split()`, `' '.join(lista)`.  
   - **Concatenação**: operador `+` e f-strings.

3. **Formatação de strings**  
   - F-strings: `f"{variavel}"`.  
   - Método `format()`: `"{} e {}".format(x, y)`.  
   - Formatação de números, datas (ex.: usando módulo `datetime`).

4. **Conversão de tipos**  
   - Para inteiro: `int("123")`.  
   - Para float: `float("123.45")`.  
   - De número para string: `str(123)`.  

5. **Boas práticas**  
   - Uso de f-strings para legibilidade.  
   - Evitar concatenar muitas strings em loop (em Python isso não é tão crítico como em outras linguagens, mas ainda assim f-strings ou `join` podem ser mais eficientes).

### 3. Exemplos

**Exemplo 1: Slicing e métodos básicos**

```python
texto = "Olá, Mundo!"
print(texto[0])         # 'O'
print(texto[0:5])       # 'Olá, '
print(texto.upper())    # 'OLÁ, MUNDO!'
print(texto.replace("Mundo", "Python"))  # 'Olá, Python!'
```

**Exemplo 2: Conversão de tipos e formatação**

```python
numero_str = "42"
numero_int = int(numero_str)
print(f"O número inteiro é {numero_int}, do tipo {type(numero_int)}")

valor = 3.14159
print(f"O valor formatado com 2 casas decimais é {valor:.2f}")
```

### 4. Exercícios Propostos

1. **Verificação de Palíndromo**: Escreva uma função que receba uma string e retorne `True` se ela for palíndromo (desconsiderando espaços e pontuação), ou `False` caso contrário.
2. **Substituição de Palavras**: Faça um programa que leia um texto de um arquivo e substitua todas as ocorrências de uma palavra X por Y, salvando o resultado em um novo arquivo.
3. **Formatação de Relatório**: Crie um relatório formatado com dados de produtos (nome, quantidade e preço). Utilize f-strings para exibir as informações em colunas alinhadas.

---

## **Módulo 3: Descrever as exceções na manipulação de arquivos e outras operações em Python**

### 1. Objetivos de Aprendizagem

- Compreender o que são exceções e por que ocorrem.
- Identificar exceções comuns em Python ao lidar com arquivos (e em outras operações).
- Aplicar blocos `try/except/else/finally` para tratamento adequado de erros.
- Criar exceções personalizadas quando necessário.

### 2. Conteúdo Programático

1. **Introdução às exceções em Python**  
   - Diferença entre erros de sintaxe e exceções em tempo de execução.  
   - Hierarquia de exceções (`BaseException`, `Exception`, etc.).

2. **Exceções comuns na manipulação de arquivos**  
   - `FileNotFoundError`, `PermissionError`, `IOError`, `IsADirectoryError`.  
   - Como capturar múltiplas exceções.

3. **Tratamento de exceções**  
   - Estrutura `try/except/else/finally`.  
   - Uso do `with open(...)` para simplificar tratamento de recursos.

4. **Exceções personalizadas**  
   - Criação de classes que herdam de `Exception`.  
   - `raise` para lançar exceções específicas.

5. **Boas práticas**  
   - Mensagens de erro claras.  
   - Evitar “engolir” exceções sem log ou tratamento.  
   - Quando e como relançar exceções (`raise`).

### 3. Exemplos

**Exemplo 1: Tratamento de exceções com arquivo**

```python
try:
    with open("dados.txt", "r") as file:
        conteudo = file.read()
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Sem permissão para acessar o arquivo.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
```

**Exemplo 2: Exceção personalizada**

```python
class FormatoInvalidoError(Exception):
    pass

def ler_configuracao(nome_arquivo):
    with open(nome_arquivo, "r") as file:
        conteudo = file.read()
        if not conteudo.startswith("[CONFIG]"):
            raise FormatoInvalidoError("Arquivo de configuração inválido.")
    return conteudo

try:
    config = ler_configuracao("config.txt")
    print("Configuração lida com sucesso!")
except FormatoInvalidoError as e:
    print(f"Erro de formato: {e}")
except FileNotFoundError:
    print("Arquivo de configuração não encontrado.")
```

### 4. Exercícios Propostos

1. **Tratamento de Erro em Abertura**: Escreva um programa que tente abrir um arquivo (caminho fornecido pelo usuário) e trate possíveis erros de `FileNotFoundError` e `PermissionError`.
2. **Exceções Personalizadas**: Crie uma classe de exceção para verificar se um arquivo de dados segue um padrão específico (por exemplo, se todas as linhas possuem a mesma quantidade de colunas).
3. **Log de Erros**: Implemente um pequeno sistema de log que registre exceções ocorridas durante a leitura e escrita de arquivos em um arquivo `log.txt`.

---

## **Estrutura Geral de Aula e Metodologia**

1. **Apresentação Teórica (20% do tempo)**  
   - Introduza os conceitos de cada módulo (arquivos, strings, exceções).  
   - Use slides ou demonstrações rápidas em Python.

2. **Demonstrações Práticas (30% do tempo)**  
   - Mostre exemplos ao vivo no interpretador Python ou em um editor (VS Code, PyCharm, etc.).  
   - Destaque como os erros aparecem e como são tratados.

3. **Exercícios Orientados (30% do tempo)**  
   - Proponha exercícios curtos para que os alunos testem o conhecimento.  
   - Dê feedback imediato para corrigir erros e reforçar conceitos.

4. **Discussão e Revisão (20% do tempo)**  
   - Reserve tempo para perguntas e revisão de possíveis problemas encontrados.  
   - Aborde boas práticas e compartilhe experiências de casos reais.

---

## **Recursos e Referências**

1. **Documentação Oficial do Python**  
   - [Documentação de I/O](https://docs.python.org/3/tutorial/inputoutput.html)  
   - [Tratamento de Exceções](https://docs.python.org/3/tutorial/errors.html)

2. **Livros e Materiais Complementares**  
   - “Automate the Boring Stuff with Python” – Al Sweigart (capítulos sobre leitura e escrita de arquivos).  
   - “Python Cookbook” – David Beazley e Brian K. Jones (receitas avançadas).

3. **Ferramentas de Prática**  
   - Python 3 (recomendado) instalado localmente ou uso de ambientes virtuais.  
   - IDEs ou editores como VS Code, PyCharm, Jupyter Notebook.

---

### Observações Finais

- Ajuste a profundidade de cada tópico de acordo com o conhecimento prévio dos alunos.  
- Demonstre casos práticos, como leitura de grandes arquivos, tratamento de logs e formatação de relatórios.  
- Reforce sempre o uso de boas práticas de programação, pois a manipulação de arquivos e tratamento de exceções são fundamentais para a robustez dos sistemas em produção.

---

**Este material fornece uma base sólida para aulas de graduação sobre manipulação de arquivos, manipulação de strings e tratamento de exceções em Python.** Sinta-se livre para complementar com exemplos adicionais, projetos práticos e estudos de caso reais que possam enriquecer a experiência de aprendizado dos estudantes.
