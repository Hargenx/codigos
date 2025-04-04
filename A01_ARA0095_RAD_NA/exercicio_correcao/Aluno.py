from typing import List, Dict
class Aluno:
    """
    Representa um aluno com nome e nota.

    Attributes:
        nome (str): Nome do aluno.
        nota (float): Nota do aluno.
    """

    def __init__(self, nome: str, nota: float):
        """
        Inicializa uma nova instância de Aluno.

        Args:
            nome (str): O nome do aluno.
            nota (float): A nota do aluno.
        """
        self.nome = nome.strip().title()
        self.nota = float(nota)

    def to_dict(self) -> Dict[str, float]:
        """
        Retorna o aluno como um dicionário com nome e nota.

        Returns:
            dict: Um dicionário {nome: nota}.
        """
        return {self.nome: self.nota}

    def __str__(self) -> str:
        """
        Representação em string do aluno no formato CSV.

        Returns:
            str: Nome e nota separados por vírgula.
        """
        return f"{self.nome},{self.nota:.1f}"