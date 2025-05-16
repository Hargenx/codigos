package A08_ARA0075_PPS_NA.aula11.observer;

class ExibidorTemperatura implements Observador {
    public void atualizar(double temperatura) {
        System.out.println("Temperatura atual: " + temperatura + " °C");
    }
}