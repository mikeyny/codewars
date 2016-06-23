'''
https://www.codewars.com/kata/550f22f4d758534c1100025a
Task

You have to write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South. The Clojure version returns nil when the path is reduced to nothing.

Examples

dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']) => ['WEST']
dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']) => []'''
def dirReduc(arr):
    for x in range(0, len(arr) - 1):
        try:
            if arr[x] == 'SOUTH':
                arr = check(arr, 'NORTH', x)
            elif arr[x] == 'WEST':
                arr = check(arr, 'EAST', x)
            elif arr[x] == 'EAST':
                arr = check(arr, 'WEST', x)
            elif arr[x] == 'NORTH':
                arr = check(arr, 'SOUTH', x)
        except:
            continue

    return arr


def check(arr, dir, pos):
    if arr[pos + 1] == dir:
        arr.pop(pos)
        arr.pop(pos)
        dirReduc(arr)
    return arr