def find_empty_location(puzzle, location):
    for row in range(len(puzzle)):
        for col in range(len(puzzle)):
            if (puzzle[row][col] == 0):
                location[0] = row
                location[1] = col


def present_in_row(puzzle, row, value):
    for i in range(len(puzzle)):
        if (puzzle[row][i] == value):
            return True

    return False


def present_in_col(puzzle, col, value):
    for i in range(len(puzzle)):
        if(arr[i][col] == value):
            return True

    return False


def present_in_small_box(puzzle, row, col, value):
    for i in range(len(puzzle) // 3):
        for j in range(len(puzzle) // 3):
            if (puzzle[i + row][j + col] == value):
                return True

    return False


def check_location_safe(puzzle, row, col, value):
    if (not present_in_row(puzzle, row, value) and
        not present_in_col(puzzle, col, value) and
            not present_in_small_box(puzzle, row - row % 3, col - col % 3, value)):
        return True

    return False


def display_puzzle(puzzle):
    for i in puzzle:
        print(i)


def solver(puzzle):
    location = [0, 0]

    # checking if there is an empty position in the puzzle (0 means unfilled position)
    if (not find_empty_location(puzzle, location)):
        return True

    row = location[0]
    col = location[1]

    for value in range(1, len(puzzle) + 1):
        if (check_location_safe(puzzle, row, col, value)):
            puzzle[row][col] = value

            if(solver(puzzle)):
                return True
            else:
                puzzle[row][col] = 0

    return False


if __name__ == '__main__':

    puzzle = [[0 for x in range(9)]for y in range(9)]

    puzzle = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
              [5, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 0, 0, 3, 1],
              [0, 0, 3, 0, 1, 0, 0, 8, 0],
              [9, 0, 0, 8, 6, 3, 0, 0, 5],
              [0, 5, 0, 0, 9, 0, 6, 0, 0],
              [1, 3, 0, 0, 0, 0, 2, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 7, 4],
              [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if(solver(puzzle)):
        display_puzzle(puzzle)
    else:
        print('The solution does not exist')
