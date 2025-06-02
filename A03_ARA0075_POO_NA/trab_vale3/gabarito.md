# O que deve ser entregue

1. **Código Java completo** para todas as classes do diagrama UML acima.
2. Um método `main(String[] args)` que:

   * Crie pelo menos **um Desenvolvedor** e **um Gerente** (com dados aceitáveis).
   * Chame `inserir(...)` em `FuncionarioDAO` para salvar esses objetos no banco.
   * Recupere esses funcionários chamando `buscarPorId(...)` ou `listarTodos()` e imprima nome e salário calculado no console.
   * Demonstre o tratamento de exceção lançando, por exemplo, `IllegalArgumentException` se o salárioBase for negativo.
3. **Instruções de uso** (comentadas no código ou em README curto) explicando:

   * Como criar a tabela no banco (ex.: MySQL ou PostgreSQL).
   * Onde configurar URL, usuário e senha do JDBC no construtor de `FuncionarioDAO`.
   * Como compilar e executar em linha de comando (sem IDE).

---

## Detalhamento dos requisitos

### 1. Modelagem orientada a objetos

* **Classe abstrata** `Funcionario`:

  * Atributos **privados**:

    * `int id`
    * `String nome`
    * `double salarioBase`
  * Construtor público que receba `(int id, String nome, double salarioBase)`.
  * Getters para cada atributo (`getId()`, `getNome()`, `getSalarioBase()`).
  * Método abstrato `public abstract double calcularSalario()`.

* **Classe** `Desenvolvedor` (extends `Funcionario`):

  * Atributo **privado** `String linguagem`.
  * Construtor que receba `(int id, String nome, double salarioBase, String linguagem)`.

    * Use `super(id, nome, salarioBase)` para inicializar a superclasse.
    * Lance `IllegalArgumentException` se `salarioBase < 0` ou `linguagem == null || linguagem.isEmpty()`.
  * Getter `public String getLinguagem()`.
  * Sobrescreva `public double calcularSalario()`:

    * Se `linguagem.equalsIgnoreCase("Java")`, retorne `salarioBase * 1.10`;
    * Senão, retorne apenas `salarioBase`.

* **Classe** `Gerente` (extends `Funcionario`):

  * Atributo **privado** `double bonus`.
  * Construtor que receba `(int id, String nome, double salarioBase, double bonus)`.

    * Use `super(id, nome, salarioBase)`.
    * Lance `IllegalArgumentException` se `salarioBase < 0` ou `bonus < 0`.
  * Getter `public double getBonus()`.
  * Sobrescreva `public double calcularSalario()`: retorne `salarioBase + bonus`.

### 2. Tratamento de exceções

* Em cada construtor de subclass (`Desenvolvedor`, `Gerente`), lance

  ```java
  if (salarioBase < 0) 
      throw new IllegalArgumentException("salarioBase não pode ser negativo");
  ```

* Similar para `linguagem` vazia ou `bonus < 0`.
* No DAO, ao inserir, capture possíveis `SQLException` e relance (ou imprima a mensagem).
* No `main`, envolva chamadas a `inserir(...)` em `try/catch` e imprima no console “Erro: \<mensagem da exceção>”.

### 3. Integração com banco de dados (JDBC)

* **Tabela SQL sugerida** (MySQL/ PostgreSQL):

  ```sql
  CREATE TABLE Funcionario (
      id INT PRIMARY KEY,
      nome VARCHAR(100) NOT NULL,
      salario_base DOUBLE NOT NULL,
      tipo VARCHAR(20) NOT NULL,      -- “DESENVOLVEDOR” ou “GERENTE”
      linguagem VARCHAR(50),          -- usado apenas se for Desenvolvedor
      bonus DOUBLE                    -- usado apenas se for Gerente
  );
  ```

  > **Observação:** Os campos `linguagem` e `bonus` podem ficar `NULL` quando não se aplicam.

