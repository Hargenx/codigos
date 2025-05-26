package A08_ARA0075_PPS_NA.aula05.padrao_prototype;

import java.util.HashMap;
import java.util.Map;

public class AmbientePrototypeRegistry {

    private static Map<String, AmbienteConfig> prototipos = new HashMap<>();

    // Inicializa alguns protótipos padrão
    static {
        // Protótipo de Desenvolvimento
        DesenvolvimentoConfig devConfig = new DesenvolvimentoConfig(
                "http://dev.local", "devUser", "devPass", 30, true);
        prototipos.put("DEV", devConfig);

        // Protótipo de Produção
        ProducaoConfig prodConfig = new ProducaoConfig(
                "https://prod.suaempresa.com", "prodUser", "prodPass", 120, false);
        prototipos.put("PROD", prodConfig);
    }

    // Retorna uma cópia (clone) do protótipo solicitado
    public static AmbienteConfig getPrototipo(String tipo) {
        AmbienteConfig config = prototipos.get(tipo);
        if (config != null) {
            return config.clone(); // Clona o objeto original
        }
        throw new IllegalArgumentException("Protótipo não encontrado: " + tipo);
    }
}
