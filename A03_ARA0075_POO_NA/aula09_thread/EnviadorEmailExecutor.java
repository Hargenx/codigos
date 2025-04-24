package A03_ARA0075_POO_NA.aula09_thread;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class EnviadorEmailExecutor implements Runnable {
    private String destinatario;

    public EnviadorEmailExecutor(String destinatario) {
        this.destinatario = destinatario;
    }

    @Override
    public void run() {
        System.out.println("Enviando e-mail para: " + destinatario);
        try {
            Thread.sleep(4000); // simula tempo de envio
        } catch (InterruptedException e) {
            System.out.println("Erro ao enviar para: " + destinatario);
        }
        System.out.println("E-mail enviado para: " + destinatario);
    }

    public static void main(String[] args) {
        String[] usuarios = { "raphael.jesus@estacio.br", "carol@email.com", "ana@email.com", "gilson@email.com" };

        // Cria um pool com 2 threads
        ExecutorService executor = Executors.newFixedThreadPool(2);

        for (String email : usuarios) {
            EnviadorEmailExecutor tarefa = new EnviadorEmailExecutor(email);
            executor.execute(tarefa); // Envia a tarefa para o pool
        }

        executor.shutdown(); // sinaliza que não vamos enviar mais tarefas
        System.out.println("Todos os envios foram agendados...");
    }
}
