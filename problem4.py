

def polyndromchecker():

    for i in range(999, 100, -1):

        for j in range(999, 100, -1):

            mul = i * j
            parta = str(int(mul / 1000))
            partb = str(mul % 1000)

            while(len(partb) < 3):
                partb = '0' + partb

            if parta == partb[::-1]:
                return i, j


if __name__ == '__main__':
    k = polyndromchecker()
    print(k)