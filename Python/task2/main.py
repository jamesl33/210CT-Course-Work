#!/usr/bin/python3

from queen import Queen

def main():
    for i in range(8):
        solver = Queen(8)
        print("Solution {0} - {1}".format(i + 1, solver.place_queen(i)))

main()

################# Pseudo Code #################

# solve(pos=0)
#   boardState = []
#   IF LEN(boardState)
#       FOR i = pos; pos < 8
#           IF safe_placement(LEN(boardState))
#               boardState APPEND i
#               RETURN solve()
#       lastQueenRow = boardState.pop()
#       return solve(lastQueenRow + 1)

################# Pseudo Code #################
