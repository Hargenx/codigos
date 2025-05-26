package A02_ARA0101_PPJ_CG.aula12.template_method;

class ImportadorCSV extends ImportadorArquivo {
    protected void abrirArquivo() {
        System.out.println("Abrindo arquivo CSV...");
    }

    protected void lerDados() {
        System.out.println("Lendo linhas CSV...");
    }

    protected void processarDados() {
        System.out.println("Processando registros CSV...");
    }

    protected void fecharArquivo() {
        System.out.println("Fechando CSV.");
    }
}