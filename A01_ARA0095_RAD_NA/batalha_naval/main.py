import tkinter as tk
import random

class BatalhaNavalSimulador:
    def __init__(self):
        self.tamanho_tabuleiro = 10
        self.tamanho_celula = 40
        self.mostrar = False  # Começa no modo de jogo
        self.jogadas = set()
        self.municoes = 20
        self.acertos = 0
        self.erros = 0
        self.pontuacao = 0

        # Navios: (nome, tamanho, sigla, cor, pontos)
        self.navios = [
            ("Porta-Aviões", 5, "PA", "darkblue", 50),
            ("Encouraçado", 4, "EN", "darkgreen", 40),
            ("Submarino", 3, "SB", "darkred", 30),
            ("Cruzador", 3, "CR", "purple", 25),
            ("Destroyer", 2, "DS", "darkorange", 20)
        ]

        self.janela = tk.Tk()
        self.janela.title("Batalha Naval")

        largura = self.tamanho_tabuleiro * self.tamanho_celula + 40
        altura = self.tamanho_tabuleiro * self.tamanho_celula + 40

        self.canvas = tk.Canvas(self.janela, width=largura, height=altura)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.atacar)

        self.botao_sortear = tk.Button(self.janela, text="Nova Rodada", command=self.sortear_novamente)
        self.botao_sortear.pack(side=tk.LEFT, padx=10, pady=5)

        self.botao_toggle = tk.Button(self.janela, text="Mostrar Navios", command=self.toggle_navios)
        self.botao_toggle.pack(side=tk.LEFT, padx=10, pady=5)

        self.status = tk.Label(self.janela, text="")
        self.status.pack(pady=5)

        self.sortear_novamente()
        self.janela.mainloop()

    def sortear_novamente(self):
        self.jogadas.clear()
        self.municoes = 20
        self.acertos = 0
        self.erros = 0
        self.pontuacao = 0
        self.posicoes_ocupadas = []
        self.navios_posicionados = []
        self.canvas.delete("all")
        self.desenhar_tabuleiro()
        self.gerar_posicoes_navios()
        self.atualizar_status("Novo jogo iniciado.")

    def toggle_navios(self):
        self.mostrar = not self.mostrar
        self.botao_toggle.config(text="Esconder Navios" if self.mostrar else "Mostrar Navios")
        self.sortear_novamente()

    def desenhar_tabuleiro(self):
        for i in range(self.tamanho_tabuleiro):
            letra = chr(65 + i)
            numero = str(i + 1)
            self.canvas.create_text(40 + i * self.tamanho_celula + self.tamanho_celula // 2, 20, text=letra, font=("Arial", 10, "bold"))
            self.canvas.create_text(20, 40 + i * self.tamanho_celula + self.tamanho_celula // 2, text=numero, font=("Arial", 10, "bold"))

        for i in range(self.tamanho_tabuleiro):
            for j in range(self.tamanho_tabuleiro):
                x0 = 40 + i * self.tamanho_celula
                y0 = 40 + j * self.tamanho_celula
                x1 = x0 + self.tamanho_celula
                y1 = y0 + self.tamanho_celula
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue", outline="black")

    def gerar_posicoes_navios(self):
        for nome, tamanho, sigla, cor, pontos in self.navios:
            colocado = False
            while not colocado:
                orientacao = random.choice(["H", "V"])
                if orientacao == "H":
                    x = random.randint(0, self.tamanho_tabuleiro - tamanho)
                    y = random.randint(0, self.tamanho_tabuleiro - 1)
                    posicoes = [(x + i, y) for i in range(tamanho)]
                else:
                    x = random.randint(0, self.tamanho_tabuleiro - 1)
                    y = random.randint(0, self.tamanho_tabuleiro - tamanho)
                    posicoes = [(x, y + i) for i in range(tamanho)]

                if not any(p in self.posicoes_ocupadas for p in posicoes):
                    self.posicoes_ocupadas.extend(posicoes)
                    self.navios_posicionados.append({
                        "nome": nome,
                        "sigla": sigla,
                        "cor": cor,
                        "pontos": pontos,
                        "posicoes": posicoes,
                        "acertos": set()
                    })
                    if self.mostrar:
                        for (x_cell, y_cell) in posicoes:
                            self.pintar_celula(x_cell, y_cell, cor)
                            self.escrever_sigla(x_cell, y_cell, sigla)
                    colocado = True

    def pintar_celula(self, x, y, cor):
        x0 = 40 + x * self.tamanho_celula
        y0 = 40 + y * self.tamanho_celula
        x1 = x0 + self.tamanho_celula
        y1 = y0 + self.tamanho_celula
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=cor, outline="black")

    def escrever_sigla(self, x, y, sigla):
        x_centro = 40 + x * self.tamanho_celula + self.tamanho_celula // 2
        y_centro = 40 + y * self.tamanho_celula + self.tamanho_celula // 2
        self.canvas.create_text(x_centro, y_centro, text=sigla, fill="white", font=("Arial", 10, "bold"))

    def atacar(self, evento):
        if self.municoes == 0:
            self.atualizar_status("⚠️ Fim de jogo! Sem munições.")
            return

        x = (evento.x - 40) // self.tamanho_celula
        y = (evento.y - 40) // self.tamanho_celula

        if 0 <= x < self.tamanho_tabuleiro and 0 <= y < self.tamanho_tabuleiro:
            if (x, y) in self.jogadas:
                self.atualizar_status("Você já atacou essa posição.")
                return

            self.jogadas.add((x, y))
            self.municoes -= 1
            acertou = False
            for navio in self.navios_posicionados:
                if (x, y) in navio["posicoes"]:
                    navio["acertos"].add((x, y))
                    self.pintar_celula(x, y, navio["cor"])
                    self.escrever_sigla(x, y, navio["sigla"])
                    self.acertos += 1
                    acertou = True

                    if set(navio["posicoes"]) == navio["acertos"]:
                        self.pontuacao += navio["pontos"]
                        self.atualizar_status(f"💥 Você afundou o {navio['nome']}! +{navio['pontos']} pts")
                    else:
                        self.atualizar_status(f"💥 Acertou o {navio['sigla']}!")

                    break

            if not acertou:
                self.pintar_celula(x, y, "white")
                self.erros += 1
                self.atualizar_status("💧 Água...")

            if self.municoes == 0 or self.todos_navios_afundados():
                fim = "🏆 Você venceu!" if self.todos_navios_afundados() else "💣 Suas munições acabaram."
                self.atualizar_status(f"{fim} Pontuação final: {self.pontuacao}")

    def todos_navios_afundados(self):
        for navio in self.navios_posicionados:
            if set(navio["posicoes"]) != navio["acertos"]:
                return False
        return True

    def atualizar_status(self, mensagem=""):
        self.status.config(
            text=f"{mensagem} | Acertos: {self.acertos} | Erros: {self.erros} | Munições: {self.municoes} | Pontos: {self.pontuacao}"
        )



if __name__ == "__main__":
    BatalhaNavalSimulador()