import json
import os

class DicionarioSinonimos:
    def __init__(self, arquivo="sinonimos.json"):
        self.arquivo = arquivo
        # Tenta carregar o dicionário a partir do arquivo JSON
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                try:
                    self.sinonimos = json.load(f)
                except json.JSONDecodeError:
                    self.sinonimos = {}
        else:
            self.sinonimos = {}

    def salvar(self):
        """Salva o dicionário atual em um arquivo JSON."""
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.sinonimos, f, ensure_ascii=False, indent=4)

    def adicionar_sinonimos(self, palavra: str, sinonimos: list) -> None:
        """
        Adiciona uma palavra e sua lista de sinônimos ao dicionário.
        Após a alteração, o dicionário é salvo no arquivo.
        """
        self.sinonimos[palavra] = sinonimos
        self.salvar()

    def buscar_sinonimos(self, palavra: str) -> list:
        """
        Retorna a lista de sinônimos da palavra ou
        'Palavra não encontrada' caso a chave não exista.
        """
        return self.sinonimos.get(palavra, "Palavra não encontrada")

    def remover_palavra(self, palavra: str) -> None:
        """
        Remove a palavra (e seus sinônimos) do dicionário,
        salvando a alteração no arquivo.
        """
        if palavra in self.sinonimos:
            del self.sinonimos[palavra]
            self.salvar()
            print(f"Palavra '{palavra}' e seus sinônimos foram removidos.")
        else:
            print(f"Palavra '{palavra}' não encontrada no dicionário.")

def principal():
    dicionario = DicionarioSinonimos()
    dicionario.adicionar_sinonimos("feliz", ["alegre", "contente"])
    dicionario.adicionar_sinonimos("triste", ["melancólico", "deprimido"])

    print("Sinônimos de 'feliz':", dicionario.buscar_sinonimos("feliz"))
    print("Sinônimos de 'chateado':", dicionario.buscar_sinonimos("chateado"))

    dicionario.remover_palavra("triste")

if __name__ == '__main__':
    principal()
