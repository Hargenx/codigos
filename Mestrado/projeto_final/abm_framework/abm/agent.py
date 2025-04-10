class AgenteBase:
    def __init__(self, id_agente: int) -> None:
        self.id = id_agente
        self.recursos = {}  # Recursos gerais, como saldo, energia, etc.
    
    def decidir(self, ambiente: 'AgenteBase') -> None:
        raise NotImplementedError("Implementar decisão do agente na subclasse.")
    
    def agir(self, ambiente: 'AgenteBase') -> None:
        raise NotImplementedError("Implementar ação do agente na subclasse.")
