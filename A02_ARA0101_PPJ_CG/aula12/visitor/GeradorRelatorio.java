package A02_ARA0101_PPJ_CG.aula12.visitor;

class GeradorRelatorio implements RelatorioClienteVisitor {
    public void visitar(PessoaFisica pf) {
        System.out.println("Relatório PF: " + pf.nome + ", CPF: " + pf.cpf);
    }

    public void visitar(PessoaJuridica pj) {
        System.out.println("Relatório PJ: " + pj.razaoSocial + ", CNPJ: " + pj.cnpj);
    }
}