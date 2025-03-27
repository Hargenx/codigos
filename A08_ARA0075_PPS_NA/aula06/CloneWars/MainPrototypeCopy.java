package CloneWars;

public class MainPrototypeCopy {
    public static void main(String[] args) {
        // Cria uma pessoa original com um endereço.
        Endereco endereco = new Endereco("Rua A");
        Pessoa original = new Pessoa("Raphael", endereco);

        // Cria clones usando shallow copy e deep copy.
        Pessoa cloneShallow = original.cloneShallow();
        Pessoa cloneDeep = original.cloneDeep();

        System.out.println("Antes de modificar:");

        System.out.println("Original: " + original);
        System.out.println("Clone Shallow: " + cloneShallow);
        System.out.println("Clone Deep: " + cloneDeep);

        // Modifica o endereço do clone shallow.
        cloneShallow.getEndereco().setRua("Rua B");
        // Modifica o nome do clone deep para diferenciar.
        cloneDeep.setNome("Caroline");

        System.out.println("\nDepois de modificar o cloneShallow:");
        System.out.println("Original: " + original);
        System.out.println("Clone Shallow: " + cloneShallow);
        System.out.println("Clone Deep: " + cloneDeep);
    }
}
