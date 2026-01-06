A,B=map(int,input().split())
C=int(input())

a_time=(A*60+B+C)

A=a_time//60
B=a_time%60
if A>=24:
    A-=24

print(A,B)