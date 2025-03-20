package A08_ARA0075_PPS_NA.aula05.padrao_builder;

// Director: orquestra a construção da nota usando o builder fornecido
public class NotaNegociacaoDirector {
    private NotaNegociacaoBuilder builder;

    public NotaNegociacaoDirector(NotaNegociacaoBuilder builder) {
        this.builder = builder;
    }

    public void construirNota() {
        builder.buildCabecalho();
        builder.buildOperacoes();
        builder.buildSumario();
    }
}