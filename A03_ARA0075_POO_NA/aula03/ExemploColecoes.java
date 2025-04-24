package A03_ARA0075_POO_NA.aula03;

import java.util.*;

public class ExemploColecoes {
    public static void main(String[] args) {
        // Uso de List (ArrayList)
        List<String> lista = new ArrayList<>();
        lista.add("Maçã");
        lista.add("Banana");
        lista.add("Laranja");
        System.out.println("Lista: " + lista);

        // Iterando pela lista
        for (String fruta : lista) {
            System.out.println("Fruta: " + fruta);
        }

        // Uso de Set (HashSet)
        // Sets não permitem elementos duplicados e não garantem ordem.
        Set<String> conjunto = new HashSet<>();
        conjunto.add("Maçã");
        conjunto.add("Banana");
        conjunto.add("Maçã"); // Este "Maçã" duplicado não será adicionado.
        System.out.println("\nConjunto: " + conjunto);

        // Uso de Queue (LinkedList)
        // Queue trabalha com o conceito FIFO (First In, First Out).
        Queue<String> fila = new LinkedList<>();
        fila.offer("Primeiro");
        fila.offer("Segundo");
        fila.offer("Terceiro");
        System.out.println("\nFila inicial: " + fila);
        // Remove o elemento que está na cabeça da fila.
        String removidoFila = fila.poll();
        System.out.println("Elemento removido da fila: " + removidoFila);
        System.out.println("Fila após remoção: " + fila);

        // Uso de Deque (ArrayDeque)
        // Deque permite inserções e remoções dos dois extremos (início e fim).
        Deque<String> deque = new ArrayDeque<>();
        // Adiciona no final
        deque.offer("Fim");
        // Adiciona no início
        deque.push("Início");
        System.out.println("\nDeque inicial: " + deque);
        // Remove do início (comportamento de pilha)
        String removidoDeque = deque.pop();
        System.out.println("Elemento removido do início: " + removidoDeque);
        System.out.println("Deque após remoção: " + deque);
    }
}
