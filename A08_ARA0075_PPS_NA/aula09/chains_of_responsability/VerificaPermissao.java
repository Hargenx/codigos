package A08_ARA0075_PPS_NA.aula09.chains_of_responsability;

public class VerificaPermissao extends VerificadorBase {
    public boolean processar(String email, String senha) {
        if (!email.startsWith("admin")) {
            System.out.println("🔒Acesso negado: Sem permissão.");
            return false;
        }
        return true;
    }
}