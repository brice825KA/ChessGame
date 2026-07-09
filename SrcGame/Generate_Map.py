def PrintCase(case: str):
    for i in range(len(case)):
        print(case[i], end=" ")
    print()

def ValueAlpha(char: str) -> int:
    dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    if char[0] not in dict:
        return -1
    return dict[char[0]]

def PrintMap(map: list) -> None:
    count = 8
    for case in map:
        print(count, end=" ")
        PrintCase(case)
        count -= 1
    print("  a b c d e f g h")

def GenerateMap(Row: int, Col: int, shame: str='0') -> list:
    map = [[shame] * (Row) for i in range(Row)]
    return map
