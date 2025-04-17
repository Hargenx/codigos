package A08_ARA0075_PPS_NA.aula09.iterator;

import java.util.List;

public class PlaylistIterador implements Iterador<String> {
    private List<String> lista;
    private int pos = 0;

    public PlaylistIterador(List<String> lista) {
        this.lista = lista;
    }

    public boolean temProximo() {
        return pos < lista.size();
    }

    public String proximo() {
        return lista.get(pos++);
    }
}
