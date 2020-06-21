for tc in range(int(input())):
    a, b, n = map(int,input().split())
    answer = max(a,b)
    count = 0
    while answer <= n:
        if a > b:
            b += a
            answer = b
        else:
            a += b
            answer = a
        count += 1
    print(count)