package A08_ARA0075_PPS_NA.aula08.Facade;

public class LojaFacade {
    private Estoque estoque = new Estoque();
    private Pagamento pagamento = new Pagamento();
    private Envio envio = new Envio();

    public void comprarFilme() {
        if (estoque.verificarDisponibilidade()) {
            pagamento.processarPagamento();
            envio.enviar();
        }
    }
}