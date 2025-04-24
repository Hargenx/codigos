package A03_ARA0075_POO_NA.aula04;

// Classe principal para testar os modificadores
public class Exemplo {
    public static void main(String[] args) {
        MinhaClasse obj = new MinhaClasse();

        // Acessando atributos
        System.out.println("Atributo default: " + obj.defaultAtributo);
        System.out.println("Atributo protected: " + obj.protectedAtributo);
        System.out.println("Atributo public: " + obj.publicAtributo);
        // A linha abaixo geraria erro, pois privateAtributo não é acessível fora da classe
        // System.out.println("Atributo private: " + obj.privateAtributo);

        // Chamando métodos
        obj.defaultMetodo();
        obj.protectedMetodo();
        obj.publicMetodo();
        // A linha abaixo geraria erro, pois privateMetodo não é acessível fora da
        // classe
        // obj.privateMetodo();
        obj.chamarPrivate(); // Método que internamente chama o método private

        // Criando uma subclasse e demonstrando o acesso aos membros herdados
        SubClasse sub = new SubClasse();
        sub.acessarAtributos();
    }
}

// Subclasse que herda de MinhaClasse
class SubClasse extends MinhaClasse {
    void acessarAtributos() {
        System.out.println("\nNa SubClasse:");
        // Pode acessar atributos default, protected e public da classe pai
        System.out.println("Atributo default: " + defaultAtributo);
        System.out.println("Atributo protected: " + protectedAtributo);
        System.out.println("Atributo public: " + publicAtributo);
        // A linha abaixo geraria erro, pois privateAtributo não é herdado
        // System.out.println("Atributo private: " + privateAtributo);

        // Chamando métodos herdados
        defaultMetodo();
        protectedMetodo();
        publicMetodo();
        // A linha abaixo geraria erro, pois privateMetodo não é acessível
        // privateMetodo();
    }
}
