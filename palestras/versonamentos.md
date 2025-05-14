# Palestra: Controle de Versão com Git e GitHub

## 📅 Duração: 1 hora

---

## 🔹 Roteiro da Apresentação

### 1. Abertura e Motivação (5 min)

* Apresentação do palestrante
* Importância do controle de versão
* Problemas comuns sem Git

### 2. Conceitos Fundamentais (10 min)

* O que é o Git (local e distribuído)
* Diferença entre Git e GitHub
* Ciclo de vida dos arquivos

  * Untracked ➔ Staged ➔ Committed

### 3. Comandos Básicos do Git (15 min)

```bash
git init                # Inicializa um repositório Git
git add .               # Adiciona todos os arquivos ao stage
git commit -m "msg"     # Salva as alterações com uma mensagem
git status              # Mostra o estado dos arquivos
git log                 # Mostra o histórico de commits
git diff                # Mostra diferenças não commitadas
```

### 4. Integração com GitHub (10 min)

```bash
# Crie o repositório no GitHub e copie o link

git remote add origin https://github.com/seuusuario/git-palestra-exemplo.git
git branch -M main
git push -u origin main

git clone https://github.com/seuusuario/git-palestra-exemplo.git
git pull origin main
```

### 5. Branches e Colaboração (10 min)

```bash
git checkout -b nova-feature    # Cria e muda para a branch
git checkout main               # Volta para a branch principal
git merge nova-feature          # Faz merge da branch atual na main
git branch                      # Lista todas as branches
```

### 6. Dicas e Erros Comuns (5 min)

```bash
git reset --hard                # Desfaz commits locais
git stash                       # Guarda mudanças temporariamente
```

* Criar `.gitignore`
* Fazer commits pequenos e com mensagens claras

### 7. Encerramento e Perguntas (5 min)

* Recapitulação dos principais conceitos
* Recursos:

  * [https://git-scm.com/book/pt-br](https://git-scm.com/book/pt-br)
  * [https://learngitbranching.js.org](https://learngitbranching.js.org)
  * [https://docs.github.com](https://docs.github.com)
* QR code com repositório de exemplo: `https://github.com/professorRaphael/git-palestra-exemplo`

---

## 📖 Slides e Materiais de * Demonstração prática com terminal e navegador

* Repositório de exemplo (próprio): [https://github.com/seuusuario/git-palestra-exemplo](https://github.com/seuusuario/git-palestra-exemplo)

---

## 📁 Estrutura do Repositório de Exemplo

```bash
📦 git-palestra-exemplo
├── 📄 README.md              # Explicação geral do projeto e comandos usados
├── 📁 projeto-exemplo        # Pasta com arquivos simulando um mini projeto real
│   ├── index.html
│   ├── script.js
│   └── style.css
├── 📄 .gitignore             # Arquivos/ pastas ignoradas pelo Git
└── 📄 LICENSE                # Licença de uso opcional
```

### README.md (sugestão de conteúdo)

```markdown
# Git Palestra Exemplo

Este repositório foi criado para servir de base para a palestra "Controle de Versão com Git e GitHub".

## Objetivo
Demonstrar os principais comandos Git na prática e simular um fluxo básico de versionamento e colaboração.

## Comandos abordados
- git init
- git add / commit / status / log / diff
- git branch / checkout / merge
- git push / pull / clone
- git stash / reset

## Slides de apoio
Disponíveis em: [link para os slides utilizados na apresentação]

---

**Instrutor:** Seu Nome
```

Se desejar, posso gerar esse repositório automaticamente ou fornecer os arquivos para você subir no GitHub.
