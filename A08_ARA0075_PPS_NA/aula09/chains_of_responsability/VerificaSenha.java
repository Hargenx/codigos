public class VerificaSenha extends VerificadorBase {
    public boolean processar(String email, String senha) {
        if (!senha.equals("123456")) {
            System.out.println("🔒Senha incorreta");
            return false;
        }
        return processarProximo(email, senha);
    }
}