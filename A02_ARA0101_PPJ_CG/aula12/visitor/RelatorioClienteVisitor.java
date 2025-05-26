package A02_ARA0101_PPJ_CG.aula12.visitor;

interface RelatorioClienteVisitor {
    void visitar(PessoaFisica pf);

    void visitar(PessoaJuridica pj);
}