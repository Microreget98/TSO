import json
import os


class A:
    def extractor(path):
        dataexp = open(path)
        data = json.load(dataexp)
        return data

    def acomododatos(data):
        for i in data:
            for j in data[0][j]:
                for a in data[j][0][a]:
                    if i == 0:
                        Equipo = str(data[i][j])
                    if i == 1:
                        Torneo = str(data[i][j])
                    # if i==4:
        return True


res = A.extractor("C:/Users/angel/Desktop/TSO/Proyecto/ligamx.json")
A.acomododatos
