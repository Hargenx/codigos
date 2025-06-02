package A03_ARA0075_POO_NA.av.questão2;

public class MinhaThread extends Thread {
    public void run() {
        System.out.println("Executando a thread: " + Thread.currentThread().getName());
    }

    public static void main(String[] args) {
        MinhaThread t1 = new MinhaThread();
        MinhaThread t2 = new MinhaThread();

        t1.start();
        t2.start();
    }
}
