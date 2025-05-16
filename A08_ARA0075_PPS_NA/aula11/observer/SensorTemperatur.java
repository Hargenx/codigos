package A08_ARA0075_PPS_NA.aula11.observer;

import java.util.ArrayList;
import java.util.List;

class SensorTemperatura {
    private List<Observador> observadores = new ArrayList<>();
    private double temperatura;

    public void adicionarObservador(Observador o) {
        observadores.add(o);
    }

    public void setTemperatura(double temp) {
        this.temperatura = temp;
        notificar();
    }

    private void notificar() {
        for (Observador o : observadores) {
            o.atualizar(temperatura);
        }
    }
}