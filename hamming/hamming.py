
def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strand Length are not equal")

    # Pythonic Way
    ##return len([strand_a[i] for i in range(len(strand_a))
    ##            if strand_a[i] != strand_b[i]])

    # Memory Efficient Way
    cnt = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            cnt += 1

    return cnt
