package A02_ARA0101_PPJ_CG.aula12.visitor;

class PessoaFisica implements Cliente {
    String nome;
    String cpf;

    public PessoaFisica(String nome, String cpf) {
        this.nome = nome;
        this.cpf = cpf;
    }

    public void aceitar(RelatorioClienteVisitor visitor) {
        visitor.visitar(this);
    }
}