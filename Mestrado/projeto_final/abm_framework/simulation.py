from concurrent.futures import ThreadPoolExecutor, as_completed

def processar_agente(agente, ambiente):
    agente.decidir(ambiente)
    agente.agir(ambiente)
    return agente.id  # Para log, se desejar

class Simulacao:
    def __init__(self, mundo, ciclos=100, paralelo=True, max_workers=None):
        self.mundo = mundo
        self.ciclos = ciclos
        self.paralelo = paralelo
        self.max_workers = max_workers

    def executar_ciclo(self):
        if self.paralelo:
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = {executor.submit(processar_agente, agente, self.mundo): agente for agente in self.mundo.agentes}
                for future in as_completed(futures):
                    future.result()  # Você pode fazer logging aqui se quiser
        else:
            for agente in self.mundo.agentes:
                processar_agente(agente, self.mundo)

        self.mundo.atualizar()
        self.mundo.coletar_dados()

    def executar(self):
        for _ in range(self.ciclos):
            self.executar_ciclo()

        self.mundo.exportar_resultados()
