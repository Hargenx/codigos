package A08_ARA0075_PPS_NA.aula10.exercicio;

import java.util.ArrayList;
import java.util.List;

import A08_ARA0075_PPS_NA.aula10.exercicio.memento.EstadoPersonagem;
import A08_ARA0075_PPS_NA.aula10.exercicio.memento.HistoricoPersonagem;
import A08_ARA0075_PPS_NA.aula10.exercicio.observer.Observador;
import A08_ARA0075_PPS_NA.aula10.exercicio.strategy.Ataque;

public class Personagem {
    private String nome;
    private int vida;
    private int energia;
    private Ataque estrategiaDeAtaque;
    private List<Observador> observadores = new ArrayList<>();
    private HistoricoPersonagem historico = new HistoricoPersonagem();

    public Personagem(String nome, int vida, int energia) {
        this.nome = nome;
        this.vida = vida;
        this.energia = energia;
    }

    public void setAtaque(Ataque ataque) {
        this.estrategiaDeAtaque = ataque;
    }

    public void atacar() {
        if (estrategiaDeAtaque != null) {
            estrategiaDeAtaque.executar();
        } else {
            System.out.println("Nenhuma estratégia de ataque definida.");
        }
    }

    public void receberDano(int dano) {
        vida -= dano;
        System.out.println(nome + " recebeu " + dano + " de dano. Vida atual: " + vida);
    }

    public void gastarEnergia(int qtd) {
        energia -= qtd;
        System.out.println(nome + " gastou " + qtd + " de energia. Energia atual: " + energia);
        notificar();
    }

    public void salvarEstado() {
        historico.salvar(new EstadoPersonagem(vida, energia));
        System.out.println("💾 Estado salvo.");
    }

    public void restaurarEstado() {
        EstadoPersonagem estado = historico.restaurar();
        if (estado != null) {
            this.vida = estado.getVida();
            this.energia = estado.getEnergia();
            System.out.println("🔄 Estado restaurado: Vida = " + vida + ", Energia = " + energia);
        } else {
            System.out.println("⚠️ Nenhum estado anterior para restaurar.");
        }
    }

    public void adicionarObservador(Observador o) {
        observadores.add(o);
    }

    private void notificar() {
        for (Observador o : observadores) {
            o.atualizar(energia);
        }
    }
}
