# Módulo 1: **Identificar as funções de manipulação de arquivos**

## 1. Objetivos de Aprendizagem

- Compreender o que são arquivos (textos, binários, etc.) e por que são importantes.
- Reconhecer as funções básicas de abertura, leitura, escrita e fechamento de arquivos.
- Entender modos de abertura de arquivos (leitura, escrita, adição, etc.).
- Saber manipular o cursor de leitura/escrita (quando aplicável).
- Conhecer boas práticas de manipulação de arquivos (tratamento de erros, fechamento adequado, etc.).

## 2. Conteúdo Programático

1. **Conceitos básicos**  
   - O que é um arquivo?  
   - Formatos: texto vs. binário.  
   - Sistemas de arquivos e caminhos (paths) absolutos e relativos.

2. **Abertura de arquivos**  
   - Funções/métodos de abertura (por exemplo, `fopen` em C, `open` em Python, `FileReader` em Java).  
   - Modos de abertura (leitura, escrita, escrita + criação, append, etc.).

3. **Leitura e escrita**  
   - Funções de leitura (`fread`, `fgets`, `fscanf`, etc. em C; `read()`, `readline()` em Python; `Scanner`, `BufferedReader` em Java).  
   - Funções de escrita (`fprintf`, `fwrite` em C; `write()`, `print()` em Python; `PrintWriter` em Java).

4. **Fechamento de arquivos**  
   - Importância de liberar recursos (uso de `fclose` em C, `close()` em Python/Java).  
   - Potenciais problemas ao não fechar corretamente (vazamentos de recurso, inconsistências no arquivo).

5. **Posicionamento no arquivo**  
   - Funções para manipular o cursor (`fseek`, `ftell`, `rewind` em C; métodos específicos em Python/Java).  
   - Uso em leitura/escrita aleatória vs. sequencial.

6. **Boas práticas**  
   - Tratamento de erros.  
   - Verificação de abertura de arquivo bem-sucedida.  
   - Fechamento em blocos de exceção (ex: `finally` em Java, `with` em Python).

## 3. Exemplos (linguagem genérica, adaptável)

**Exemplo 1 (Pseudocódigo)**  

```pseudo
file = open("dados.txt", "r")
if file is not null:
    line = file.readLine()
    while line != null:
        print(line)
        line = file.readLine()
    file.close()
else:
    print("Não foi possível abrir o arquivo")
```

- **Exemplo 2 (Manipulação de arquivo binário em C)**

```c
FILE *fp;
int numeros[5] = {1, 2, 3, 4, 5};

fp = fopen("binario.dat", "wb");
if (fp != NULL) {
    fwrite(numeros, sizeof(int), 5, fp);
    fclose(fp);
} else {
    printf("Erro ao abrir arquivo.\n");
}
```

## 4. Exercícios Propostos

1. **Leitura de Arquivo Texto**: Crie um programa que leia um arquivo texto linha a linha e imprima seu conteúdo no console.  
2. **Escrita em Arquivo**: Escreva um programa que receba nomes de estudantes e notas e salve em um arquivo CSV.  
3. **Manipulação de Cursor**: Desenvolva um programa que posicione o cursor em diferentes partes de um arquivo (por exemplo, ler o arquivo de trás para frente).

---

## Módulo 2: **Reconhecer as funções de manipulação de strings**

### 1. Objetivos de Aprendizagem

- Entender o conceito de string como uma sequência de caracteres.
- Conhecer funções comuns de manipulação (concatenação, divisão, busca, substituição, etc.).
- Aplicar métodos de formatação e conversão de strings.
- Desenvolver boas práticas para evitar problemas como buffer overflow (em C) ou manipulação ineficiente de strings (em linguagens de alto nível).

## 2. Conteúdo Programático

1. **Conceito de String**  
   - Representação interna em diferentes linguagens (em C como array de `char`, em Java como objeto `String`, em Python como tipo `str`).

