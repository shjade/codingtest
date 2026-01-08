nums=[int(input()) for _ in range(10)]
na=[]
for i in range(10):
    na.append(nums[i]%42)

print(len(set(na)))
