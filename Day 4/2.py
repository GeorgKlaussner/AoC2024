import numpy as np
shape = None
matrix = np.array([])
sum = 0

def xmas1(coord):
    y, x = coord
    global sum
    if y >= 1 and x >= 1 and x <= shape[0]-2 and y <= shape[1]-2:
        print(matrix[x-1][y-1], matrix[x-1][y+1], matrix[x+1][y-1], matrix[x+1][y+1])
        if matrix[x-1][y-1] == b'M' and matrix[x-1][y+1] == b'M' and matrix[x+1][y-1] == b'S' and matrix[x+1][y+1] == b'S':
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
        xmas1(coord)
        xmas2(coord)
        xmas3(coord)
        xmas4(coord)
    print(sum)

if __name__ == "__main__":
    main()