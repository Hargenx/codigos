package A08_ARA0075_PPS_NA.aula05.padrao_builder;

// Builder concreto para formato XML
public class XmlNotaNegociacaoBuilder implements NotaNegociacaoBuilder {
    private NotaNegociacao nota;

    public XmlNotaNegociacaoBuilder() {
        this.nota = new NotaNegociacao();
    }

    @Override
    public void buildCabecalho() {
        nota.adicionarConteudo("<cabecalho>XML: Cabeçalho da Nota</cabecalho>");
    }

    @Override
    public void buildOperacoes() {
        nota.adicionarConteudo("<operacoes>XML: Lista de operações</operacoes>");
    }

    @Override
    public void buildSumario() {
        nota.adicionarConteudo("<sumario>XML: Sumário com totais e taxas</sumario>");
    }

    @Override
    public NotaNegociacao getNota() {
        return nota;
    }
}