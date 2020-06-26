for tc in range(int(input())):
    N = int(input())
    a = list(map(int,input().split()))
    tmp = [0,0]
    for i in range(N):
        if i % 2:
            if not a[i] % 2:
                tmp[0] += 1
        else:
            if a[i] % 2:
                tmp[1] += 1
    if tmp[0] == tmp[1]:
        print(tmp[0])
    else:
        print(-1)