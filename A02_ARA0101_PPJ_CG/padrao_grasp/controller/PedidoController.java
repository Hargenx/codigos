package A02_ARA0101_PPJ_CG.padrao_grasp.controller;

import A02_ARA0101_PPJ_CG.padrao_grasp.model.*;
import A02_ARA0101_PPJ_CG.padrao_grasp.repository.ClienteRepository;
import A02_ARA0101_PPJ_CG.padrao_grasp.service.MetodoPagamento;

public class PedidoController {
    private MetodoPagamento metodo;
    private ClienteRepository clienteRepo;

    public PedidoController(MetodoPagamento metodo, ClienteRepository repo) {
        this.metodo = metodo;
        this.clienteRepo = repo;
    }

    public void realizarPedido(String clienteId, Produto produto, int qtde) {
        Cliente cliente = clienteRepo.buscarPorId(clienteId);
        Pedido pedido = new Pedido();
        pedido.adicionarItem(produto, qtde);
        double total = pedido.calcularTotal();
        System.out.println("Cliente: " + cliente.getNome());
        metodo.pagar(total);
    }
}
