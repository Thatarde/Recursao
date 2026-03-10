def fatorial(n: int) -> int:
    """
    Calcula o fatorial de n recursivamente
    Lógica:
        fatorial(4) = 4 * fatorial(3)
        fatorial(3) = 3 * fatorial(2)
        fatorial(2) = 2 * fatorial(1)
        fatorial(1) = 1
        → 4 * 3 * 2 * 1 = 24
    """
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(4))
