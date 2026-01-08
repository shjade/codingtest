n, m = map(int, input().split())
lst = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split())
    lst[i-1:j] = lst[i-1:j][::-1]

print(*lst)