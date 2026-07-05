def FillMap(map: list) ->list:
    map[1] = ['P' for case in map[1]]
    map[6] = ['p' for case in map[6]]
    
    map[7][0], map[7][7] = 'r', 'r'
    map[0][0], map[0][7] = 'R', 'R'
    map[0][1], map[0][6] = 'N', 'N'
    map[7][1], map[7][6] = 'n', 'n'
    map[0][2], map[0][5] = 'B', 'B'
    map[7][2], map[7][5] = 'b', 'b'
    map[0][3] = 'Q'
    map[7][3] = 'q'
    map[0][4] = 'K'
    map[7][4] = 'k'    
    return map