import numpy as np
shape = None
matrix = np.array([])
sum = 0

def xmas(coord):
    x, y = coord
    global sum
    if y >= 1 and x >= 1 and x <= shape[0]-2 and y <= shape[1]-2:
        pos = [matrix[x-1][y-1],matrix[x-1][y+1], matrix[x+1][y-1], matrix[x+1][y+1]]
        print(pos)
        if pos.count(b'M') == 2 and pos.count(b'S') == 2:
            sum += 1

def main():
    global shape
    global matrix
    matrix = np.genfromtxt("input.txt", delimiter=1, dtype=np.character)
    shape = matrix.shape
    a = np.where(matrix == b'A')
    listA = tuple(zip(*a))
    print(listA)
    for coord in listA:
        xmas(coord)
    print(sum)

if __name__ == "__main__":
    main()