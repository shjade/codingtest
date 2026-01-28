while True:
    a = list(map(int, input().split()))
    rtri = sorted(a)

    if rtri[0] == 0:
        break

    if rtri[0] == 0:
        print('wrong')
    elif (rtri[0])**2 + (rtri[1])**2 == (rtri[2])**2:
        print('right')
    else:
        print('wrong')
