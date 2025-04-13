class Marca:
    def __init__(self, id: int, nome: str, sigla: str) -> None:
        self.id = id
        self.nome = nome
        self.sigla = sigla

    def __str__(self) -> str:
        return f"{self.nome} ({self.sigla})"
