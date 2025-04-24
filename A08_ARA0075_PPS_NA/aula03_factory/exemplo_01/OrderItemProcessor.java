package A08_ARA0075_PPS_NA.aula03_factory.exemplo_01;

import java.util.ArrayList;
import java.util.List;

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