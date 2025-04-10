package A08_ARA0075_PPS_NA.aula08.Proxy;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        CotacaoService service = new CotacaoProxy();

        System.out.println("Cotação: " + service.getCotacaoDolar());
        Thread.sleep(1000);
        System.out.println("Cotação: " + service.getCotacaoDolar());
    }
}