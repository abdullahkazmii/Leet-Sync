from typing import List


def finalValueAfterOperations(operations: List[str]) -> int:
    x = 0
    for operation in operations:
        if operation in ["--X", "X--"]:
            x -= 1
        elif operation in ["X++", "++X"]:
            x += 1
    return x


print(finalValueAfterOperations(["--X", "X++", "X++"]))  # Output: 1
print(finalValueAfterOperations(["++X", "++X", "X++"]))  # Output: 3
print(finalValueAfterOperations(["X--", "--X", "X++"]))  # Output: -1
