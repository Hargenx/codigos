import dao.PessoaDAO;
import model.Pessoa;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        PessoaDAO dao = new PessoaDAO();

        // Criar
        Pessoa novaPessoa = new Pessoa("Raphael", 40);
        dao.salvar(novaPessoa);

        // Listar
        List<Pessoa> pessoas = dao.listar();
        for (Pessoa p : pessoas) {
            System.out.println(p.getId() + ": " + p.getNome() + " - " + p.getIdade());
        }

        // Atualizar
        novaPessoa.setNome("Raphael Jesus");
        dao.atualizar(novaPessoa);

        // Deletar
        //dao.deletar(novaPessoa);
    }
}
