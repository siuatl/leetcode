def finalPositionOfSnake(n: int, commands: list[str]) -> int:

    pos = [0, 0]
    for c in commands:
        if c == "RIGHT":
            pos[1] += 1
        if c == "LEFT":
            pos[1] -= 1
        if c == "UP":
            pos[0] -= 1
        if c == "DOWN":
            pos[0] += 1

    return pos[0] * n + pos[1]


print(finalPositionOfSnake(2, ["RIGHT", "DOWN"]))
print(finalPositionOfSnake(3, ["DOWN", "RIGHT", "UP"]))
