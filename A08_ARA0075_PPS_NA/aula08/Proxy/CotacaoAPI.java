package A08_ARA0075_PPS_NA.aula08.Proxy;

public class CotacaoAPI implements CotacaoService {
    public double getCotacaoDolar() {
        System.out.println("Consultando API externa...");
        return 5.23; // Simulação da resposta da API
    }
}
