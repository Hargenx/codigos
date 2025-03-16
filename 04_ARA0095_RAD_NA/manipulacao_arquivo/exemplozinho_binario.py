with open("dor.jpg", "rb") as file:
    conteudo = file.read(100)  # lê 100 bytes
    print(conteudo)