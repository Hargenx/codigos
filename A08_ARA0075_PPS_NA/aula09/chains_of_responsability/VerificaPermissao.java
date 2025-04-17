public class VerificaPermissao extends VerificadorBase {
    public boolean processar(String email, String senha) {
        if (!email.startsWith("admin")) {
            System.out.println("🔒Acesso negado: Sem permissão.");
            return false;
        }
        return true;
    }
}