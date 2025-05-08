# 🎫 Totem de Estacionamento — Projeto Educacional

Este é um **projeto exemplo** desenvolvido com fins didáticos para alunos de graduação em cursos de Computação, Sistemas de Informação e afins. O objetivo é demonstrar a aplicação do padrão arquitetural **MVC (Model-View-Controller)** utilizando a linguagem **Python** com a biblioteca **Tkinter** para interfaces gráficas.

---

## 🧭 Funcionalidades

### Entrada de Veículos

- Geração automática de tickets com placas simuladas.
- Registro de data/hora de entrada.
- Armazenamento persistente em arquivo JSON.
- Registro de log para auditoria.

### Totem de Pagamento

- Interface gráfica para simular o pagamento de estacionamento.
- Consulta de ticket, cálculo de valor pela permanência.
- Pagamento via Cartão ou PIX (simulado).
- Geração de comprovante em `.txt` estilo cupom fiscal.
- Registro em log e controle de tempo para liberação.

---

## 🧱 Arquitetura do Projeto

O projeto está organizado segundo o padrão **MVC**:

```terminal

totem\_estacionamento/
├── controller/       # Lógica de controle
├── model/            # Regras de negócio e persistência
├── view/             # Interfaces gráficas (Tkinter)
├── data/             # Dados persistentes (JSON, log e comprovantes)
├── main.py           # Inicia o totem de pagamento
└── main\_entrada.py   # Inicia o painel de entrada

````

---

## 🚀 Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório.
3. Execute o painel de entrada com:

    ```bash
    python main_entrada.py
    ````

4. Execute o totem de pagamento com:

    ```bash
    python main.py
    ```

---

## 📚 Aprendizados Aplicados

- Uso do padrão **MVC**
- Boas práticas com funções, módulos e classes
- Persistência de dados com arquivos `.json`
- Manipulação de datas e horários (`datetime`)
- Geração de logs (`logging`)
- Criação de interfaces com **Tkinter**
- Simulação de sistema real: entrada, pagamento e saída

---

## 📎 Observações

Este sistema é uma **simulação acadêmica**. Nenhuma integração real com sistemas de pagamento foi implementada. Todos os dados são gerados e armazenados localmente para fins de demonstração.

---

## 👨‍🏫 Autor

Prof. Raphael Mauricio Sanches de Jesus

- Desenvolvedor de software e professor universitário.
