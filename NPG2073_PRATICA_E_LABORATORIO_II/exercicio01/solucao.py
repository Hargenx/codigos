from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Solicita ao usuário a entrada de um texto
texto_input = input("Digite o texto para gerar a nuvem de palavras: ")

# Divide o texto em palavras e filtra aquelas com 4 ou mais caracteres
palavras = texto_input.split()
palavras_filtradas = [palavra for palavra in palavras if len(palavra) >= 4]

# Junta as palavras filtradas para formar o texto final
texto_filtrado = " ".join(palavras_filtradas)

# Conta o número total de palavras consideradas na nuvem
num_palavras = len(palavras_filtradas)

# Gera a nuvem de palavras utilizando o texto filtrado
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_filtrado)

# Configura a figura e exibe a nuvem com um título customizado
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title(f"Nuvem de Palavras - {num_palavras} palavras consideradas")

# Salva a imagem gerada em um arquivo
plt.savefig("nuvem_customizada.png")
plt.show()
