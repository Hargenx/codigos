package A02_ARA0101_PPJ_CG.padrao_grasp;

import A02_ARA0101_PPJ_CG.padrao_grasp.model.Produto;
import A02_ARA0101_PPJ_CG.padrao_grasp.repository.ClienteRepository;
import A02_ARA0101_PPJ_CG.padrao_grasp.service.PagamentoPix;
import A02_ARA0101_PPJ_CG.padrao_grasp.controller.PedidoController;
import A02_ARA0101_PPJ_CG.padrao_grasp.service.MetodoPagamento;

public class Main {
    public static void main(String[] args) {
        // Criar alguns produtos
        Produto p1 = new Produto("Notebook", 3500.00);
        Produto p2 = new Produto("Mouse", 150.00);

        // Repositório de cliente
        ClienteRepository repo = new ClienteRepository();

        // Escolher um método de pagamento
        MetodoPagamento pagamento = new PagamentoPix(); // ou new PagamentoCartao();

        // Criar controller
        PedidoController controller = new PedidoController(pagamento, repo);

        // Simular pedido
        controller.realizarPedido("001", p1, 1);
        controller.realizarPedido("002", p2, 2);
    }
}
