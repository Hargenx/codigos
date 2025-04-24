package A03_ARA0075_POO_NA.aula09_thread;

public class EnviadorEmail extends Thread {
    private String destinatario;

    public EnviadorEmail(String destinatario) {
        this.destinatario = destinatario;
    }

    @Override
    public void run() {
        System.out.println("Enviando e-mail para: " + destinatario);
        try {
            // Simula tempo de envio
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            System.out.println("Erro ao enviar para: " + destinatario);
        }
        System.out.println("E-mail enviado para: " + destinatario);
    }

    public static void main(String[] args) {
        String[] usuarios = { "raphael.jesus@estacio.br", "Carol@email.com", "ana@email.com" };

        for (String email : usuarios) {
            EnviadorEmail thread = new EnviadorEmail(email);
            thread.start(); // inicia a thread para envio paralelo
        }

        System.out.println("Todos os envios foram iniciados...");
    }
}
