for tc in range(int(input())):
    a, b = map(int,input().split())
    if a > b:
        a,b = b,a
    answer = 0 
    while a < b:
        if 8 * a <= b:
            a *= 8
        elif 4 * a <= b:
            a *= 4
        elif 2 * a <= b:
            a *= 2
        else:
            print(-1)
            break
        answer += 1
    if a == b:
        print(answer)