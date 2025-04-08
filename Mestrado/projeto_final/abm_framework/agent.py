class AgenteBase:
    def __init__(self, id_agente):
        self.id = id_agente
        self.recursos = {}  # Recursos gerais, como saldo, energia, etc.
    
    def decidir(self, ambiente):
        raise NotImplementedError("Implementar decisão do agente na subclasse.")
    
    def agir(self, ambiente):
        raise NotImplementedError("Implementar ação do agente na subclasse.")
