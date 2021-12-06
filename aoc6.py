import time

def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)


# Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp

# brute force
def p1(dates):
    nb = len(dates)
    for i in range(256):
        for i in range(nb):
            if dates[i] == 0:
                dates.append(8)
                dates[i] = 6
                nb =nb + 1
            else:
                dates[i] = dates[i] - 1
        #print(dates)
    print(len(dates))


# on reflechis un peu
def p2(dates):
    fish = [0] * 9
    # remplisage initial
    for date in dates:
        fish[date] += 1
    #print(fish)
    # passage des jours
    for i in range(256):
        leftRotate(fish, 1, 9)
        fish[6] = fish[6] + fish[8]
        #print(i)

    #calcul de la somme
    sum = 0
    for i in range(9):
        sum = sum + fish[i]
    print(sum)


if __name__ == '__main__':
    fichier = open("input/input6", "r")
    date = []
    for line in fichier:
        date = list(map(int,line.split(",")))

    #print(date)
    p2(date)
