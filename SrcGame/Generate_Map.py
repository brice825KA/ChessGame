def PrintCase(case: str):
    for i in range(len(case)):
        print(case[i], end=" ")
    print()

def ValueAlpha(char: str) -> int:
    dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    return dict[char]

def PrintMap(map: list) -> None:
    count = 8
    for case in map:
        print(count, end=" ")
        PrintCase(case)
        count -= 1
    print("  a b c d e f g h")

def GenerateMap(Row: int, Col: int) -> list:
    map = [[0] * (Row) for i in range(Row)]
    return map
