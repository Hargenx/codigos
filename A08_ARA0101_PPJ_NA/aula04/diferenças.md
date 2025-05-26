# Diferença entre Factory Method e Abstract Factory

## Factory Method

- **Foco na Criação de um Único Produto:**  
  O Factory Method define um método (geralmente abstrato) responsável por criar um único tipo de objeto. As subclasses implementam esse método para instanciar produtos concretos específicos.

- **Herança e Sobrescrita:**  
  O padrão se baseia no uso da herança. A classe base declara o método-fábrica e as classes derivadas decidem qual instância concreta retornar.

- **Desacoplamento na Criação:**  
  Permite que o cliente use o método sem conhecer as classes concretas, mas o foco é criar apenas um objeto por vez.

- **Exemplo Prático:**  
  Uma classe `Pedido` que possui um método abstrato `criarItem()` e subclasses como `PedidoLojaFisica` e `PedidoOnline` que implementam esse método para criar, respectivamente, `ItemPedidoLojaFisica` ou `ItemPedidoOnline`.

---

## Abstract Factory

- **Foco em Famílias de Produtos:**  
  O Abstract Factory fornece uma interface para criar **vários produtos relacionados**. Ou seja, ele agrupa vários métodos-fábrica, cada um responsável por criar um produto diferente, mas que pertencem à mesma família.

- **Composição ao Invés de Herança:**  
  Em vez de apenas depender de herança para criar um único objeto, o Abstract Factory usa a composição para garantir que todos os produtos criados por uma fábrica sejam compatíveis entre si.

- **Coerência entre os Produtos:**  
  Garante que os objetos criados (por exemplo, componentes de uma interface ou itens de um pedido) sejam usados juntos, mantendo uma consistência de design ou regras de negócio.

- **Exemplo Prático:**  
  Em um sistema de e-commerce, uma fábrica para pedidos físicos pode criar um `PhysicalOrderItem`, um `PhysicalPayment` e um `PhysicalShipping`, enquanto uma fábrica para pedidos digitais cria `DigitalOrderItem`, `DigitalPayment` e `DigitalShipping`. Dessa forma, cada fábrica gera uma família de objetos que se complementam.

---

## Resumo das Diferenças

- **Escopo de Criação:**
  - **Factory Method:** Cria **um único** produto.
  - **Abstract Factory:** Cria **vários produtos** que compõem uma família.

- **Abordagem:**
  - **Factory Method:** Baseado em **herança**, onde subclasses determinam a instância a ser criada.
  - **Abstract Factory:** Baseado em **composição**, onde uma fábrica abstrata agrupa vários métodos para a criação dos produtos relacionados.

- **Aplicação:**
  - **Factory Method:** Útil quando há variação na criação de um único objeto, mas não há necessidade de garantir a compatibilidade entre múltiplos produtos.
  - **Abstract Factory:** Ideal para cenários onde é preciso garantir que os objetos criados trabalhem juntos de forma consistente, como em interfaces gráficas (botões, menus, janelas) ou diferentes tipos de pedidos em um e-commerce.

---

Essas diferenças ajudam a definir quando usar cada padrão de forma adequada, de acordo com os requisitos e a complexidade da criação dos objetos no sistema.
