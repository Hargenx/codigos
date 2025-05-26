package A02_ARA0101_PPJ_CG.aula12.visitor;

public class Main {
    public static void main(String[] args) {
        Cliente cliente1 = new PessoaFisica("Raphael", "123.456.789-00");
        Cliente cliente2 = new PessoaJuridica("Empresa X", "12.345.678/0001-90");

        RelatorioClienteVisitor relatorio = new GeradorRelatorio();

        cliente1.aceitar(relatorio);
        cliente2.aceitar(relatorio);
    }
}