2. **Principais Funções de Manipulação**  
   - Comprimento (ex: `strlen` em C, `len()` em Python, `length()` em Java).  
   - Concatenação (`strcat` em C, `+` ou `join` em Python, `concat` ou `+` em Java).  
   - Cópia (`strcpy` em C, fatiamento em Python, `substring` em Java).  
   - Comparação (`strcmp` em C, operadores `==` e `!=` em Python para objetos, `equals` em Java).  
   - Busca e substituição (`strstr`, `str_replace`, métodos em Python e Java).

3. **Fatiamento (Slicing)**  
   - Conceito de slicing em Python.  
   - Substring em Java (`substring(início, fim)`).  
   - Equivalentes em C (manipulação manual de ponteiros ou arrays).

4. **Formatação de Strings**  
   - `sprintf` em C, `format()` e f-strings em Python, `String.format` em Java.  
   - Máscaras de formatação (inteiros, floats, datas, etc.).

5. **Conversão de Strings**  
   - Para números (`atoi`, `atof` em C; `int()`, `float()` em Python; `Integer.parseInt`, `Double.parseDouble` em Java).  
   - Para maiúsculas/minúsculas (`toupper`, `tolower` em C; `upper()`, `lower()` em Python; `toUpperCase`, `toLowerCase` em Java).

6. **Boas Práticas**  
   - Evitar buffer overflow em C (uso de `strncpy`, limites de tamanho).  
   - Uso eficiente de strings em linguagens de alto nível (imutabilidade, uso de `StringBuilder` em Java quando necessário).

### 3. Exemplos (linguagem genérica, adaptável)

- **Exemplo 1 (Pseudocódigo)**

```pseudo
texto = "Olá, Mundo!"
print("Comprimento: " + length(texto))
print("Parte inicial: " + substring(texto, 0, 5))
print("Maiúsculo: " + toUpperCase(texto))
```

- **Exemplo 2 (C – Concatenação segura)**

```c
char str1[20] = "Hello ";
char str2[] = "World!";
strncat(str1, str2, sizeof(str1) - strlen(str1) - 1);
printf("%s\n", str1);
```

### 4. Exercícios Propostos

1. **Verificação de Palíndromo**: Escreva um programa que leia uma string e verifique se ela é um palíndromo.  
2. **Formatação de Strings**: Crie um código que leia nome, idade e salário de uma pessoa e formate uma mensagem de saída.  
3. **Substituição**: Faça um programa que busque todas as ocorrências de uma substring e as substitua por outra.

---

## Módulo 3: **Descrever as exceções na manipulação de arquivos e outras operações**

### 1. Objetivos de Aprendizagem

- Entender o que são exceções e por que elas ocorrem.
- Compreender como tratar erros relacionados à manipulação de arquivos (arquivo inexistente, permissões, etc.).
- Conhecer mecanismos de tratamento de exceções (try/catch, try/except, etc.) em diferentes linguagens.
- Saber quando lançar exceções personalizadas e como criar logs de erros.

### 2. Conteúdo Programático

1. **Introdução às Exceções**  
   - Definição e importância do tratamento de erros.  
   - Diferença entre erros em tempo de compilação e exceções em tempo de execução.

2. **Exceções Comuns em Manipulação de Arquivos**  
   - Arquivo não encontrado.  
   - Permissão negada.  
   - Disco cheio ou problemas de escrita/leitura.  
   - Erros de formatação em leitura (ex: ler arquivo texto como binário).

3. **Tratamento de Exceções**  
   - Estrutura geral (por exemplo, `try-catch-finally` em Java, `try-except-finally` em Python, em C uso de retornos de função e códigos de erro).  
   - Pilha de chamadas e propagação de exceções.

4. **Exceções Personalizadas**  
   - Quando criar suas próprias exceções.  
   - Vantagens de uma hierarquia de exceções clara.

5. **Boas Práticas**  
   - Logar e reportar erros (armazenamento de logs, uso de frameworks de logging).  
   - Evitar tratamento excessivo ou “engolir” exceções.  
   - Uso de blocos `finally` (ou contexto `with` em Python) para garantir fechamento de recursos.

### 3. Exemplos (linguagem genérica, adaptável)

