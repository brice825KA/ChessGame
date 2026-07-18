from SrcGame.GetPositionPlayer import GetPosPlayer
from SrcGame.Generate_Map import PrintMap

def LoopGame(map: list):
    position = []
    count = 0
    print("Type 'exit' to quit the game.")
    while True:
        tmp = count
        if count % 2 == 0:
            print("White player turn")
            position = input("Enter position: ")
            if position == "exit":
                print("Black win by forfeit")
                break
            position = GetPosPlayer(position)
            org = map[position[1]][position[0]]
            char = map[position[3]][position[2]]
            if position == [0, 0, 0, 0] or org.isupper() == 1 or map[position[3]][position[2]] != '0' or map[position[1]][position[0]] == '0' or char.islower() == 1:
                print("Invalid position, try again")
                count = tmp
                continue
            current = map[position[1]][position[0]]
            map[position[1]][position[0]] = '0'
            map[position[3]][position[2]] = current
            PrintMap(map)
        else:
            position = input("Enter position: ")
            print("Black player turn")
            if position == "exit":
                print("White win by forfeit")
                break
            position = GetPosPlayer(position)
            org = map[position[1]][position[0]]
            char = map[position[3]][position[2]]
            if position == [0, 0, 0, 0] or org.islower() == 1 or map[position[3]][position[2]] != '0' or map[position[1]][position[0]] == '0' or char.isupper() == 1:
                print("Invalid position, try again")
                count = tmp
                continue
            current = map[position[1]][position[0]]
            map[position[1]][position[0]] = '0'
            map[position[3]][position[2]] = current
            PrintMap(map)
        count += 1
