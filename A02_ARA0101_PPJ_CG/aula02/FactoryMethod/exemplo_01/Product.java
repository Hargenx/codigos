package A02_ARA0101_PPJ_CG.aula02.FactoryMethod.exemplo_01;

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