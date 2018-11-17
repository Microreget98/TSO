A1 = [[1, 2], [4, 4]]
A2 = [[1, 2], [4, 4]]
AR = []
O = []
R = 0

fila = 0
f = 0
n = A1.__len__()
for i in range(n):
    for j in range(n):
        O.append(A1[i][j]/17)
print(str(O) + "Esto es <<o>>")



class asingdata():
    def Objequipo(Equipo, Torneo, Matriz):
        equipo = Equipo
        torneo = Torneo
        matriz = Matriz

        return matriz, equipo, torneo

    def Getdatos(matriz):
        matriz1 = matriz
        fila = 0
        f = 0
        n = A1.__len__()
        for z in range(n):
            AR.append([])
            for i in range(n):
                for j in range(n):
                    R += ((matriz[fila][j]) / 17 * (matriz[j][i]) / 17)
                AR[f].append(R)
                R = 0
            fila += 1
            f += 1

        print(AR)
        print(matriz)

    def Acmodo(self, equipo, torneo):
        pass