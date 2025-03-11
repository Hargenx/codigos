import json
import os

def carregar_dicionario(nome_arquivo: str) -> dict:
    """
    Carrega o dicionário de sinônimos de um arquivo JSON.
    Retorna um dicionário vazio caso o arquivo não exista.
    """
    if not os.path.exists(nome_arquivo):
        return {}
    
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            # Se o arquivo estiver corrompido ou vazio
            return {}

def salvar_dicionario(dicionario: dict, nome_arquivo: str) -> None:
    """
    Salva o dicionário de sinônimos em formato JSON.
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dicionario, arquivo, ensure_ascii=False, indent=4)

def adicionar_palavra(palavra: str, sinonimos: list, dicionario: dict) -> None:
    """
    Adiciona uma palavra e sua lista de sinônimos ao dicionário.
    Caso a palavra já exista, os novos sinônimos são adicionados
    sem duplicar os existentes.
    """
    palavra = palavra.lower()  # Normaliza para letras minúsculas
    # Garante que todos os sinônimos também fiquem em minúsculas
    sinonimos_normalizados = [sin.lower() for sin in sinonimos]
    
    if palavra not in dicionario:
        dicionario[palavra] = []
    
    for sin in sinonimos_normalizados:
        if sin not in dicionario[palavra]:
            dicionario[palavra].append(sin)

def buscar_sinonimos(palavra: str, dicionario: dict) -> list:
    """
    Retorna a lista de sinônimos de uma palavra.
    Caso a palavra não exista, retorna None.
    """
    palavra = palavra.lower()
    return dicionario.get(palavra, None)

def remover_palavra(palavra: str, dicionario: dict) -> bool:
    """
    Remove a palavra do dicionário, se existir.
    Retorna True se a palavra foi removida, False caso contrário.
    """
    palavra = palavra.lower()
    if palavra in dicionario:
        del dicionario[palavra]
        return True
    return False

def main():
    nome_arquivo = "sinonimos.json"
    
    # Carrega o dicionário a partir do arquivo
    dicionario_sinonimos = carregar_dicionario(nome_arquivo)
    
    # 1. Adicionar palavras e sinônimos
    adicionar_palavra("Feliz", ["Contente", "Alegre", "Satisfeito"], dicionario_sinonimos)
    adicionar_palavra("Triste", ["Melancólico", "Abatido"], dicionario_sinonimos)
    adicionar_palavra("Rápido", ["Veloz", "Ágil"], dicionario_sinonimos)
    
    # 2. Buscar sinônimos
    palavra_busca = "Feliz"
    sin = buscar_sinonimos(palavra_busca, dicionario_sinonimos)
    if sin:
        print(f"Sinônimos de '{palavra_busca}': {sin}")
    else:
        print(f"A palavra '{palavra_busca}' não está no dicionário.")
    
    # 3. Remover palavra
    palavra_remover = "Triste"
    if remover_palavra(palavra_remover, dicionario_sinonimos):
        print(f"A palavra '{palavra_remover}' foi removida com sucesso.")
    else:
        print(f"A palavra '{palavra_remover}' não foi encontrada.")
    
    # 4. Salvar alterações no arquivo
    salvar_dicionario(dicionario_sinonimos, nome_arquivo)
    print("Dicionário salvo com sucesso no arquivo 'sinonimos.json'.")

if __name__ == "__main__":
    main()
