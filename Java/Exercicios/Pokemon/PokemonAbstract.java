public abstract class PokemonAbstract {
    private Integer numero;
    private String nome;
    private Integer ataque;
    private Integer defesa;
    private Integer saude;
    private Integer ataqueEspecial;
    private Integer defesaEspecial;
    private Integer velocidade;
    private String genero;

    public Integer getNumero() {
        return numero;
    }
    public void setNumero(Integer numero) {
        this.numero = numero;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public Integer getAtaque() {
        return ataque;
    }
    public void setAtaque(Integer ataque) {
        this.ataque = ataque;
    }

    public Integer getDefesa() {
        return defesa;
    }
    public void setDefesa(Integer defesa) {
        this.defesa = defesa;
    }

    public Integer getSaude() {
        return saude;
    }
    public void setSaude(Integer saude) {
        this.saude = saude;
    }

    public Integer getAtaqueEspecial() {
        return ataqueEspecial;
    }
    public void setAtaqueEspecial(Integer ataqueEspecial) {
        this.ataqueEspecial = ataqueEspecial;
    }

    public Integer getDefesaEspecial() {
        return defesaEspecial;
    }
    public void setDefesaEspecial(Integer defesaEspecial) {
        this.defesaEspecial = defesaEspecial;
    }

    public Integer getVelocidade() {
        return velocidade;
    }
    public void setVelocidade(Integer velocidade) {
        this.velocidade = velocidade;
    }

    public String getGenero() {
        return genero;
    }
    public void setGenero(String genero) {
        this.genero = genero;
    }

    public abstract void restaurarVida();
    public abstract void golpear();
    public abstract void defender();
}