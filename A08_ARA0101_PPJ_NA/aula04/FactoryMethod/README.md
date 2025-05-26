# Aplicativo de Transporte

Imagine um aplicativo de transporte (semelhante ao Uber) que precisa oferecer diferentes tipos de veículos conforme a disponibilidade ou a preferência do usuário. Cada veículo pode ser um Carro, Moto ou Bicicleta – todos implementando a mesma interface, por exemplo, Veiculo.

Como funciona:

- Uma classe abstrata, digamos VeiculoFactory, define o método criarVeiculo().
- Cada subclasse concreta (como CarroFactory, MotoFactory e BicicletaFactory) implementa esse método para instanciar o veículo adequado.

Benefícios:

- Permite a criação dinâmica dos objetos sem acoplamento direto com as classes concretas, facilitando a manutenção e a expansão do sistema (por exemplo, adicionando um novo tipo de veículo).

Ponderações:

- Desacoplamento: O cliente não precisa conhecer as classes concretas, apenas utiliza a interface Veiculo e a fábrica correspondente.
- Flexibilidade: Para adicionar um novo tipo de veículo, basta criar uma nova classe que implemente Veiculo e sua fábrica correspondente, sem alterar o código do cliente.
- Manutenção: Facilita a manutenção e a extensão do sistema, pois a lógica de criação está centralizada nas fábricas.

Este exemplo ilustra como o padrão Factory Method permite a criação flexível de objetos, promovendo uma arquitetura mais modular e fácil de manter.
