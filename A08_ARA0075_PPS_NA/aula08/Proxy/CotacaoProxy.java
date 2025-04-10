package A08_ARA0075_PPS_NA.aula08.Proxy;

import java.time.Duration;
import java.time.LocalDateTime;

public class CotacaoProxy implements CotacaoService {
    private CotacaoAPI cotacaoReal = new CotacaoAPI();
    private double cache;
    private LocalDateTime ultimaConsulta;

    public double getCotacaoDolar() {
        if (ultimaConsulta == null || Duration.between(ultimaConsulta, LocalDateTime.now()).getSeconds() > 30) {
            cache = cotacaoReal.getCotacaoDolar();
            ultimaConsulta = LocalDateTime.now();
        } else {
            System.out.println("Retornando cotação do cache.");
        }
        return cache;
    }
}
