package A08_ARA0075_PPS_NA.aula04.FactoryMethod;

public class CarroFactory extends VeiculoFactory {
    @Override
    public Veiculo criarVeiculo() {
        return new Carro();
    }
}
