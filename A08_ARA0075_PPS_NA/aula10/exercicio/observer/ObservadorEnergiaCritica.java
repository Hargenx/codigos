package A08_ARA0075_PPS_NA.aula10.exercicio.observer;

public class ObservadorEnergiaCritica implements Observador {
    public void atualizar(int energia) {
        if (energia < 20) {
            System.out.println("⚠️ Energia crítica! Energia atual: " + energia);
        }
    }
}
