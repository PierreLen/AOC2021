
# coup de chance
def p1(crabes):
    sumint = 100000000000
    for crabe in crabes:
        sum = 0
        for crab in crabes:
            sum = abs(crabe - crab) + sum
        if sum < sumint:
            sumint = sum
            #print(sum)
    print("Résultat P1 :", sumint)

# Merci les maths de LE1
def p2(crabes):
    sumint = 100000000000
    for i in range(max(crabes)):
        sum = 0
        for crab in crabes:
            n = abs(i - crab)
            sum = (n*(n+1)/2) + sum
        if sum < sumint:
            sumint = sum
            #print(sum)
    print("Résultat P2 :", sumint)



if __name__ == '__main__':
    fichier = open("input/input7", "r")
    crabes = []
    for line in fichier:
        crabes = list(map(int,line.split(",")))

    #print(crabes)
    p1(crabes)
    p2(crabes)