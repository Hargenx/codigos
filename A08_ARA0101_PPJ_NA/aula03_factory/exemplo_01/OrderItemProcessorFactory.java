package A08_ARA0075_PPS_NA.aula03_factory.exemplo_01;

// Fábrica que cria a instância do processador (Factory Method)
class OrderItemProcessorFactory {
    public static OrderItemProcessor createProcessor() {
        // Aqui é possível decidir qual implementação instanciar.
        return new DefaultOrderItemProcessor();
    }
}