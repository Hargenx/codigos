package A08_ARA0075_PPS_NA.aula07.bridge;

public class Email implements CanalEnvio {
    public void enviar(String texto) {
        System.out.println("Email: " + texto);
    }
}