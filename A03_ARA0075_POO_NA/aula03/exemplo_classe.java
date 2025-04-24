package A03_ARA0075_POO_NA.aula03;

class Pessoa {
    private int codigo;
    private String nome;
    private String email;

    public Pessoa() {
    }

    public Pessoa(int codigo, String nome, String email) {
        this.codigo = codigo;
        this.nome = nome;
        this.email = email;
    }

    public int getCodigo() {
        return codigo;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    @Override
    public String toString() {
        return "Código: " + codigo + "\nNome: " + nome + "\nEmail: " + email;
    }
}
public class exemplo_classe {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa(1, "Raphael", "raphael@email.com");
        System.out.println(p1.toString());
    }
}
