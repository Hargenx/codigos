import FactoryMethod.Veiculo;

public class Carro implements Veiculo {
    @Override
    public void dirigir() {
        System.out.println("Dirigindo um carro.");
    }
}