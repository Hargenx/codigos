package A02_ARA0101_PPJ_CG.aula12.template_method;

class ImportadorXML extends ImportadorArquivo {
    protected void abrirArquivo() {
        System.out.println("Abrindo arquivo XML...");
    }

    protected void lerDados() {
        System.out.println("Lendo nós XML...");
    }

    protected void processarDados() {
        System.out.println("Processando elementos XML...");
    }

    protected void fecharArquivo() {
        System.out.println("Fechando XML.");
    }
}