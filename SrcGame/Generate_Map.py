def PrintCase(case: str):
    for i in range(len(case)):
        print(case[i], end=" ")
    print()

def ValueAlpha(char: str) -> int:
    dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
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
