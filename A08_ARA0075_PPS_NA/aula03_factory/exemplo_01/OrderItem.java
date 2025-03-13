package exemplo_01;

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