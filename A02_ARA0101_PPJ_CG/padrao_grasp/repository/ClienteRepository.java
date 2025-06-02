package A02_ARA0101_PPJ_CG.padrao_grasp.repository;

import A02_ARA0101_PPJ_CG.padrao_grasp.model.Cliente;

// Invenção Pura
public class ClienteRepository {
    public Cliente buscarPorId(String id) {
        return new Cliente(id); // simulação de banco
    }
}
