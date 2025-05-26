# Abstract Factory

Exemplo: Sistema de Interfaces para Diferentes Plataformas

Considere um sistema que precisa exibir uma interface gráfica em múltiplas plataformas (Windows, macOS, Linux). Cada plataforma possui um conjunto de componentes de interface (botões, menus, janelas) com aparência e comportamentos próprios.

Como funciona:

- Uma interface GUIFactory define métodos para criar os componentes necessários, como criarBotao() e criarMenu().
  - Implementações concretas, como WindowsFactory e MacFactory, fornecem os componentes específicos para cada ambiente.

Benefícios:

- Garante que todos os componentes criados por uma fábrica sejam compatíveis entre si, possibilitando uma fácil troca de “estilo” ou de plataforma sem alterar o código que utiliza esses componentes.

Ponderações:

- Isolamento de Implementação: O cliente não precisa conhecer as classes concretas dos componentes;
  - ele trabalha apenas com as interfaces.

- Facilidade de Manutenção e Extensão: Para adicionar suporte a uma nova plataforma, basta criar novas implementações dos produtos e uma nova fábrica, sem alterar o código do cliente.
- Consistência dos Componentes: A Abstract Factory garante que todos os componentes criados por uma fábrica sejam compatíveis entre si, mantendo a uniformidade da interface.
