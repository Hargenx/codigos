package A08_ARA0075_PPS_NA.aula06.desafioSingProt;

public class ConfigManager {
    // Atributo estático para armazenar a única instância
    private static ConfigManager instancia;

    private String configuracao;
    private Documento prototipoDocumento;

    // Construtor privado para evitar criação externa
    private ConfigManager() {
        // Configuração padrão, por exemplo, o formato dos documentos
        this.configuracao = "Formato Padrão";
        // Instancia um protótipo de Documento com valores iniciais
        this.prototipoDocumento = new Documento("Documento Padrão", "Conteúdo Padrão", configuracao);
    }

    // Método estático para obter a instância única do ConfigManager
    public static ConfigManager getInstancia() {
        if (instancia == null) {
            instancia = new ConfigManager();
        }
        return instancia;
    }

    // Getters e Setters
    public String getConfiguracao() {
        return configuracao;
    }

    public void setConfiguracao(String configuracao) {
        this.configuracao = configuracao;
    }

    public Documento getPrototipoDocumento() {
        return prototipoDocumento;
    }

    public void setPrototipoDocumento(Documento prototipoDocumento) {
        this.prototipoDocumento = prototipoDocumento;
    }
}
