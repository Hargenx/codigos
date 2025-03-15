def exemplo01(pos: int) -> None:
    texto = "Eu estou criando coisas legais."
    print(texto[:pos])

def outro_exemplo(param: str) -> None:
    texto = 'Eu sou apenas um texto bobo feito para exemplo de aula.'
    print(param in texto)

def mais_exemplo(texto: str, sai: str, sub: str) -> None:
    novo_texto = texto.replace(sai, sub)
    print(novo_texto)

if __name__ == "__main__":
    exemplo01(4)
    outro_exemplo("au")
    mais_exemplo('Texto onde teremos uma substituição.', 'onde', 'no qual')