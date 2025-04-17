// MainChain.java (classe de teste)
public class MainChain {
    public static void main(String[] args) {
        // Construindo a cadeia de responsabilidade
        VerificadorBase cadeia = new VerificaUsuario();
        cadeia.linkarProximo(new VerificaSenha())
                .linkarProximo(new VerificaPermissao());

        Middleware auth = cadeia;

        System.out.println("Tentando autenticar...");
        boolean sucesso = auth.processar("admin@empresa.com", "123456");

        if (sucesso) {
            System.out.println("✅ Acesso autorizado!");
        } else {
            System.out.println("❌ Acesso negado.");
        }
    }
}
