package A08_ARA0075_PPS_NA.aula05.padrao_builder;

// Produto final: representa a nota de negociação
public class NotaNegociacao {
    private StringBuilder conteudo;

    public NotaNegociacao() {
        this.conteudo = new StringBuilder();
    }

    public void adicionarConteudo(String parte) {
        conteudo.append(parte).append("\n");
    }

    public String getConteudo() {
        return conteudo.toString();
    }
}