* **Classe** `FuncionarioDAO`:

  ```java
  public class FuncionarioDAO {
      private final String url;
      private final String usuario;
      private final String senha;

      public FuncionarioDAO(String url, String usuario, String senha) {
          this.url = url;
          this.usuario = usuario;
          this.senha = senha;
      }

      private Connection conectar() throws SQLException {
          return DriverManager.getConnection(url, usuario, senha);
      }

      public void inserir(Funcionario f) throws SQLException {
          // validação extra em caso de dados inválidos:
          if (f.getSalarioBase() < 0) {
              throw new IllegalArgumentException("Salário-base não pode ser negativo");
          }

          String sql = "INSERT INTO Funcionario (id, nome, salario_base, tipo, linguagem, bonus) "
                     + "VALUES (?, ?, ?, ?, ?, ?)";
          try (Connection conn = conectar();
               PreparedStatement ps = conn.prepareStatement(sql)) {
              ps.setInt(1, f.getId());
              ps.setString(2, f.getNome());
              ps.setDouble(3, f.getSalarioBase());
              if (f instanceof Desenvolvedor) {
                  Desenvolvedor d = (Desenvolvedor) f;
                  ps.setString(4, "DESENVOLVEDOR");
                  ps.setString(5, d.getLinguagem());
                  ps.setNull(6, java.sql.Types.DOUBLE);
              } else if (f instanceof Gerente) {
                  Gerente g = (Gerente) f;
                  ps.setString(4, "GERENTE");
                  ps.setNull(5, java.sql.Types.VARCHAR);
                  ps.setDouble(6, g.getBonus());
              } else {
                  // caso outra subclasse futuramente
                  ps.setString(4, "FUNCIONARIO");
                  ps.setNull(5, java.sql.Types.VARCHAR);
                  ps.setNull(6, java.sql.Types.DOUBLE);
              }
              ps.executeUpdate();
          }
      }

      public Funcionario buscarPorId(int id) throws SQLException {
          String sql = "SELECT * FROM Funcionario WHERE id = ?";
          try (Connection conn = conectar();
               PreparedStatement ps = conn.prepareStatement(sql)) {
              ps.setInt(1, id);
              try (ResultSet rs = ps.executeQuery()) {
                  if (rs.next()) {
                      String tipo = rs.getString("tipo");
                      String nome = rs.getString("nome");
                      double salarioBase = rs.getDouble("salario_base");
                      if ("DESENVOLVEDOR".equalsIgnoreCase(tipo)) {
                          String linguagem = rs.getString("linguagem");
                          return new Desenvolvedor(id, nome, salarioBase, linguagem);
                      } else if ("GERENTE".equalsIgnoreCase(tipo)) {
                          double bonus = rs.getDouble("bonus");
                          return new Gerente(id, nome, salarioBase, bonus);
                      } else {
                          // Caso futuramente haja outros tipos
                          return null;
                      }
                  } else {
                      return null;
                  }
              }
          }
      }

      public List<Funcionario> listarTodos() throws SQLException {
          List<Funcionario> lista = new ArrayList<>();
          String sql = "SELECT * FROM Funcionario";
          try (Connection conn = conectar();
               PreparedStatement ps = conn.prepareStatement(sql);
               ResultSet rs = ps.executeQuery()) {
              while (rs.next()) {
                  int id = rs.getInt("id");
                  String tipo = rs.getString("tipo");
                  String nome = rs.getString("nome");
                  double salarioBase = rs.getDouble("salario_base");
                  if ("DESENVOLVEDOR".equalsIgnoreCase(tipo)) {
                      String linguagem = rs.getString("linguagem");
                      lista.add(new Desenvolvedor(id, nome, salarioBase, linguagem));
                  } else if ("GERENTE".equalsIgnoreCase(tipo)) {
                      double bonus = rs.getDouble("bonus");
                      lista.add(new Gerente(id, nome, salarioBase, bonus));
                  }
              }
          }
          return lista;
      }
  }
  ```

#### 4. Exemplo de `main`

