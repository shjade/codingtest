a = [int(input()) for _ in range(28)]
lst = list(range(1, 31))
res = sorted(set(lst) - set(a))
print(*res, sep='\n')