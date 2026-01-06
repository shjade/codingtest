dice=list(map(int,input().split()))
A,B,C=dice
if (A==B) and (B==C):
    money=10000+(1000*A)
elif (A!=B) and (A!=C) and (B!=C):
    money=max(dice)*100
else:
    if (A==B) or (A==C):
        same=A
    else:
        same=B
    money=1000+100*same

print(money)