**Exemplo 1 (Java)**

```java
try {
    FileReader fr = new FileReader("arquivo.txt");
    BufferedReader br = new BufferedReader(fr);
    String linha = br.readLine();
    while (linha != null) {
        System.out.println(linha);
        linha = br.readLine();
    }
    br.close();
} catch (FileNotFoundException e) {
    System.out.println("Arquivo não encontrado: " + e.getMessage());
} catch (IOException e) {
    System.out.println("Erro de leitura/escrita: " + e.getMessage());
} finally {
    System.out.println("Bloco finally sempre é executado.");
}
```

**Exemplo 2 (Python)**

```python
try:
    with open("dados.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError as e:
    print(f"Erro: {e}")
except PermissionError as e:
    print(f"Permissão negada: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
```

### 4. Exercícios Propostos

1. **Tratamento de Erro em Abertura**: Escreva um programa que tente abrir um arquivo e trate possíveis erros (arquivo não existente, sem permissão).  
2. **Exceções Personalizadas**: Crie uma classe de exceção personalizada para lidar com formatação incorreta de um arquivo de configuração.  
3. **Log de Exceções**: Implemente um sistema simples de logging que registre exceções ocorridas durante a leitura e escrita de arquivos.

---

## Estrutura Geral de Aula e Metodologia

1. **Apresentação Teórica (20% do tempo)**  
   - Use slides ou quadro para explicar os conceitos básicos de cada módulo.  
   - Aborde exemplos simples, comparando as funções/métodos em diferentes linguagens (se for relevante para o curso).

2. **Demonstrações Práticas (30% do tempo)**  
   - Mostre na prática como abrir um arquivo, ler/escrever conteúdo e fechar adequadamente.  
   - Demonstre casos de erro e como o programa se comporta.

3. **Exercícios Orientados (30% do tempo)**  
   - Proponha exercícios curtos em sala de aula para que os alunos testem o conhecimento.  
   - Estimule o uso de técnicas de depuração (debug) para observar variáveis e entender comportamentos anômalos.

4. **Discussão e Revisão (20% do tempo)**  
   - Reserve tempo para perguntas, revisões e esclarecimento de dúvidas.  
   - Apresente boas práticas e discuta problemas reais (casos em produção ou exemplos históricos de falhas de manipulação de arquivos).

---

## Recursos e Referências

1. **Documentação Oficial**  
   - [Documentação em C](https://en.cppreference.com/w/c/io)  
   - [Documentação Python](https://docs.python.org/pt-br/3/tutorial/inputoutput.html)  
   - [Documentação Java (File I/O)](https://docs.oracle.com/javase/tutorial/essential/io/index.html)

2. **Livros e Materiais Complementares**  
   - “The C Programming Language” – Brian Kernighan e Dennis Ritchie (para quem utiliza C).  
   - “Automate the Boring Stuff with Python” – Al Sweigart (capítulos sobre leitura e escrita de arquivos).  
   - “Effective Java” – Joshua Bloch (capítulo sobre tratamento de exceções).

3. **Ferramentas de Prática**  
   - Ambientes de desenvolvimento integrados (IDEs) ou editores de texto com suporte a execução rápida (VS Code, PyCharm, Eclipse, etc.).  
   - Repositórios de códigos de exemplo (GitHub, GitLab).

---

### Observações Finais

- O conteúdo de cada módulo pode ser expandido ou reduzido conforme o nível de conhecimento prévio dos alunos e o tempo disponível.  
- Reforce a importância de tratar adequadamente recursos de I/O e exceções para construir programas robustos.  
- Sempre incentive a prática constante e o uso de ferramentas de versionamento (Git) para que os alunos acompanhem suas evoluções e gerenciem seus projetos adequadamente.

---

**Este material serve como um guia inicial para estruturar aulas em nível de graduação sobre funções de manipulação de arquivos, funções de manipulação de strings e tratamento de exceções relacionadas.** Sinta-se à vontade para ajustar exemplos e exercícios de acordo com a linguagem principal do curso e o perfil dos estudantes.
