public class BicicletaFactory extends VeiculoFactory {
    @Override
    public Veiculo criarVeiculo() {
        return new Bicicleta();
    }
}
