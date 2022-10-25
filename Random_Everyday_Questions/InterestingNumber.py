def interesting(n: int) -> int:
    total = 0
    for i in range(n + 1):
        if any(str(i).__contains__(str(j)) for j in [1, 2, 9, 0]):
            total += i
    return total

print(interesting(40))
