package A08_ARA0075_PPS_NA.aula09.chains_of_responsability;

public class VerificaUsuario extends VerificadorBase {
    public boolean processar(String email, String senha) {
        if (!email.equals("admin@empresa.com")) {
            System.out.println("🔒Usuário não encontrado");
            return false;
        }
        return processarProximo(email, senha);
    }
}