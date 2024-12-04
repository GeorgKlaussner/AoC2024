import numpy as np
shape = None
matrix = np.array([])
sum = 0

def west(coord):
    x, y = coord
    global sum
    try:
        if matrix[x-1][y] == b'M' and matrix[x-2][y] == b'A' and matrix[x-3][y] == b'S' and x >= 3:
            sum += 1
            print(f"w {coord}")
    except Exception as e:
        pass


def east(coord):
    x, y = coord
    global sum
    try:
        if matrix[x+1][y] == b'M' and matrix[x+2][y] == b'A' and matrix[x+3][y] == b'S' and x <= shape[0] -4:
            sum += 1
            print(f"e {coord}")
    except Exception as e:
        pass

def south(coord):
    x, y = coord
    global sum
    try:
        if matrix[x][y+1] == b'M' and matrix[x][y+2] == b'A' and matrix[x][y+3] == b'S' and y <= shape[1] -4:
            sum += 1
            print(f"s {coord}")
    except Exception as e:
        pass

def north(coord):
    x, y = coord
    global sum
    if matrix[x][y-1] == b'M' and matrix[x][y-2] == b'A' and matrix[x][y-3] == b'S' and y >= 3:
        sum += 1
        print(f"n {coord}")

def northWest(coord):
    x, y = coord
    global sum
    if matrix[x-1][y-1] == b'M' and matrix[x-2][y-2] == b'A' and matrix[x-3][y-3] == b'S' and y >= 3 and x >= 3:
        sum += 1
        print(f"nw {coord}")

def northEast(coord):
    x, y = coord
    global sum
    try:
        if matrix[x+1][y-1] == b'M' and matrix[x+2][y-2] == b'A' and matrix[x+3][y-3] == b'S' and y >= 3 and x <= shape[0] -4:
            sum += 1
            print(f"ne {coord}")
    except Exception as e:
        pass

def southEast(coord):
    x, y = coord
    global sum
    try:
        if matrix[x+1][y+1] == b'M' and matrix[x+2][y+2] == b'A' and matrix[x+3][y+3] == b'S' and y <= shape[1] -4 and x <= shape[0] -4:
            sum += 1
            print(f"se {coord}")
    except Exception as e:
        pass

def southWest(coord):
    x, y = coord
    global sum
    try:
        if matrix[x-1][y+1] == b'M' and matrix[x-2][y+2] == b'A' and matrix[x-3][y+3] == b'S' and y <= shape[1] -4 and x >= 3:
            print(f"sw {coord}")
            sum += 1
    except Exception as e:
        pass


def main():
    global shape
    global matrix
    matrix = np.genfromtxt("input.txt", delimiter=1, dtype=np.character)
    shape = matrix.shape
    a = np.where(matrix == b'X')
    listA = tuple(zip(*a))
    for coord in listA:
        east(coord)
        west(coord)

        south(coord)
        north(coord)

        southEast(coord)
        southWest(coord)

        northEast(coord)
        northWest(coord)
    print(sum)

if __name__ == "__main__":
    main()
    print(shape)