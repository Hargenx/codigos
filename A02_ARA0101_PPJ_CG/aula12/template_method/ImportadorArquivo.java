package A02_ARA0101_PPJ_CG.aula12.template_method;

abstract class ImportadorArquivo {
    public final void importar() {
        abrirArquivo();
        lerDados();
        processarDados();
        fecharArquivo();
    }

    protected abstract void abrirArquivo();

    protected abstract void lerDados();

    protected abstract void processarDados();

    protected abstract void fecharArquivo();
}
