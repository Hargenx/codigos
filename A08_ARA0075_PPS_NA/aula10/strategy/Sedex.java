package A08_ARA0075_PPS_NA.aula10.strategy;

public class Sedex implements FreteStrategy {
    public double calcular(double peso) {
        return 20 + peso * 2;
    }
}