package A08_ARA0075_PPS_NA.aula05.padrao_builder;

// Classe principal para teste
public class Main {
    public static void main(String[] args) {
        // Exportação para PDF
        NotaNegociacaoBuilder pdfBuilder = new PdfNotaNegociacaoBuilder();
        NotaNegociacaoDirector director = new NotaNegociacaoDirector(pdfBuilder);
        director.construirNota();
        NotaNegociacao notaPdf = pdfBuilder.getNota();
        System.out.println("Nota em PDF:");
        System.out.println(notaPdf.getConteudo());

        // Exportação para XML
        NotaNegociacaoBuilder xmlBuilder = new XmlNotaNegociacaoBuilder();
        director = new NotaNegociacaoDirector(xmlBuilder);
        director.construirNota();
        NotaNegociacao notaXml = xmlBuilder.getNota();
        System.out.println("Nota em XML:");
        System.out.println(notaXml.getConteudo());

        // Exportação para XLS
        NotaNegociacaoBuilder xlsBuilder = new XlsNotaNegociacaoBuilder();
        director = new NotaNegociacaoDirector(xlsBuilder);
        director.construirNota();
        NotaNegociacao notaXls = xlsBuilder.getNota();
        System.out.println("Nota em XLS:");
        System.out.println(notaXls.getConteudo());
    }
}