```java
import java.sql.SQLException;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // ► Ajuste a URL, usuário e senha conforme seu banco
        String url = "jdbc:mysql://localhost:3306/meubanco";
        String usuario = "root";
        String senha = "1234";

        FuncionarioDAO dao = new FuncionarioDAO(url, usuario, senha);

        try {
            // 1. Criação dos objetos
            Desenvolvedor dev = new Desenvolvedor(1, "Alice Souza", 5000.0, "Java");
            Gerente ger = new Gerente(2, "Bruno Lima", 7000.0, 2000.0);

            // 2. Inserir no banco
            dao.inserir(dev);
            dao.inserir(ger);

            // 3. Buscar por ID e imprimir
            Funcionario f1 = dao.buscarPorId(1);
            Funcionario f2 = dao.buscarPorId(2);

            System.out.println("Dados do funcionário ID=1:");
            System.out.println("Nome: " + f1.getNome());
            System.out.println("Salário Calculado: " + f1.calcularSalario());

            System.out.println();

            System.out.println("Dados do funcionário ID=2:");
            System.out.println("Nome: " + f2.getNome());
            System.out.println("Salário Calculado: " + f2.calcularSalario());

            // 4. Listar todos
            System.out.println("\n=== Lista de Todos os Funcionários no BD ===");
            List<Funcionario> todos = dao.listarTodos();
            for (Funcionario f : todos) {
                System.out.println("ID=" + f.getId()
                    + " | Nome=" + f.getNome()
                    + " | Salário=" + f.calcularSalario());
            }

        } catch (IllegalArgumentException e) {
            System.out.println("Erro de validação: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("Erro de acesso ao banco: " + e.getMessage());
        }
    }
}
```

> **Saída esperada (console)**
>
> ```cmd
> Dados do funcionário ID=1:
> Nome: Alice Souza
> Salário Calculado: 5500.0
>
> Dados do funcionário ID=2:
> Nome: Bruno Lima
> Salário Calculado: 9000.0
>
> === Lista de Todos os Funcionários no BD ===
> ID=1 | Nome=Alice Souza | Salário=5500.0
> ID=2 | Nome=Bruno Lima  | Salário=9000.0
> ```

*(Os valores de salário calculado já incluem o acréscimo de 10 % para “Java” e o bônus do gerente.)*

---

## Resumo dos passos para realização do trabalho

1. **Criar tabela no banco** (execute antes em seu MySQL/PostgreSQL):

   ```sql
   CREATE TABLE Funcionario (
       id INT PRIMARY KEY,
       nome VARCHAR(100) NOT NULL,
       salario_base DOUBLE NOT NULL,
       tipo VARCHAR(20) NOT NULL,
       linguagem VARCHAR(50),
       bonus DOUBLE
   );
   ```

2. **Implementar as classes Java** (`Funcionario`, `Desenvolvedor`, `Gerente`) seguindo o UML e tratando `IllegalArgumentException` em construtores.

3. **Implementar o `FuncionarioDAO`** para abrir conexão via `DriverManager`, inserir e buscar.

   * Certifique-se de fechar `PreparedStatement` e `Connection` usando *try-with-resources*.

4. **Criar o `main`** que instancia o `FuncionarioDAO`, cria objetos, chama `inserir(...)`, faz `buscarPorId(...)`, exibe no console, e inclui tratamento de exceções.

5. **Testar**:

   * Compile todos os `.java`
   * Execute `Main`; confira se imprime corretamente os dados e salários.
   * Alterne propositalmente um salário para valor negativo para ver o “Erro de validação: …”

---

> **Dica final:**
>
> * Mantenha nomes de métodos e atributos **exatos** ao UML para facilitar entendimento.
> * Deixe comentários claros (por exemplo, `// lança exceção se salário inválido`).
> * Verifique que, ao inserir no banco, as colunas `linguagem` e `bonus` sejam definidas como `NULL` quando não usadas.

Bom trabalho!
