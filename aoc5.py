arr_num = [[0]*1000 for i in range(1000)]
#print(arr_num)


def fillvertical(y1,y2,x):

    for i in range(y1, y2+1):
        # print(arr_num[i][x])
        arr_num[i][x] = arr_num[i][x] + 1

    # print(arr_num)


def fillhorizontal(x1,x2,y):

    for i in range(x1, x2+1):
        #print(arr_num[i][x])
        arr_num[y][i] = arr_num[y][i] + 1

    #print(arr_num)

def filldiag(x1,y1,x2,y2):
    # on aime se compliquer la vie
    if x1 < x2 and y1 < y2:
        # print(arr_num)
        # print(x1, y1, x2, y2)
        tempx = x1
        tempy = y1
        while tempx <= x2 and tempy <= y2:
            arr_num[tempy][tempx] = arr_num[tempy][tempx]+1
            tempy = tempy +1
            tempx = tempx + 1
            #print(arr_num)

    if x1 > x2 and y1 < y2:
        tempx = x2
        tempy = y2
        while tempx <= x1 and tempy >= y1:
            arr_num[tempy][tempx] = arr_num[tempy][tempx] + 1
            tempy = tempy - 1
            tempx = tempx + 1
            # print(arr_num)

    if x1 > x2 and y1 > y2:
        tempx = x2
        tempy = y2
        #print(tempx, tempy)
        while tempx <= x1 and tempy <= y1:
            arr_num[tempy][tempx] = arr_num[tempy][tempx] + 1
            tempy = tempy + 1
            tempx = tempx + 1
            # print(arr_num)

    if x1 < x2 and y1 > y2:
        tempx = x1
        tempy = y1
        #print(tempx, tempy)
        while tempx <= x2 and tempy >= y2:
            arr_num[tempy][tempx] = arr_num[tempy][tempx] + 1
            tempy = tempy - 1
            tempx = tempx + 1



def p1(coords):
    listfinal = []
    #onfait le tri
    for coord in coords:
        if coord[0] == coord[2] or coord[1] == coord[3]:
            listfinal.append(coord)
    #print(listfinal)

    for coord in listfinal:
        # vertical
        if coord[0] == coord[2]:
            if coord[1] > coord[3]:
                fillvertical(coord[3], coord[1],coord[0])
            else:
                fillvertical(coord[1], coord[3],coord[0])
        else:
            if coord[0] > coord[2]:
                fillhorizontal(coord[2],coord[0],coord[3]);
            else:
                fillhorizontal(coord[0],coord[2],coord[3]);
    sum = 0
    for line in arr_num:
        for elment in line:
            if elment > 1:
                sum = sum + 1
    print(sum)

def p2(coords):

    for coord in coords:
        # vertical

        if coord[0] == coord[2]:
            if coord[1] > coord[3]:
                fillvertical(coord[3], coord[1],coord[0])
            else:
                fillvertical(coord[1], coord[3],coord[0])
        #horizontal
        elif coord[3] == coord[1]:
            if coord[0] > coord[2]:
                fillhorizontal(coord[2],coord[0],coord[3]);
            else:
                fillhorizontal(coord[0],coord[2],coord[3]);
        #diag
        else:
            filldiag(coord[0],coord[1],coord[2],coord[3])

    #print(arr_num)
    sum = 0
    for line in arr_num:
        for elment in line:
            if elment > 1:
                sum = sum + 1
    print(sum)
    #print(arr_num)



if __name__ == '__main__':
    # fichier formaté en X,Y -> X,Y ==> X,Y,X,Y
    fichier = open("input/input5", "r")
    coords = []
    for line in fichier:
        coord = list(map(int, line.split(",")))
        coords.append(coord)
    #print(coords)
    p1(coords)
    arr_num = [[0] * 1000 for i in range(1000)]
    p2(coords)
