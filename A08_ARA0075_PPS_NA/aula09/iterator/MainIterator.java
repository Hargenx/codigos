package A08_ARA0075_PPS_NA.aula09.iterator;

public class MainIterator {
    public static void main(String[] args) {
        Playlist playlist = new Playlist();
        playlist.adicionarMusica("Intro");
        playlist.adicionarMusica("Abertura");
        playlist.adicionarMusica("Encerramento");

        Iterador<String> it = playlist.criarIterador();
        while (it.temProximo()) {
            System.out.println("▶ Tocando: " + it.proximo());
        }
    }
}
