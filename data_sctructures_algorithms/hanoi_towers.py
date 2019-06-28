def hanoi(n, rod_from, rod_middle, rod_to):
    if n == 1:
        print("Plate 1 from %s to %s" % (rod_from, rod_to))
        return
    hanoi(n - 1, rod_from, rod_to, rod_middle)
    print("plate %s from %s to %s" % (n, rod_from, rod_to))
    hanoi(n - 1, rod_middle, rod_from, rod_to)


hanoi(3, "A", "B", "C")
