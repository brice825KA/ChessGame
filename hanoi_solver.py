#! /usr/bin/env python3

src = 0
des = 2
aux = 1


def create_puzzle(n=0) -> list[list[int]]:
    table = []
    pickone = [i for i in range(n, 0, -1)]
    table.append(pickone) 
    table.append([])
    table.append([])
    return table

def moves_disks(n, puzzle, src, des, aux):
    if n == 1:
        if not puzzle[src]:
            return
        puzzle[des].append(puzzle[src].pop())
        print(puzzle)
        return
    moves_disks(n - 1,puzzle, src, aux, des)
    puzzle[des].append(puzzle[src].pop())
    print(puzzle)
    moves_disks(n - 1, puzzle, aux, des, src)
    

def hanoi_solver(n=0):
    puzzle = create_puzzle(n)
    print(puzzle)
    moves_disks(n, puzzle, src, des, aux)
    

disk = int(input('Enter numbers of Disk: '))
hanoi_solver(disk)

