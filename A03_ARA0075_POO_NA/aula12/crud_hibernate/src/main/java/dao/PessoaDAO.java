package dao;

import model.Pessoa;
import org.hibernate.Session;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

import java.util.List;

public class PessoaDAO {
    private Session getSession() {
        return new Configuration().configure().buildSessionFactory().openSession();
    }

    public void salvar(Pessoa pessoa) {
        Session session = getSession();
        Transaction tx = session.beginTransaction();
        session.save(pessoa);
        tx.commit();
        session.close();
    }

    public List<Pessoa> listar() {
        Session session = getSession();
        List<Pessoa> lista = session.createQuery("from Pessoa", Pessoa.class).list();
        session.close();
        return lista;
    }

    public void atualizar(Pessoa pessoa) {
        Session session = getSession();
        Transaction tx = session.beginTransaction();
        session.update(pessoa);
        tx.commit();
        session.close();
    }

    public void deletar(Pessoa pessoa) {
        Session session = getSession();
        Transaction tx = session.beginTransaction();
        session.delete(pessoa);
        tx.commit();
        session.close();
    }
}
