package A08_ARA0075_PPS_NA.aula04.FactoryMethod;

public class Main {
    public static void main(String[] args) {
        // Utilizando a fábrica de Carro
        VeiculoFactory factory = new CarroFactory();
        Veiculo veiculo = factory.criarVeiculo();
        veiculo.dirigir(); // Saída: "Dirigindo um carro."

        // Utilizando a fábrica de Moto
        factory = new MotoFactory();
        veiculo = factory.criarVeiculo();
        veiculo.dirigir(); // Saída: "Pilotando uma moto."

        // Utilizando a fábrica de Bicicleta
        factory = new BicicletaFactory();
        veiculo = factory.criarVeiculo();
        veiculo.dirigir(); // Saída: "Pedalando uma bicicleta."
    }
}
