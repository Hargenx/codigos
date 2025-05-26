package A08_ARA0075_PPS_NA.aula10.memento;

public class App {
    public static void main(String[] args) {
        Jogo jogo = new Jogo();
        ControleJogo controle = new ControleJogo();

        controle.salvar(jogo.salvar()); // posição inicial
        jogo.moverPara("B2");

        controle.salvar(jogo.salvar());
        jogo.moverPara("C3");

        // desfazer última jogada
        jogo.restaurar(controle.desfazer());
        // desfazer novamente
        jogo.restaurar(controle.desfazer());
    }
}
