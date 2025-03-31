package singleton.exemploLogger;

// Classe com método main para demonstrar o uso do Singleton
public class MainSingleton {
    public static void main(String[] args) {
        // Obtendo a instância única do Logger
        Logger logger1 = Logger.getInstancia();
        Logger logger2 = Logger.getInstancia();

        // Utilizando o logger para registrar mensagens
        logger1.log("Iniciando aplicação...");
        logger2.log("Continuando execução...");

        // Verifica se ambas as referências apontam para a mesma instância
        if (logger1 == logger2) {
            System.out.println("logger1 e logger2 são a mesma instância.");
        }
    }
}