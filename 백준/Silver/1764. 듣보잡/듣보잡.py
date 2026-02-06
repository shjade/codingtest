N,M = map(int,input().split())
s= set(input().strip() for _ in range(N))
ans=sorted(name for _ in range(M) if (name := input().strip()) in s)
print(len(ans), *ans, sep="\n")