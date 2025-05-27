# **Nível Estagiário – Fundamentos e Boas Práticas**

## **1. Cadastro Simples de Produtos**

**Objetivo:** Criar uma classe `Produto` com atributos `nome`, `preco` e `quantidade`.
**Desafio:** Criar um menu de texto para cadastrar produtos e mostrar todos os produtos cadastrados.
**Requisitos:**

* Encapsulamento.
* Validação de dados (ex: preço e quantidade não podem ser negativos).
* `toString()` personalizado.

---

## **2. Controle de Conta Bancária**

**Objetivo:** Criar uma classe `ContaBancaria` com métodos para `sacar`, `depositar` e `consultarSaldo`.
**Desafio:** Criar uma interface `OperacoesConta` e implementá-la na classe.
**Requisitos:**

* Uso de interface.
* Tratamento de exceções para saques indevidos.
* Separação entre modelo (classe) e lógica de uso (main).

---

## **3. Gerenciamento de Tarefas**

**Objetivo:** Criar classes `Tarefa` e `GerenciadorDeTarefas`.
**Desafio:** Adicionar, remover, listar tarefas e marcar como concluída.
**Requisitos:**

* Uso de `ArrayList`.
* Uso de `enum` para status (`PENDENTE`, `CONCLUIDA`).
* Responsabilidade única (SRP).

---

## **4. Sistema de Notas**

**Objetivo:** Criar classe `Aluno` com nome e notas, e calcular média.
**Desafio:** Informar se o aluno está aprovado (média ≥ 6).
**Requisitos:**

* Uso de métodos privados para lógica de média.
* Separação de responsabilidades entre entrada e cálculo.

---

## **5. Agenda Telefônica**

**Objetivo:** Criar uma agenda que armazena contatos (nome + telefone).
**Desafio:** Buscar por nome e exibir todos os contatos.
**Requisitos:**

* Uso de `HashMap<String, String>`.
* Boas práticas de escrita de métodos (`get`, `add`, `list`).

---

## **Nível Júnior – Orientação a Objetos + Padrões**

### **6. Biblioteca com Herança**

**Objetivo:** Criar uma superclasse `ItemBiblioteca` e subclasses `Livro` e `Revista`.
**Desafio:** Implementar um sistema para listar todos os itens disponíveis e emprestar.
**Requisitos:**

* Herança e polimorfismo.
* Princípios de Liskov e Open/Closed.
* Uso de `instanceof` só se justificável.

---

### **7. Sistema de Pedidos com Composição**

**Objetivo:** Classe `Pedido` que contém vários `ItemPedido`.
**Desafio:** Calcular valor total e permitir a adição/remoção de itens.
**Requisitos:**

* Composição.
* Boas práticas de modelagem.
* `BigDecimal` no lugar de `double`.

---

### **8. Controle de Funcionários com Interface**

**Objetivo:** Interface `Funcionario` com método `calcularSalario()`.
**Desafio:** Implementar classes `FuncionarioCLT` e `FuncionarioPJ`.
**Requisitos:**

* Uso de polimorfismo.
* `List<Funcionario>` com cálculo do custo mensal total.
* OCP e SRP.

---

### **9. Cadastro com Validação e DAO Simulado**

**Objetivo:** Criar CRUD de usuários com validação e persistência em memória.
**Desafio:** Separar em camadas: Model, Controller e DAO.
**Requisitos:**

* Padrão DAO (sem banco real).
* Validações com exceptions personalizadas.
* Arquitetura MVC (simples).

---

### **10. Aplicando o Padrão Strategy**

**Objetivo:** Sistema de cálculo de frete com diferentes estratégias (Normal, Expresso).
**Desafio:** Usar padrão Strategy para escolher algoritmo de frete em tempo de execução.
**Requisitos:**

* Interfaces para estratégias.
* Evitar `if`/`else` extensivos.
* Boa separação entre contexto e estratégias.
