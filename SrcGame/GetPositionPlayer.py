from SrcGame.Generate_Map import ValueAlpha

def extract_coord(coord: str) -> list:
    newcoord = []
    coord.strip()
    newcoord.append([x for x in coord if x != ' ' or x == '\t'])
    return newcoord

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

def GetPosPlayer(coord: str) -> list:
    formatstr = FormatStr(coord)
    position = [0] * 4
    
    if formatstr == 0:
        print(f"Coord invalid: {coord}")
    else:
        coordextract = extract_coord(coord)
        position[0] = ValueAlpha(coordextract[0][0])
        position[2] = ValueAlpha(coordextract[0][2])
        position[1] = 8 - int(coordextract[0][1])
        position[3] = 8 - int(coordextract[0][3])
    if position[2] not in range(0, 8) or position[3] not in range(0, 8):
        return [0, 0, 0, 0]
    return position