import FactoryMethod.Veiculo;

public class Moto implements Veiculo {
    @Override
    public void dirigir() {
        System.out.println("Pilotando uma moto.");
    }
}
