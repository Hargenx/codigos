package A02_ARA0101_PPJ_CG.aula12.visitor;

class PessoaJuridica implements Cliente {
    String razaoSocial;
    String cnpj;

    public PessoaJuridica(String razao, String cnpj) {
        this.razaoSocial = razao;
        this.cnpj = cnpj;
    }

    public void aceitar(RelatorioClienteVisitor visitor) {
        visitor.visitar(this);
    }
}