package A08_ARA0075_PPS_NA.aula06.desafioSingProt;

public class Documento {
    private String titulo;
    private String conteudo;
    private String formato;

    public Documento(String titulo, String conteudo, String formato) {
        this.titulo = titulo;
        this.conteudo = conteudo;
        this.formato = formato;
    }

    // Getters e Setters
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getConteudo() {
        return conteudo;
    }

    public void setConteudo(String conteudo) {
        this.conteudo = conteudo;
    }

    public String getFormato() {
        return formato;
    }

    public void setFormato(String formato) {
        this.formato = formato;
    }

    // Método clone que retorna um novo Documento com os mesmos valores
    public Documento clone() {
        return new Documento(titulo, conteudo, formato);
    }

    @Override
    public String toString() {
        return "Documento [titulo=" + titulo + ", conteudo=" + conteudo + ", formato=" + formato + "]";
    }
}
