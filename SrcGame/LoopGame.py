from GetPositionPlayer import GetPosPlayer


def LoopGame(map: list):
    position = []
    while True:
        position = input("Enter position: ")
        if position == "exit":
            break
        position = GetPosPlayer(position)
        print(position)
