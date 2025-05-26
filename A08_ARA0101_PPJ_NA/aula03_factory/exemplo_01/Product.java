package A08_ARA0075_PPS_NA.aula03_factory.exemplo_01;

// Classe representando um produto
class Product {
    private String name;

    public Product(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return name;
    }
}