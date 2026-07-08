#! /usr/bin/env python3

import sys
from SrcGame.Generate_Map import GenerateMap
from SrcGame.FillingMap import FillMap
from SrcGame.Generate_Map import PrintMap
from SrcGame.LoopGame import LoopGame

def main():
    mapchess = GenerateMap(8, 8)
    mapchess = FillMap(mapchess)
    PrintMap(mapchess)
    LoopGame(mapchess)
    sys.exit(0)

if __name__ == "__main__":
    main()