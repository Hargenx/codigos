# Trabalho POO JAVA

> Você irá desenvolver uma pequena aplicação Java de console para gerenciar funcionários, composta por dois tipos: **Desenvolvedor** e **Gerente**.
> O sistema deve:
>
> 1. Demonstrar uso de **programação orientada a objetos** (classes, atributos, métodos).
> 2. Utilizar **herança** e **polimorfismo** para cálculo de salários.
> 3. Implementar **tratamento de exceções** para dados inválidos.
> 4. Fazer integração com um banco de dados relacional (via JDBC) para **inserir** e **consultar** funcionários.
>
> A seguir, há um diagrama UML que define as classes envolvidas. Baseie-se nele para criar seu código.

---

```wsd
@startuml

abstract class Funcionario {
  - id: int
  - nome: String
  - salarioBase: double
  + Funcionario(int id, String nome, double salarioBase)
  + getId(): int
  + getNome(): String
  + getSalarioBase(): double
  + calcularSalario(): double
}

class Desenvolvedor {
  - linguagem: String
  + Desenvolvedor(int id, String nome, double salarioBase, String linguagem)
  + getLinguagem(): String
  + calcularSalario(): double
}

class Gerente {
  - bonus: double
  + Gerente(int id, String nome, double salarioBase, double bonus)
  + getBonus(): double
  + calcularSalario(): double
}

class FuncionarioDAO {
  + FuncionarioDAO(String url, String usuario, String senha)
  + void inserir(Funcionario f) throws SQLException, IllegalArgumentException
  + Funcionario buscarPorId(int id) throws SQLException
  + List<Funcionario> listarTodos() throws SQLException
}

Funcionario <|-- Desenvolvedor
Funcionario <|-- Gerente

@enduml
```
