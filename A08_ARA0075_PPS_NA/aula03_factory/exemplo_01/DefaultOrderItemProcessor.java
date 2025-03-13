package exemplo_01;

// Implementação concreta da validação: quantidade deve estar entre 1 e 100
class DefaultOrderItemProcessor extends OrderItemProcessor {
    @Override
    protected boolean isValid(OrderItem item) {
        return item.getQuantity() >= 1 && item.getQuantity() <= 100;
    }
}