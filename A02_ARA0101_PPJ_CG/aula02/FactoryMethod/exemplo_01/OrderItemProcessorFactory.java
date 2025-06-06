package A02_ARA0101_PPJ_CG.aula02.FactoryMethod.exemplo_01;

// Fábrica que cria a instância do processador (Factory Method)
class OrderItemProcessorFactory {
    public static OrderItemProcessor createProcessor() {
        // Aqui é possível decidir qual implementação instanciar.
        return new DefaultOrderItemProcessor();
    }
}