package A02_ARA0101_PPJ_CG.aula12.template_method;



public class Main {
    public static void main(String[] args) {
        ImportadorArquivo importadorCSV = new ImportadorCSV();
        importadorCSV.importar();

        System.out.println();

        ImportadorArquivo importadorXML = new ImportadorXML();
        importadorXML.importar();
    }
}