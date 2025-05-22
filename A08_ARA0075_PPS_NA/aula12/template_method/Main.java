package A08_ARA0075_PPS_NA.aula12.template_method;

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

public class Main {
    public static void main(String[] args) {
        ImportadorArquivo importadorCSV = new ImportadorCSV();
        importadorCSV.importar();

        System.out.println();

        ImportadorArquivo importadorXML = new ImportadorXML();
        importadorXML.importar();
    }
}