package A08_ARA0075_PPS_NA.aula10.strategy;

public class PAC implements FreteStrategy {
    public double calcular(double peso) {
        return 15 + peso * 1.5;
    }
}
