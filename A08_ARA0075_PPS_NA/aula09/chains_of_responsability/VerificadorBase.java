public abstract class VerificadorBase implements Middleware {
    private Middleware proximo;

    public VerificadorBase linkarProximo(VerificadorBase next) {
        this.proximo = next;
        return next;
    }

    protected boolean processarProximo(String email, String senha) {
        if (proximo == null)
            return true;
        return proximo.processar(email, senha);
    }
}
