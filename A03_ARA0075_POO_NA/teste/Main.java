package teste;
public class Main {
    public static void main(String[] args) {
        A a = new B();
        a.imprimir();
        ((B) a).adicional();
    }
}

class A {
    void imprimir() {
        System.out.println("A");
    }
}

class B extends A {
    @Override
    void imprimir() {
        System.out.println("B");
    }

    void adicional() {
        System.out.println("Extra");
    }
}
