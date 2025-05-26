package A08_ARA0075_PPS_NA.aula05.padrao_prototype;

public class Main {
    public static void main(String[] args) {
        // Obtém uma configuração de Desenvolvimento (clone do protótipo)
        AmbienteConfig devClone = AmbientePrototypeRegistry.getPrototipo("DEV");
        devClone.exibirInfo();

        // Podemos customizar esse clone, se necessário
        devClone.setUrl("http://dev.featureX.local");
        devClone.setUsuario("devFeatureUser");
        devClone.setTimeoutSegundos(45);
        devClone.exibirInfo();

        // Obtém uma configuração de Produção (clone do protótipo)
        AmbienteConfig prodClone = AmbientePrototypeRegistry.getPrototipo("PROD");
        prodClone.exibirInfo();

        // Personaliza se necessário
        prodClone.setUrl("https://prod-novo.suaempresa.com");
        prodClone.setSenha("senhaNova123");
        prodClone.exibirInfo();
    }
}
