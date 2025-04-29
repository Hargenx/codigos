package A08_ARA0075_PPS_NA.aula08.Proxy;

public class CotacaoAPI implements CotacaoService {
    public double getCotacaoDolar() {
        double cota = 0.0;
        System.out.println("Consultando API externa...");
        try {
            Thread.sleep(1000); // Simula o tempo de resposta da API
            cota = 5.25 + (Math.random() * 2); // Simulação de uma cotação de dólar
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return cota; // Simulação da resposta da API
    }
}
