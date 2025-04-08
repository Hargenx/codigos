class MundoBase:
    def __init__(self):
        self.agentes = []
        self.recursos = {}
        self.tempo = 0
        self.coletor_dados = []

    def adicionar_agente(self, agente):
        self.agentes.append(agente)

    def atualizar(self):
        # Lógica para atualizar o estado global do mundo
        pass

    def coletar_dados(self):
        snapshot = {
            'tempo': self.tempo,
            'estado_mundo': self.recursos.copy(),
            'estado_agentes': [vars(agente) for agente in self.agentes]
        }
        self.coletor_dados.append(snapshot)

    def exportar_resultados(self, caminho='resultados.json'):
        import json
        with open(caminho, 'w') as f:
            json.dump(self.coletor_dados, f, indent=4)
