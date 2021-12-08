
def p1(segments):
    sum = 0
    for data in segments:
        for i in range(4):
            long = len(data[i + 11])
            if long in [2, 3, 4, 7]:
                sum = sum + 1
    print(sum)

def p2(segments):
    sum = 0
    for ligne in segments:
        segment = ['', '', '', '', '', '', '']
        # recherche 1
        for info in ligne:
            if len(info) == 2:
                segment[1] = segment[1] + info
                segment[2] = segment[2] + info
                break
        # recherche 7
        for info in ligne:
            if len(info) == 3:
                for element in info:
                    if not element in segment[1] and segment[2]:
                        segment[0] = element
                break
        # recherche 4

        for info in ligne:
            if len(info) == 4:
                for element in info:
                    if not element in segment[1] and not element in segment[2]:
                        segment[5] = element + segment[5]
                        segment[6] = element + segment[6]
                break
        #recherche 8
        for info in ligne:
            if len(info) == 7:
                for element in info:
                    if not element in segment[1] and not element in segment[2] and not element in segment[5] and not element in segment[0]:
                        segment[4] = element + segment[4]
                        segment[3] = element + segment[3]
                break
        # recherche 6 0 9
        for info in ligne:
            if len(info) == 6:
                # c'est un 6
                for element in segment[1]:
                    if element not in info:
                        segment[2] = segment[2].replace(element, '')
                        segment[1] = segment[1].replace(segment[2], '')
                        #print(element)
                        break
                # 0
                for element in segment[6]:
                    if not element in info:
                        segment[5] = segment[5].replace(element, '')
                        segment[6] = segment[6].replace(segment[5], '')
                        break
                # 9
                for element in segment[4]:
                    if not element in info:
                        segment[3] = segment[3].replace(element, '')
                        segment[4] = segment[4].replace(segment[3], '')
                        break

        value = 0
        for i in range(4):
            wire = ligne[i+11]
            #print(wire)
            long = len(wire)
            if long in [2, 3, 4, 7]:
                if long == 2:
                    temp = 1
                if long == 3:
                    temp = 7
                if long == 4:
                    temp = 4
                if long == 7:
                    temp = 8
            else:
                if long == 5:
                    if not segment[1] in wire and not segment[4] in wire:
                        temp = 5
                    elif not segment[2] in wire and not segment[5] in wire:
                        temp = 2
                    else:
                        temp = 3
                else:
                    if not segment[6] in wire:
                        temp = 0
                    else:
                        if not segment[4] in wire:
                            temp = 9
                        else:
                            temp = 6

            #print(temp *  pow(10, 3-i))
            value = temp * pow(10, 3-i) + value

        #print(segment)
        #print(value)
        sum = sum + value
    print(sum)

if __name__ == '__main__':
    fichier = open("input/input8", "r")
    segments = []
    for line in fichier:
        data = line.split()
        segments.append(data)
    #print(segments)
    p2(segments)