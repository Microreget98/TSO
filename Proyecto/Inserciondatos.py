import json

dataexp = open("ligamx.json")
data = json.load(dataexp)
print(str(data) +" estos es data")
for i in data:
    Equipo = data[i]
    print(i)
    print(str(Equipo[0])+" equipos")
    for j in Equipo[0]:
        Torneo = Equipo[0][j]
        print(j)
        print(str(Torneo)+" torneos")
        for a in Torneo[0]:
            Resultados = Torneo[0][a]
            print(a)
            print(str(Resultados) + " resultados")

#
#asdfg = data["America"][0]["Apertura 2011"]
#print(asdfg[0])