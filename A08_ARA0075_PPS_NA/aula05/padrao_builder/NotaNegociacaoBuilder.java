package A08_ARA0075_PPS_NA.aula05.padrao_builder;

// Interface do Builder que define os passos de construção
public interface NotaNegociacaoBuilder {
    void buildCabecalho();

    void buildOperacoes();

    void buildSumario();

    NotaNegociacao getNota();
}