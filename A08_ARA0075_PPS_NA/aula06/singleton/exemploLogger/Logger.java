package singleton.exemploLogger;

// Classe Singleton para gerenciamento de logs
public class Logger {
    // Variável privada que guarda a única instância da classe
    private static Logger instancia;

    // Construtor privado para evitar instanciamento externo
    private Logger() {
    }

    // Método público para obter a instância única da classe
    public static Logger getInstancia() {
        if (instancia == null) {
            instancia = new Logger();
        }
        return instancia;
    }

    public void log(String mensagem) {
        System.out.println("[LOG] " + mensagem);
    }
}
