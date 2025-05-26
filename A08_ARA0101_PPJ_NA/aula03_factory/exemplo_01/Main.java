package A08_ARA0075_PPS_NA.aula03_factory.exemplo_01;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<OrderItem> items = new ArrayList<>();
        items.add(new OrderItem(0, 10.0, new Product("Produto A"))); // inválido (quantidade = 0)
        items.add(new OrderItem(50, 20.0, new Product("Produto B"))); // válido
        items.add(new OrderItem(101, 30.0, new Product("Produto C"))); // inválido (quantidade = 101)
        items.add(new OrderItem(100, 40.0, new Product("Produto D"))); // válido (quantidade = 100)

        // Utilizando o Factory Method para obter o processador
        OrderItemProcessor processor = OrderItemProcessorFactory.createProcessor();
        List<OrderItem> validItems = processor.removeInvalidItems(items);

        System.out.println("Itens válidos:");
        for (OrderItem item : validItems) {
            System.out.println(item);
        }
    }
}