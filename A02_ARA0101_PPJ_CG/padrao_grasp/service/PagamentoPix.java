package A02_ARA0101_PPJ_CG.padrao_grasp.service;

public class PagamentoPix implements MetodoPagamento {
    public void pagar(double valor) {
        System.out.println("Pagando com Pix: " + valor);
    }
}
