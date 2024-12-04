import numpy as np
shape = None
matrix = np.array([])
sum = 0

def northWest(coord):
    y, x = coord
    global sum
    if matrix[x-1][y-1] == b'M' and y >= 1 and x >= 1:
        southWest(coord)

def northEast(coord):
    y, x = coord
    global sum
    try:
        if matrix[x+1][y-1] == b'S' and y >= 1 and x <= shape[0] -2:
            print(f"ne {coord}")
            northWest(coord)
    except Exception as e:
        pass

def southEast(coord):
    y, x = coord
    global sum
    try:
        if matrix[x+1][y+1] == b'S' and y <= shape[1] -2 and x <= shape[0] -2:
            northEast(coord)
    except Exception as e:
        pass

def southWest(coord):
    y, x = coord
    global sum
    try:
        if matrix[x-1][y+1] == b'M' and y <= shape[1] -2 and x >= 1:
            print(f"sw {coord}")
            sum += 1
    except Exception as e:
        pass


def main():
    global shape
    global matrix
    matrix = np.genfromtxt("input.txt", delimiter=1, dtype=np.character)
    shape = matrix.shape
    a = np.where(matrix == b'A')
    listA = tuple(zip(*a))
    print(listA)
    for coord in listA:
        southEast(coord)
    print(sum)

if __name__ == "__main__":
    main()
    print(shape)