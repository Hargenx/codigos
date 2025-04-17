package A08_ARA0075_PPS_NA.aula09.iterator;

import java.util.ArrayList;
import java.util.List;

public class Playlist {
    private List<String> musicas = new ArrayList<>();

    public void adicionarMusica(String nome) {
        musicas.add(nome);
    }

    public Iterador<String> criarIterador() {
        return new PlaylistIterador(musicas);
    }
}
