def recorrido():
    arr = [[1,1,1,1],[0,0,1,1],[1,0,1,0]]
    ben = [25,16,36]
    peso = [5,4,6]
    sumpes = 0
    sumben = 0
    n = 3
    j = 0
    b = 0
    for i in range(3):
        for j in range(1):
            sumben = arr[i][j] * ben[b] + sumben
            sumpes = arr[i][j] * peso[b] + sumpes
                
    print(str(sumben) + " esto es suma del beneficio")
    print(str(sumpes) + " esto es suma del peso")
                

recorrido()
#(arr[i+1][j] * pesben[i][b]) + (arr[i+2][j] * pesben[i][b])