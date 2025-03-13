package exemplo_01;

// Fábrica que cria a instância do processador (Factory Method)
class OrderItemProcessorFactory {
    public static OrderItemProcessor createProcessor() {
        // Aqui é possível decidir qual implementação instanciar.
        return new DefaultOrderItemProcessor();
    }
}