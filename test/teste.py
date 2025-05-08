class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        x_diff_sq = (self.x - p2.x) ** 2
        y_diff_sq = (self.y - p2.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

co = Coordenadas(1, 2)
print(co)
distancia = co.distance(Coordenadas(4, 6))
print("Distancia: ", distancia)
print(co)