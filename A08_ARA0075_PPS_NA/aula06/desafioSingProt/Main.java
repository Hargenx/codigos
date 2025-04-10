package desafioSingProt;

public class Main {
    public static void main(String[] args) {
        // Obtém a instância única do ConfigManager
        ConfigManager config = ConfigManager.getInstancia();

        // Exibe a configuração e o protótipo atual
        System.out.println("Configuração atual: " + config.getConfiguracao());
        System.out.println("Prototipo de Documento: " + config.getPrototipoDocumento());

        // Cria um novo documento clonando o protótipo
        Documento novoDocumento = config.getPrototipoDocumento().clone();
        // Personaliza o novo documento
        novoDocumento.setTitulo("Contrato do Cliente ABC");
        novoDocumento.setConteudo("Conteúdo personalizado para o cliente ABC.");

        // Exibe o novo documento
        System.out.println("Novo Documento: " + novoDocumento);
    }
}
