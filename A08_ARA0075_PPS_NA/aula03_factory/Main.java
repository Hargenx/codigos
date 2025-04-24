package A08_ARA0075_PPS_NA.aula03_factory;

import java.util.ArrayList;
import java.util.List;

// Classe representando um produto
class Product {
    private String name;

    public Product(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return name;
    }
}

// Classe representando um item de pedido
class OrderItem {
    private int quantity;
    private double unitPrice;
    private Product product;

    public OrderItem(int quantity, double unitPrice, Product product) {
        this.quantity = quantity;
        this.unitPrice = unitPrice;
        this.product = product;
    }

    public int getQuantity() {
        return quantity;
    }

    public double getUnitPrice() {
        return unitPrice;
    }

    public Product getProduct() {
        return product;
    }

    @Override
    public String toString() {
        return "OrderItem [produto=" + product + ", quantidade=" + quantity + ", preço unitário=" + unitPrice + "]";
    }
}

// Classe abstrata que define o template para remoção de itens inválidos
abstract class OrderItemProcessor {
    // Método abstrato que será implementado pelas subclasses para definir a
    // validação
    protected abstract boolean isValid(OrderItem item);

    // Método template que utiliza o método isValid para filtrar a lista de itens
    public List<OrderItem> removeInvalidItems(List<OrderItem> items) {
        List<OrderItem> validItems = new ArrayList<>();
        for (OrderItem item : items) {
            if (isValid(item)) {
                validItems.add(item);
            }
        }
        return validItems;
    }
}

// Implementação concreta da validação: quantidade deve estar entre 1 e 100
class DefaultOrderItemProcessor extends OrderItemProcessor {
    @Override
    protected boolean isValid(OrderItem item) {
        return item.getQuantity() >= 1 && item.getQuantity() <= 100;
    }
}

// Fábrica que cria a instância do processador (Factory Method)
class OrderItemProcessorFactory {
    public static OrderItemProcessor createProcessor() {
        // Aqui é possível decidir qual implementação instanciar.
        return new DefaultOrderItemProcessor();
    }
}

// Classe principal que demonstra o uso
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
