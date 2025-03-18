texto = "Nossa aula manipulando String."

novo_txt = texto.replace("manipulando", "trabalhando com")
print(novo_txt)

print(texto.lower())
print(texto.upper())
print(texto.capitalize())
print(texto.title())
print(texto.swapcase())

print(texto.count("a"))
print(texto.count("a", 0, 10))

print(texto.find("aula"))


print(texto.index("aula"))
#print(texto.index("aula", 10, 15))

print(texto.startswith("Nossa"))
print(texto.startswith("aula"))

print(texto.endswith("aula"))
print(texto.endswith("."))