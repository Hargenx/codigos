from agent import AgenteBase
from world import MundoBase
import random

class AgenteFinanceiro(AgenteBase):
    def __init__(self, id_agente, saldo_inicial):
        super().__init__(id_agente)
        self.recursos['saldo'] = saldo_inicial
        self.recursos['ativos'] = {}

    def decidir(self, ambiente):
        self.decisao = random.choice(["comprar", "vender", "nada"])

    def agir(self, ambiente):
        # Exemplo simplificado
        if self.decisao == "comprar":
            ambiente.recursos['compras'] = ambiente.recursos.get('compras', 0) + 1
        elif self.decisao == "vender":
            ambiente.recursos['vendas'] = ambiente.recursos.get('vendas', 0) + 1

class MundoMercado(MundoBase):
    def atualizar(self):
        # Atualiza estado geral
        total_compras = self.recursos.get('compras', 0)
        total_vendas = self.recursos.get('vendas', 0)
        print(f"Ciclo {self.tempo}: Compras: {total_compras}, Vendas: {total_vendas}")
        self.recursos['compras'] = 0
        self.recursos['vendas'] = 0
