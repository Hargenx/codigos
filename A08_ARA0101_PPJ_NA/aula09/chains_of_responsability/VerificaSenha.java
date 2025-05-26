package A08_ARA0075_PPS_NA.aula09.chains_of_responsability;

public class VerificaSenha extends VerificadorBase {
    public boolean processar(String email, String senha) {
        if (!senha.equals("123456")) {
            System.out.println("🔒Senha incorreta");
            return false;
        }
        return processarProximo(email, senha);
    }
}