import re
def validar_email(email):
    # Padrão para validar endereços de e-mail
    padrao = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.match(padrao, email):
        return True
    else:
        return False
# Testando a função com alguns exemplos
exemplos_emails = ["usuario@email.com", "ou-tro@email.co.uk", "invalido@.com", "sem_arroba.com"]
for email in exemplos_emails:
    if validar_email(email):
        print(f"{email} é um endereço de e-mail válido.")
    else:
        print(f"{email} não é um endereço de e-mail válido.")