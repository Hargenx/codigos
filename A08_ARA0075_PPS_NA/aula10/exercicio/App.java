package A08_ARA0075_PPS_NA.aula10.exercicio;

import A08_ARA0075_PPS_NA.aula10.exercicio.observer.ObservadorEnergiaCritica;
import A08_ARA0075_PPS_NA.aula10.exercicio.strategy.AtaqueEspada;
import A08_ARA0075_PPS_NA.aula10.exercicio.strategy.AtaqueMagia;

public class App {
    public static void main(String[] args) {
        Personagem heroi = new Personagem("Arthas", 100, 50);
        heroi.adicionarObservador(new ObservadorEnergiaCritica());

        heroi.setAtaque(new AtaqueEspada());
        heroi.atacar();

        heroi.salvarEstado(); // salvar estado inicial

        heroi.receberDano(30);
        heroi.gastarEnergia(35); // deverá notificar energia crítica

        heroi.restaurarEstado(); // retorna ao estado salvo

        heroi.setAtaque(new AtaqueMagia());
        heroi.atacar();
    }
}
