from SrcGame.GetPositionPlayer import GetPosPlayer

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
            if position == [0,0, 0, 0]:
                print("Invalid position, try again")
                count = tmp
                continue
        else:
            position = input("Enter position: ")
            print("Black player turn")
            if position == "exit":
                print("White win by forfeit")
                break
            position = GetPosPlayer(position)
            if position == [0, 0, 0, 0]:
                print("Invalid position, try again")
                count = tmp
                continue
        count += 1
