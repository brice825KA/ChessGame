
from Generate_Map import ValueAlpha

def FormatStr(coord: str) -> int | str:
    newcoord = []
    newcoord = list(coord.strip())
    universe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    formatcoord = [x for x in newcoord if x != ' ' or x == '\t']
    if len(formatcoord) != 4:
        return 0
    if formatcoord[0].islower() == 0 or formatcoord[2].islower() == 0:
        return 0
    elif formatcoord[1].isdigit() == 0 or formatcoord[3].isdigit() == 0:
        return 0
    elif formatcoord[0] not in universe or formatcoord[2] not in universe:
        return 0
    return str(formatcoord)

def GetPosPlayer(coord: str, map: list) -> list:
    formatstr = FormatStr(coord)
    position = [0] * 2
    if formatstr == 0:
        print(f"Coord invalid: {coord}")
    else:
        position[0]
    return map