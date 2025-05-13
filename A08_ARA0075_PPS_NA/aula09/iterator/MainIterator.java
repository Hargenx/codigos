package A08_ARA0075_PPS_NA.aula09.iterator;

public class MainIterator {
    public static void main(String[] args) {
        Playlist playlist = new Playlist();
        playlist.adicionarMusica("Pearl jam - Elderly Woman Behind the Counter in a Small Town");
        playlist.adicionarMusica("Metallica - Nothing Else Matters");
        playlist.adicionarMusica("Angra - Carry On");
        playlist.adicionarMusica("Iron Maiden - Fear of the Dark");
        playlist.adicionarMusica("Offspring - The Kids Aren't Alright");
        playlist.adicionarMusica("Nirvana - Smells Like Teen Spirit");
        playlist.adicionarMusica("Red Hot Chili Peppers - Californication");
        playlist.adicionarMusica("Linkin Park - In the End");
        playlist.adicionarMusica("Green Day - Boulevard of Broken Dreams");
        playlist.adicionarMusica("Foo Fighters - Everlong");
        playlist.adicionarMusica("System of a Down - Chop Suey");
        playlist.adicionarMusica("Rage Against the Machine - Killing in the Name");
        playlist.adicionarMusica("Megadeth - Symphony of Destruction");
        playlist.adicionarMusica("Slipknot - Duality");

        Iterador<String> it = playlist.criarIterador();
        while (it.temProximo()) {
            System.out.println("▶ Tocando: " + it.proximo());
        }
    }
}
